import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = "transcripts"
    allowed_domains = ["subslikescript.com"]
    # start_urls = ["https://subslikescript.com/movies"]
    start_urls = ["https://subslikescript.com/movies_letter-X"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")) , callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]")) , ),

    )
    def parse_item(self, response):
        # item = {}
        # #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # #item["name"] = response.xpath('//div[@id="name"]').get()
        # #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item


        article=response.xpath("//article[@class='main-article']")
        transcipt_list= article.xpath("./div[@class='full-script']/text()").getall()
        transcipt_string= ' '.join(transcipt_list)

        yield{
            'title': article.xpath("./h1/text()").get(),
            'plot': article.xpath("./p/text()").get(),
            # 'transcript': article.xpath("./div[@class='full-script']/text()").getall(),
            'transcript': transcipt_string, #for sql
            'url': response.url,
        }
