from model.pricemodel import Price
from dao import pricedao
from sqlalchemy.orm import Session


class PriceBusiness:

    def __init__(self, session: Session):
        self.session: Session = session

    def save(self, price: Price) -> Price:
        saved = pricedao.save_price(self.session, price)
        if saved:
            return saved
        else:
            return None

def getBusinessPrice(session: Session):
    return PriceBusiness(session)