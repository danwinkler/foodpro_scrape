import scrapy
from scraper.items import FoodItem


class FoodproSpider(scrapy.Spider):
    name = "foodpro"
    allowed_domains = ["utexas.edu"]
    start_urls = [
        "http://hf-foodweb.hf.utexas.edu/foodpro/pickMenu2.asp?locationNum=01&locationName=Jester+City+Limits&dtdate=05%2F18%2F2015&mealName=Breakfast&sName=University+of+Texas+-+Division+of+Housing+%26+Food+Service"
    ]
    download_delay = .5

    def parse( self, response ):
        #if on menu
        if response.css('a'):
            for url in response.xpath('//a/@href').extract():
                yield scrapy.Request("http://hf-foodweb.hf.utexas.edu/foodpro/" + url, callback=self.parse)
        else:
            yield FoodItem(
                name=response.css('.labelrecipe::text').extract()[0],
                allergens=response.css('.labelallergensvalue::text').extract()[0].split(", "),
                meal="Breakfast"
            )
