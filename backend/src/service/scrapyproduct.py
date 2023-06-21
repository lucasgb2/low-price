import asyncio
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import os


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

    def getDriver(self):
        try:
            driver = None
            driver_name: str = 'chrome'
            if os.environ.get('DRIVERSCRAPY') is not None:
                driver_name = os.environ['DRIVERSCRAPY']

            if driver_name == 'firefox':
                firefox_options: FirefoxOptions = webdriver.FirefoxOptions()
                firefox_options.add_argument('-headless')
                firefox_options.add_argument("-disable-gpu")
                firefox_options.add_argument("-no-sandbox")

                if os.environ.get("FIREFOX_BIN") is not None:
                    print('Path Binary: '+os.environ.get("FIREFOX_BIN"))
                    firefox_options.binary = FirefoxBinary(os.environ.get("FIREFOX_BIN"))

                executable_path = 'geckodriver'
                if os.environ.get("FIREFOXDRIVER_PATH") is not None:
                    print('Path Drive: ' + os.environ.get("FIREFOXDRIVER_PATH"))
                    executable_path = os.environ.get("FIREFOXDRIVER_PATH")

                driver = webdriver.Firefox(options=firefox_options, executable_path=executable_path)
            else:
                chrome_options: ChromeOptions = webdriver.ChromeOptions()
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument("--no-sandbox")
                #https://stackoverflow.com/questions/45631715/downloading-with-chrome-headless-and-selenium/73840130#73840130
                chrome_options.add_argument("--headless=new")

                if os.environ.get("GOOGLE_CHROME_BIN") is not None:
                    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

                executable_path = 'chromedriver'
                if os.environ.get("CHROMEDRIVER_PATH") is not None:
                    executable_path = os.environ.get("CHROMEDRIVER_PATH")

                driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

            return driver
        except NameError:
            print(NameError)
            raise NameError


    async def __get_data(self):
        try:
            driver = self.getDriver()
            driver.get(self.get_url())
            elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'product_description')))
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

        except NameError:
            print(NameError.name)
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
