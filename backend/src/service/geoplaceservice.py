import asyncio
from geopy.geocoders import Nominatim
from model.marketplacemodel import Marketplace


class GeoPlaceService:

    def __init__(self, longitude: str, latitude: str):
        self.marketplace: Marketplace = Marketplace(longitude=0, latitude=0)
        self.longitude: str = longitude
        self.latitude: str = latitude


    async def __get_data(self):
        geoLoc = Nominatim(user_agent="GetLoc")
        address = geoLoc.reverse(f'{self.longitude}, {self.latitude}')

        print(address.raw)
        if hasattr(address, 'raw'):
            if 'place_id' in address.raw:
                self.marketplace.place_id = address.raw['place_id']
            if 'display_name' in address.raw['address']:
                self.marketplace.name = address.raw['address']['shop']
            elif 'amenity' in address.raw['address']:
                self.marketplace.name = address.raw['address']['amenity']
            elif 'road' in address.raw['address']:
                self.marketplace.name = address.raw['address']['road']
                if 'town' in address.raw['address']:
                    self.marketplace.name = self.marketplace.name + ', '+address.raw['address']['town']+'-'+address.raw['address']['state']

            if 'city' in address.raw['address']:
                self.marketplace.city = address.raw['address']['city']
            self.marketplace.longitude = self.longitude
            self.marketplace.latitude = self.latitude


    async def __execute(self):
        try:
            event_loop = asyncio.get_running_loop()
        except:
            event_loop = None

        if event_loop and event_loop.is_running():
            task = event_loop.create_task(self.__get_data())
        else:
            task = asyncio.create_task(self.__get_data())
        await task

    async def fill(self):
        await self.__execute()
