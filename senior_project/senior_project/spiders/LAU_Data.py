import scrapy
from scrapy.crawler import CrawlerProcess
import pathlib
import datetime
class LAUDataSpider(scrapy.Spider):
    name = 'LAU_data'
    start_urls = ['https://www.bls.gov/web/laus/lauhsthl.htm']

    def parse(self, response):
        self.logger.debug(response.text)  # print the page source to check if it's correct
        # Extract the state names from the "td" elements in the first row of the table
        for i, row in enumerate(response.xpath('//table[@class="regular"]//tr')):
            # Skip the first row since it contains the state names
            if i == 0:
                continue
            yield {
                'state': row.xpath('th[1]//text()').get(),
                'February 2023 rate': row.xpath('td[1]//text()').get(),
                'Historical High Date': row.xpath('td[2]//text()').get(),
                'Historical High Rate': row.xpath('td[3]//text()').get(),
                'Historical Low Date': row.xpath('td[4]//text()').get(),
                'Historical Low Rate': row.xpath('td[5]//text()').get(),
            }
        self.logger.info('Finished scraping')  # log when the spider is finished

filename = "senior_project\senior_project\CSVs\LAU_Data_" + str(datetime.date.today())
process = CrawlerProcess(settings={
    "FEEDS": {
        "{}.csv".format(filename): {
        'format': 'csv'}
    },
})

process.crawl(LAUDataSpider)
process.start() # the script will block here until the crawling is finished
