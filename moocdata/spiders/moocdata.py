import scrapy

import json

from pprint import pprint

from moocdata.items import MoocDataItem

class moocdataSpider(scrapy.spiders.Spider):

    name = 'xuetang'

    allowed_domains = ['www.xuetangx.com/']

    url_pat = 'https://www.xuetangx.com/api/v1/lms/get_product_list/?page={}'

   

    data = '{"query":"","chief_org":[],"classify":[],"selling_type":[],"status":[],"appid":10000}'



    headers = {

    'Host': 'www.xuetangx.com',

    'authority': 'www.xuetangx.com',

    'method': 'POST',

    'path': '/api/v1/lms/get_product_list/?page=1',

    'scheme': 'https',

    'accept': 'application/json, text/plain, */*',

    'accept-encoding': 'gzip, deflate, br',

    'accept-language': 'zh',

    'content-type': 'application/json',

    'cookie': '_ga=GA1.2.192047866.1605620269; provider=xuetang; django_language=zh',

    'django-language': 'zh',

    'origin': 'https://www.xuetangx.com',

    'referer': 'https://www.xuetangx.com/search?query=&org=&classify=&type=&status=&page=1',

    'sec-fetch-dest': 'empty',

    'sec-fetch-mode': 'cors',

    'sec-fetch-site': 'same-origin',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',

    'x-client': 'web',

    'xtbz': 'xt'

    }

    def start_requests(self):

         #"""使用start_requests创建post请求"""

        for page in range(1, 883):

         #"""爬取n页信息"""

            yield scrapy.FormRequest(

            url = self.url_pat.format(page),

            headers = self.headers,

            method = 'POST',

            body = self.data,

            callback = self.parse

            )

    def parse(self, response):

        msg= json.loads(response.body)
        print(len(msg['data']['product_list']))

        for each in msg['data']['product_list']:

            item = MoocDataItem()

            item['name'] = each['name']

            item['school'] = each['org']['name']

            item['peopleNum'] = each['count']

            if 'classify_name' in each and each['classify_name']:
                item['course_type'] = ' '.join(each['classify_name'])
            else:
                item['course_type'] = "None"
                

            item['sell_type'] = each['sell_type_name']
  

            if 'tag_titles' in each and each['tag_titles']:
                item['tags'] = ' '.join(each['tag_titles'])
            else:
                item['tags'] = "None"

            item['intro'] = each['short_intro'].replace('\n', ' ').replace('"', '').strip()


            yield item


