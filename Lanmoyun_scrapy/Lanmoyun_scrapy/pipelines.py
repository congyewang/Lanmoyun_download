# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

s = 0

class LanmoyunScrapyPipeline(object):
    def __init__(self):
        self.file = open(r"Sum.txt", "a+")

    def process_item(self, item, spider):
        title = item["title"]
        ans_sum = item["ans_sum"]
        curr = item["curr"]
        global s
        for i in range(len(title)):
            for j in range(len(title[i])):
                s = s + 1
                self.file.write(f'{s}、{title[i][j][0]}\n')
                for k in range(len(ans_sum[i][j])):
                    self.file.write(f'{chr(65 + k)}、{ans_sum[i][j][k]}\n')
                    self.file.write(f'{"".join(curr[i][j][k])}\n\n')

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()
