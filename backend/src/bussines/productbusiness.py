from typing import List
from model.productmodel import Product
from model.pricemodel import Price
from model.gtinmodel import Gtin
from service.scrapyproduct import ScrapyProduct
from dao.productdao import ProductDAO
from dao.pricedao import PriceDAO
from fastapi.responses import JSONResponse


class ProductBusiness:


    async def save(self, gtin: Gtin) -> Product:
        product_saved : Product = await ProductDAO.factory().get_product_by_gtin(gtin.gtin)
        if product_saved:
            return product_saved
        else:
            new_product: Product = await self.__fill_product_information(gtin)
            if new_product is not None:
                product_saved = await ProductDAO.factory().save_product(new_product)
                return product_saved
            else:
                return None

    async def __fill_product_information(self, gtin: Gtin) -> Product:
        scrapy: ScrapyProduct = ScrapyProduct(gtin.gtin)
        try:
            await scrapy.fill()
            product: Product = Product()
            product.gtin = gtin.gtin
            product.description = scrapy.description
            product.ncm = scrapy.ncm
            product.linkimage = scrapy.linkImage
            product.ncmDescription = scrapy.ncmdescription
            return product
        except NameError:
            return None

    async def get_product_by_gtin(self, gtin: str):
        product =  await ProductDAO.factory().get_product_by_gtin(gtin)
        return product

    async def get_product_all(self) -> List[Product]:
        productsmaxmin: List[Product] = await ProductDAO.factory().get_product_all()
        products = []
        for p in productsmaxmin:
            p_max = await PriceDAO.factory().get_max_price_by_product(p['_id'])
            p_min = await PriceDAO.factory().get_min_price_by_product(p['_id'])
            p['pricemax'] = p_max
            p['pricemin'] = p_min
            products.append(p)

        return products


    async def get_price_by_gtin(self, gtin: str) -> List[Price]:
        product : Product = await ProductDAO.factory().get_product_by_gtin(gtin)
        price = await PriceDAO.factory().get_price_by_idproduct(product.to_id())
        return price

    @classmethod
    def factory(self):
        return ProductBusiness()

