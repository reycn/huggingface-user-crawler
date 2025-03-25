'''
Author: Rongxin rongxin@u.nus.edu
Date: 2024-11-20 16:08:10
LastEditors: Rongxin rongxin@u.nus.edu
LastEditTime: 2025-03-26 01:08:21
FilePath: /hugging-face-user-scrawler/hf_user_scrawler/hf_user_scrawler/pipelines.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HfUserScrawlerPipeline:
    def process_item(self, item, spider):
        return item
