import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ScrapyProduct:
    def __init__(self, gtin: str):
        self.urlscrapy: str = 'https://cosmos.bluesoft.com.br/produtos/{0}'
        self.gtin: str = gtin
        self.description: str = ''
        self.ncm: str = ''
        self.linkImage: str = ''
        self.ncmdescription: str = ''


    def get_url(self):
        return self.urlscrapy.format(self.gtin)


    async def __get_data(self):
        try:
            driver = webdriver.Chrome()
            driver.get(self.get_url())
            elem = driver.find_element(By.ID, 'product_description')
            if elem:
                self.description = elem.text

            elem: WebElement = driver.find_element(By.CLASS_NAME, 'ncm-name')
            if elem:
                self.ncmdescription = elem.text
                for i, c in enumerate(elem.text):
                    if '-' in c:
                        break
                    else:
                        self.ncm = self.ncm + c
                self.ncm = self.ncm.replace('.', '').replace(' ', '')

            elem = driver.find_element(By.CLASS_NAME, 'product-thumbnail').find_element(By.TAG_NAME, 'img')
            if elem:
                self.linkImage = elem.get_attribute('src')

        except:
            self.description: str = 'PRODUTO NÃO CATALOGADO'

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