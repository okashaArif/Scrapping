import scrapy
import json

class AssignmentapiSpider(scrapy.Spider):
    name = "AssignmentAPI"
    allowed_domains = ["www.daraz.pk"]
    start_urls = ["https://www.daraz.pk/mens-t-shirts/?ajax=true&page=2&spm=a2a0e.home.cate_3.1.35e34076Bkph54"]

    def parse(self, response):
        json_response = json.loads(response.body)
        data = json_response.get('mods').get('listItems')
        for i in data:
            yield {
                'name':i['name'],
                'Nid':i['nid'],
            }
        