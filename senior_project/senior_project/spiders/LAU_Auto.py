import scrapy
import csv
import datetime
from scrapy.crawler import CrawlerProcess
import pandas as pd

class GenericTableSpider(scrapy.Spider):
    name = 'generic_table'
    start_urls = ['https://www.bls.gov/lau/tables.htm']
    #print('test')
    def parse(self, response):
        #self.logger.debug(response.text)  # print the page source to check if it's correct

        # Extract all the links on the page
        links = response.xpath('//a/@href').getall()
        print(links)
        # Loop through each link and yield a new request
        for link in links:
            if "/web/" in link or "/lastrk" in link or "/lastrk" in link or "/lamtrk" in link or "/malrgrank" in link or "/lamtch" in link or "/malrgch" in link:
                yield scrapy.Request(response.urljoin(link), callback=self.parse_table)
            

    def parse_table(self, response):
        #self.logger.debug(response.text)  # print the page source to check if it's correct

        # Extract the header names from the first row of the table
        headers = []
        for header in response.xpath('//table[@class="regular"]//tr'):
            headers.append(header.xpath('th[1]//text()').get())

        # Loop through each row of the table
        for i, row in enumerate(response.xpath('//table[@class="regular"]//tr')):
            # Skip the header row
            if i == 0:
                continue

            # Extract the data from each column of the row
            data = {}
            for j, cell in enumerate(row.xpath('td')):
                data[headers[j]] = cell.xpath('.//text()').get()

            yield data

        self.logger.info('Finished scraping')
        '''
        # Write the data to a CSV file
        date_time = datetime.datetime.now()
        filename = 'table_data'+str(date_time)+'.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for data in response.xpath('//table[@class="regular"]//tr[position()>1]'):
                writer.writerow({headers[j]: cell.xpath('.//text()').get() for j, cell in enumerate(data.xpath('td'))})
        self.logger.info('Saved data to {}'.format(filename))'''

filename = "senior_project\senior_project\CSVs\LAU_Auto_" + str(datetime.date.today())
process = CrawlerProcess(settings={
    "FEEDS": {
        "{}.json".format(filename): {
        'format': 'json'}
    },
})

process.crawl(GenericTableSpider)
process.start(stop_after_crawl=False) # the script will continue running until it is manually stopped. Anything after this will not run.