'''
Author: Rongxin rongxin@u.nus.edu
Date: 2025-03-25 23:57:52
LastEditors: Rongxin rongxin@u.nus.edu
LastEditTime: 2025-03-26 00:10:36
FilePath: /hugging-face-user-scrawler/hf_user_scrawler/hf_user_scrawler/spiders/example.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import scrapy


class hf_user_scrawler(scrapy.Spider):
    name = "hf_user_scrawler"
    allowed_domains = ["huggingface.co"]
    start_urls = ["https://huggingface.co/user"]

    def parse(self, response):
        # Called when a response is received from the server

        print(response.body)
        pass
