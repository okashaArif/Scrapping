import scrapy


class AssignmentSpider(scrapy.Spider):
    name = "assignment"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["https://www.bbc.com/news/av/world-middle-east-67362960","https://www.bbc.com/news/av/world-middle-east-67365679","https://www.bbc.com/news/av/world-us-canada-67359653",
                  "https://www.bbc.com/news/av/world-us-canada-67352378","https://www.bbc.com/news/av/uk-england-hampshire-67350933"]

    def parse(self, response):
        title= response.xpath("//h1[@id='main-heading']/text()").get()
        paragraphs= response.xpath("//div[@class='ssrcss-1s1kjo7-RichTextContainer e5tfeyi1']")
        for paragraph in paragraphs:
            paragraphText1= paragraph.xpath(".//p/text()").getall()
            yield{
                'Title':title,
                'paragraph':paragraphText1,
                }
