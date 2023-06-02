from typing import List
from model.productmodel import Product
from model.pricemodel import Price
from database.schemas import ProductSchema
from service.scrapyproduct import ScrapyProduct
from dao import productdao, pricedao
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder



class ProductBusiness:

    def __init__(self, session: Session):
        self.session: Session = session

    async def save(self, product: Product) -> Product:
        product_saved = productdao.get_product_by_gtin(self.session, product.gtin)
        if product_saved:
            return product_saved
        else:
            new_product: Product = await self.__fill_product_information(product)
            new_product.gtin = product.gtin
            new_product.linkimage = product.linkimage
            new_product.ncmDescription = product.ncmDescription
            new_product = productdao.save_product(self.session, new_product)
            return new_product

    async def __fill_product_information(self, product: Product) -> Product:
        scrapy: ScrapyProduct = ScrapyProduct(product.gtin)
        await scrapy.fill()
        product.description = scrapy.description
        product.ncm = scrapy.ncm
        product.linkimage = scrapy.linkImage
        product.ncmDescription = scrapy.ncmdescription
        return product

    def get_product_by_gtin(self, gtin: str) -> Product:
        return productdao.get_product_by_gtin(self.session, gtin)

    def get_product_all(self) -> List[Product]:
        productsmaxmin: List[ProductSchema] = productdao.get_product_all(self.session)
        products = []
        for p in productsmaxmin:
            prices = self.__get_maxmin_price_by_product(p.id)
            for price in prices:
                if price['type'] == 'max':
                    p.pricemax = price['price']
                elif price['type'] == 'min':
                    p.pricemin = price['price']
            products.append(p)
        return products

    def get_price_by_product(self, gtin: str) -> List[Price]:
        p: Product = self.get_product_by_gtin(gtin)
        return pricedao.get_price_by_product(self.session, p.id)

    def get_maxmin_price_by_gtin(self, gtin: str) -> List[Price]:
        p: Product = self.get_product_by_gtin(gtin)
        r = self.__get_max_min_price_by_product(self.session, p.id)
        return r

    def __get_maxmin_price_by_product(self, id_product: int) -> List[Price]:
        return pricedao.get_max_min_price_by_product(self.session, id_product)

def getProductBusiness(session: Session) -> ProductBusiness:
    return ProductBusiness(session)
