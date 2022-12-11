import scrapy


class JjSpider(scrapy.Spider):
    name = 'jj'
    allowed_domains = ['www.junaidjamshed.com']
    start_urls = ['https://www.junaidjamshed.com/womens/stitched.html']

    def parse(self, response):
        stiched = response.xpath('//h2/a')
        next_page = response.xpath('//a[@class="action  next"]/@href').extract_first()


        for stich in stiched:
    
            link = stich.xpath(".//@href").get()
            

            yield response.follow(url=link,callback=self.parse_cloth)

            # if next_page is not None:
            #      yield scrapy.Request(response.urljoin(next_page))


    def parse_cloth(self,response):
        name = response.xpath('//h1/span/text()').get()   
        is_stock = response.xpath('//div[@class="stock available"]/span/text()').extract()  
        price = response.xpath('//span[@class="price-container price-final_price tax weee"]/span/@data-price-amount').extract_first()  

        yield{
            'name': name,
            'availablity': is_stock,
            'price':price
        }



