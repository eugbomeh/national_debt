# -*- coding: utf-8 -*-
import scrapy


class GdpDebSpider(scrapy.Spider):
    name = 'gdp_deb'
    allowed_domains = ['worldpopulationreview.com/']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//tbody[@class='jsx-2642336383']/tr")
        for row in rows:
            iname = row.xpath(".//td[1]/a/text()").get()
            NDGR = row.xpath(".//td[2]/text()").get()
            population = row.xpath(".//td[3]/text()").get()            
            yield {
                'country_name': iname,
                'NDGR': NDGR,
                'population': population
            }
