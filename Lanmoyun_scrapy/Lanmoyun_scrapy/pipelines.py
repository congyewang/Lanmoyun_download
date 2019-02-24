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
        s += 1
        self.file.write(f'{s}、{title[0]}()\n')
        for i in range(len(ans_sum)):
            self.file.write(f'{chr(65 + i)}、{ans_sum[i]}\n')
        self.file.write(f'正确答案:{"".join(curr)}\n')
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()
