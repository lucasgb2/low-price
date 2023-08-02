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
            pricemax = await PriceDAO.factory().get_max_price_by_product(product_saved.to_id())
            pricemin = await PriceDAO.factory().get_min_price_by_product(product_saved.to_id())
            product_saved.pricemax = pricemax
            product_saved.pricemin = pricemin
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
        await scrapy.fill()
        if scrapy.fail == False:
            product: Product = Product()
            product.gtin = gtin.gtin
            product.description = scrapy.description
            product.ncm = scrapy.ncm
            product.linkimage = scrapy.linkImage
            product.ncmDescription = scrapy.ncmdescription
            return product
        else:
            return None

    async def get_product_by_gtin(self, gtin: str):
        product = await ProductDAO.factory().get_product_by_gtin(gtin)
        product = await self.__set_min_max_price(product)
        product = await self.__set_statistic(product)
        return product

    async def get_product_by_ncm(self, ncm: str):
        productsncm: List[Product] = await ProductDAO.factory().get_product_by_ncm(ncm)
        products = []
        for p in productsncm:
            p = Product(**p)
            p = await self.__set_min_max_price(p)
            p = await self.__set_statistic(p)
            products.append(p)
        return products


    async def get_product_all(self) -> List[Product]:
        productsmaxmin: List[Product] = await ProductDAO.factory().get_product_all()
        products = []
        for p in productsmaxmin:
            p = Product(**p)
            p = await self.__set_min_max_price(p)
            p = await self.__set_statistic(p)
            products.append(p)
        return products

    async def __set_min_max_price(self, product : Product) -> Product:
        p_max = await PriceDAO.factory().get_max_price_by_product(product.to_id())
        p_min = await PriceDAO.factory().get_min_price_by_product(product.to_id())
        product.pricemax = p_max
        product.pricemin = p_min
        return product

    async def __set_statistic(self, product: Product) -> Product:
        product.contrib =  await PriceDAO.factory().get_count_price(product.to_id())
        return product


    async def get_price_by_gtin(self, gtin: str) -> List[Price]:
        product : Product = await ProductDAO.factory().get_product_by_gtin(gtin)
        price = await PriceDAO.factory().get_price_by_idproduct(product.to_id())
        return price

    async def get_statistic(self, gtin: str) -> int:
        product: Product = await ProductDAO.factory().get_product_by_gtin(gtin)
        return await PriceDAO.factory().get_count_price(product.to_id())

    @classmethod
    def factory(self):
        return ProductBusiness()

