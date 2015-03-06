from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from MGcrawler.items import MgcrawlerItem

class MGSpider(BaseSpider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]
	#def parse(self,response):
	#	fHandle = open("test.txt","w")
	#	fHandle.write(response.body)
	#	fHandle.close()

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//ul/li')
		items = []
		for site in sites:
			item = MgcrawlerItem()
			item['title'] = site.select('a/text()').extract()
			item['link'] = site.select('a/@href').extract()
			item['desc'] = site.select('text()').extract()
			items.append(item)
		return items

		#filename = response.url.split("/")[-2]
		#open(filename, 'wb').write(response.body)
