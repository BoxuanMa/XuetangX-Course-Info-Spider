# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter

import csv

class CoursePipeline(object):

    def open_spider(self, spider):

        try:

            self.file = open('CourseData.csv', 'a', encoding='utf-8', newline = '')

            self.csv = csv.writer(self.file)

            column_names = ['name', 'school', 'peopleNum','course_type', 'sell_type', 'tags', 'intro']

            self.csv.writerow(column_names)

        except Exception as e:

            print(e)

    def process_item(self, item, spider):

        self.csv.writerow(list(item.values()))

        return item

    def close_spider(self, spider):

        self.file.close()

