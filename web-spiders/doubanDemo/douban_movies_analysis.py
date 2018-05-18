# -*- coding: utf-8 -*-
import random
import re

import jieba
import numpy
import matplotlib
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from os import path
from PIL import Image
from bs4 import BeautifulSoup as bs
import time

from Spiders.learningDemos.doubanDemo.ip_proxies import IPProxy

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)

from wordcloud import WordCloud

__author__ = 'rovo98'

d = path.dirname(__file__)
default_fonts = [os.path.join(d, "fonts/STXINGKA.TTF")]
default_backgrounds = [os.path.join(d, 'background/stormtrooper_mask.png')]


class DouBanAnalysis:
    def __init__(self, headers, url, font=default_fonts, img=default_backgrounds, save=False):
        self.now_playing_list = []
        self.url = url
        self.ip_proxy = IPProxy(headers=headers)
        self.headers = headers
        self.font = font
        self.bg = img
        self.isSave = save

    # 爬取正在热映的电影的subject id.
    def get_now_playing_movie_list(self):
        try:
            res = requests.get(self.url, timeout=30,
                               headers=self.headers,proxies=self.ip_proxy.get_random_ip())
            res.raise_for_status()
            res.encoding = res.apparent_encoding

            soup = bs(res.text, 'html.parser')
            now_playing_movie = soup.find_all('div', id='nowplaying')[0].find_all('li', attrs={'class': 'list-item'})
            for subject in now_playing_movie:
                movie = {}
                movie['id'] = subject.get('data-subject')
                movie['title'] = subject.get('data-title')
                self.now_playing_list.append(movie)
        except Exception as e:
            print('获取热映电影出错! :', e)
            return None

    # 获取每一部电影的评论
    def get_comments_by_id(self, movie_id, page_num):
        each_comment_list = []

        if page_num > 0:
            start = (page_num - 1) * 20
        else:
            return False
        try:
            req_url = 'https://movie.douban.com/subject/' + movie_id + '/comments?start=' + str(start) + '&limit=20'

            res = requests.get(req_url, timeout=30,
                               headers=self.headers,proxies=self.ip_proxy.get_random_ip())
            res.raise_for_status()
            res.encoding = res.apparent_encoding
            soup = bs(res.text, 'html.parser')

            comments = soup.find_all('div', attrs={'class': 'comment'})

            for each in comments:
                each_comment_list.append(each.find_all('p')[0].string)

            return each_comment_list
        except:
            print('爬取评论出错!')
            return None

    # 清洗数据
    def clean_data(self, comment_list):
        # 将里列表转化为字符串
        comments = ''
        for k in range(len(comment_list)):
            comments = comments + (str(comment_list[k]).strip())
        # 使用正则表达式去除标点符号
        pattern = re.compile(r"[\u4e00-\u9fa5]+")
        filter_data = re.findall(pattern, comments)
        cleaned_comments = ''.join(filter_data)

        # 使用结巴分词进行中文分词
        segment = jieba.lcut(cleaned_comments)
        words_df = pd.DataFrame({'segment': segment})
        # 去掉停用词
        stopwords = pd.read_csv('stopwords.txt', index_col=False, quoting=3, sep='\t', names=['stopword'],
                                encoding='utf-8')
        words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

        # 统计词频
        words_stat = words_df.groupby(by=['segment'])['segment'].agg({'计数': numpy.size})
        words_stat = words_stat.reset_index().sort_values(by=['计数'], ascending=False)

        return words_stat

    # 用词云进行显示
    def word_cloud_show(self, words_stat, title):
        color = ['white', 'black']

        # 统计词频
        word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}
        word_frequence_dict = {}
        for key in word_frequence:
            word_frequence_dict[key] = word_frequence[key]

        if len(word_frequence_dict) < 1:
            print('该电影没有词频')
            return
        img = np.array(Image.open(random.choice(self.bg)))
        wd = WordCloud(font_path=random.choice(self.font),max_font_size=120,
                               background_color=random.choice(color),mask=img,margin=10).fit_words(word_frequence_dict)


        # 显示词云图片
        # img_coloring = np.array(Image.open(self.bg))
        # plt.imshow(word_cloud, interpolation="bilinear")
        plt.imshow(wd)
        plt.title(u''+title)
        plt.axis('off')
        plt.show()
        if self.isSave:
            dir = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            if path.exists(dir) is False:
                os.mkdir(dir)
            wd.to_file(dir + '/' + title + '.png')

    # start up the spider.
    def run(self):
        self.get_now_playing_movie_list()
        count = 0
        # for each_movie in self.now_playing_list:
        for each_movie in self.now_playing_list:
            comments = []
            count = count + 1
            # 每部电影爬5个评论页面
            for i in range(5):
                num = i + 1
                comment_temp = self.get_comments_by_id(each_movie['id'], num)
                comments.append(comment_temp)

            words_stat = self.clean_data(comments)
            self.word_cloud_show(words_stat, each_movie['title'])
            print('第', count, '部电影爬取分析完成!')


# Driver the program to test the method above.
if __name__ == "__main__":
    url = 'https://movie.douban.com/nowplaying/guangzhou/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    # 随机是使用字体和mask图.
    d = path.dirname(__file__)
    bg_path = path.join(d, 'background/')
    font_path = path.join(d, 'fonts/')
    fonts = []
    backgrounds = []
    for img in os.listdir(bg_path):
        backgrounds.append(path.join(bg_path, img))
    for font in os.listdir(font_path):
        fonts.append(path.join(font_path, font))

    doubanSpider = DouBanAnalysis(headers=headers, img=backgrounds, font=fonts, url=url,save=True)
    doubanSpider.run()
