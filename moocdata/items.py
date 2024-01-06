# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoocDataItem(scrapy.Item):

    name = scrapy.Field() # 课程名

    school = scrapy.Field() # 学校

    peopleNum = scrapy.Field() # 选课人数

    course_type = scrapy.Field()

    sell_type = scrapy.Field()

    tags = scrapy.Field()

    intro = scrapy.Field()

    pass

