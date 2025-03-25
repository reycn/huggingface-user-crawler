'''
Author: Rongxin rongxin@u.nus.edu
Date: 2025-03-25 23:57:52
LastEditors: Rongxin rongxin@u.nus.edu
LastEditTime: 2025-03-26 01:10:22
FilePath: /hugging-face-user-scrawler/hf_user_scrawler/hf_user_scrawler/spiders/example.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import re
from os import path

import pandas as pd
import requests as rq
import scrapy
from rich import print as pp


class hf_user_scrawler(scrapy.Spider):
    name = "hf_user_scrawler"
    allowed_domains = ["huggingface.co"]
    df_path = "../data/task/huggingface_users.csv"
    pp(f"[blue bold][>>] Reading {df_path} for urls...[/]")
    df_start = pd.read_csv(df_path).head(100)
    start_urls = df_start["url"].tolist()
    # start_urls += ["https://huggingface.co/JustinLin610"]
    pp(f"[green bold][<<] Successfully retrieved {len(start_urls)} urls from the csv file.[/]")

    def rq_followers(self, user_id):
        pp(f"[blue bold][>>] Retrieving the followers of user {user_id}...[/]")
        url = f"https://huggingface.co/api/users/{user_id}/followers"
        response = rq.get(url)
        if response.status_code != 200:
            pp(f"[red bold][<<] Failed to retrieve the followers of user {user_id}...[/]")
            return []
        else:
            pp(f"[green bold][<<] Successfully retrieved the followers of user {user_id}...[/]")
            return response.json()
    def rq_following(self, user_id):
        pp(f"[blue bold][>>] Retrieving the followings of user {user_id}...[/]")
        url = f"https://huggingface.co/api/users/{user_id}/following"
        response = rq.get(url)
        if response.status_code != 200:
            pp(f"[red bold][<<] Failed to retrieve the followings of user {user_id}...[/]")
            return []
        else:
            pp(f"[green bold][<<] Successfully retrieved the followings of user {user_id}...[/]")
            # pp(response.content)
            return response.json()

    def parse(self, response):
        pp(f"[blue bold][>>] Parsing {response.url}...[/]")
        # Extracting the username
        user_id = path.basename(response.url)

        user_name = response.xpath('/html/body/div[1]/main/div/div/section[1]/h1/span/text()').get()
        
        user_meta = response.xpath("/html/body/div[1]/main/div[@data-target='UserProfile']/@data-props").get("")
        # Extracting the team
        team = response.xpath('/html/body/div[1]/main/div/div/section[1]/div[6]/text()').get()

        # Extracting followers count
        pattern_int_number = re.compile(r'[0-9]+')
        follower_amount = response.xpath('/html/body/div[1]/main/div/div/section[1]/div[4]/button[1]/text()').get()
        if follower_amount is not None:
            try:
                follower_amount = int(pattern_int_number.findall(follower_amount)[0])
            except:
                follower_amount = 0
        else:
            follower_amount = 0
        # Extracting follower list
        follower_meta = self.rq_followers(user_id)

        # Note: following api https://huggingface.co/api/users/edmundhui/following
        # Extracting followings count
        following_amount = response.xpath('/html/body/div[1]/main/div/div/section[1]/div[4]/button[2]/text()').get()

        if following_amount is not None:
            try:
                following_amount = int(pattern_int_number.findall(following_amount)[0])
            except:
                following_amount = 0
        else:
            following_amount = 0
        # Extracting followings list
        following_meta = self.rq_following(user_id)
        result_dict = {
            'user_id': user_id,
            'user_name': user_name,
            'user_meta': user_meta,
            'team': team,
            'follower_amount': follower_amount,
            'follower_meta': follower_meta,
            'following_amount': following_amount,
            'following_meta': following_meta,
        }
        pp(result_dict["user_meta"])
        yield result_dict