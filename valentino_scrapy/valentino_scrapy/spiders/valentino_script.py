import scrapy
from datetime import date

from valentino_scrapy.items import ValentinoProduct, ValentinoPrice
from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    name = 'valent2'

    def parse(self, response):
        categories = response.xpath('//ul[@class="level-2"]/li[@id="donna_categories_abbigliamento"]/'
                                    'ul[@class="level-3"]/li/a')
        for category in categories:
            meta = {}
            id = 0
            url_cat = category.xpath('@href').extract_first()
            name_cat = category.xpath('span/text()').extract_first()
            # print(name_cat)
            meta['categories'] = name_cat
            yield scrapy.Request(
                url=url_cat,
                callback=self.get_items,
                meta=meta
            )

    def get_items(self, response):
        items = response.xpath('//ul[@class="products "]/li[@class="item "]/article/div[@class="search-item-info"]/span/a')        #print(items)
        i = 0
        for item in items:
            i = i+1
            url = item.xpath('@href').extract_first()
            yield scrapy.Request(
                url=url,
                callback=self.get_item, meta=response.meta)

    def get_item(self, response):
        product = ValentinoProduct()
        price = ValentinoPrice()
        product['name'] = response.xpath(
            '//h1[@class="item-name"]/div/span[@class="value"]/text()'
        ).extract_first()#.strip()


        product['model'] = response.xpath(
            '//div[@class="modelName outer"]/span[@class="inner modelName"]/text()'
        ).extract_first()  # .strip()

        product['category'] = response.meta['categories']

        product['description'] = response.xpath(
            '//div[@class="attributesUpdater editorialdescription "]/span[@class="value"]'
        ).extract_first()  # .strip()

        product['url'] = response.url

        product['image'] = response.css('div.mainImage ul.alternativeImages img::attr(srcset)').extract()

        product['site'] = 'https://www.valentino.com/'
        print(product)
        yield product

        price['date'] = date.today()

        price['currency'] = '€'
        price1 = response.xpath('//div[@class="item-price"]//span[@class="price"]/'
                               'span[@class="value"]/text()').extract_first()
        if not price1:
            price1 = response.xpath('//div[@class="item-price"]//span[@class="full price"]/'
                                   'span[@class="value"]/text()').extract_first()
        sale_price1 = response.xpath('//div[@class="item-price"]//span[@class="discounted price"]'
                                    '/span[@class="value"]/text()').extract_first()
        size1 = response.css('div.item-sizeSelection span.sizeValue::text').extract()
        price['params'] = {
            'price' :price1,
            'size': size1,
            'sale_price': sale_price1

        }
        yield price