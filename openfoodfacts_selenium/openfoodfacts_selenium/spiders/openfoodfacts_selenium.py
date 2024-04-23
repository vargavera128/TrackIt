import scrapy
import logging
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openfoodfacts_selenium.items import OpenFoodItem

class OpenFoodFactsSpider(scrapy.Spider):
    name = 'openfoodfacts_selenium'
    start_urls = ['https://world.openfoodfacts.org/']

    def __init__(self):
        self.driver = webdriver.Chrome()
        logging.getLogger('selenium').setLevel(logging.WARNING) 

    def parse(self, response):
        self.driver.get(response.url)
        wait = WebDriverWait(self.driver, 10)
    
        # Várunk, amíg az oldal betöltődik
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2.title-1[property='food:name'][itemprop='name']")))

        # Az oldal betöltődése után a Selenium WebDriver page_source tulajdonságával dolgozunk
        sel = Selector(text=self.driver.page_source)
    
        for product_link in sel.css('img#og_image::attr(src)').getall():
            product_url = response.urljoin(product_link)
            yield scrapy.Request(product_url, callback=self.parse_product)

    def parse_product(self, response):
        sel = Selector(text=response.body)
    
        # Próbáljuk meg pontosítani az XPath kifejezéseket
        product_name = sel.xpath("//h2[@class='title-1']/text()").get()
        product_image_url = sel.xpath('//img[@id="og_image"]/@src').get()
    
        # Ellenőrizzük, hogy az adatokat sikerült-e kinyerni
        if product_name and product_image_url:
             print(product_name, product_image_url)

             item = OpenFoodItem()
             item['item_name'] = product_name.strip()
             item['image_url'] = product_image_url.strip()

             yield item
        else:
            self.logger.warning(f"Failed to parse product from {response.url}")

        if product_name and product_image_url:
            print(product_name, product_image_url)

            item = OpenFoodItem()
            item['item_name'] = product_name.strip()
            item['image_url'] = product_image_url.strip()

            yield item
        else:
            self.logger.warning(f"Failed to parse product from {response.url}")

    def closed(self, reason):
        self.driver.quit()
