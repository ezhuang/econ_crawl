import scrapy

class EconCrawlSpider(scrapy.Spider):
    name = "econ_crawl"
    allowed_domains = ["http://tea.share2china.com/"]
    start_urls = ["http://tea.share2china.com/"]
    curr_issue = ""
    
    def parse(self, response):
        baseUrl = self.start_urls[0][:-1]
        yearUrls = [(baseUrl + a) for a in  response.css('div.btn-group a').xpath('@href').extract() if (a.split('/')[1] == "year")]
        for yearUrl in yearUrls:
            yield scrapy.Request(yearUrl, callback = self.handle_year,
                                            errback=self.errback,
                                            dont_filter=True)

    def handle_year(self, response):
        self.logger.info("working on " + response.url)
        baseUrl = self.start_urls[0][:-1]
        issueUrls = [(baseUrl + a) for a in  response.css('.container .btn-group a').xpath('@href').extract()]


    def handle_issue(self, response):
        print "haha"


    def errback(self, failure):
        self.logger.error(repr(failure))
