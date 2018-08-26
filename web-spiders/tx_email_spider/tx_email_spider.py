#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author : rovo98
# date: 2018.7.25
# description : 获取腾讯企业邮箱通讯录信息
import re
import requests

# 运行程序前，需要手动登陆到企业邮箱，获取到'xxx'对应的数据，即 sid 和 cookies 的内容


class Spider:

    def __init__(self):
        """
        初始化
        """
        self.sid = 'xxx'  # 用户登陆后的sid
        # 获取所有组id的链接
        self.all_parties_url = 'https://exmail.qq.com/cgi-bin/laddr_biz?action=show_party_list&sid={sid}' \
                               '&t=contact&view=biz'.format(sid=self.sid)
        # 获取用户信息的链接
        self.party_user_url = 'https://exmail.qq.com/cgi-bin/laddr_biz?t=memtree&limit={limit}&partyid={pid}' \
                              '&action=show_party&sid={sid}'
        self.cookies = dict(
            _ga='xxx',
            _gid='xxx',
            biz_referrer='xxx',
            biz_username='xxx',
            CCSHOW='xxx',
            Hm_lpvt_bdfb0d7298c0c5a5a2475c291ac7aca2='xxx',
            Hm_lvt_bdfb0d7298c0c5a5a2475c291ac7aca2='xxx',
            new_mail_num='xxx',
            qm_flag='xxx',
            qm_sid='xxx',
            qm_sk='xxx',
            qm_ssum='xxx',
            qm_username='xxx',
            qqmail_alias='xxx',
            qylevel='xxx',
            sid='xxx',
            ssl_edition='xxx',
            tinfo='xxx',
            username='xxx',
            logout_page='xxx',
            dm_login_weixin_rem='',
            pgv_pvi='xxx',
            pgv_si='xxx',
            pt2gguin='xxx',
            ptcz='xxx',
            ptui_loginuin='xxx',
            qm_authimgs_id='xxx',
            qm_verifyimagesession='xxx',
            RK='xxx'
        )
        self.all_parties_ids = []  # 所有的通信组id,作为pid使用
        self.root_party = None  # 根通信组
        self.all_parties_info = dict()  # 用于保存所有的通信组信息
        self.limit = 10000  # 单次获取数据量
        self.all_user_info = []  # 用于保存所有的用户信息

    def get_all_ids(self):
        """
        获取所有的通信组的id
        """
        print("获取所有通信组的id...")
        try:
            regexp = r'{id:"(\S*?)", pid:"(\S*?)", name:"(\S*?)", order:"(\S*?)"'
            request = requests.get(self.all_parties_url, cookies=self.cookies)
            request.encoding = request.apparent_encoding
            request.raise_for_status()
            text = request.text

            results = re.findall(regexp, text)

            for p in results:
                self.all_parties_ids.append(p[0])
                party = dict(id=p[0], pid=p[1], name=p[2], order=p[3])
                self.all_parties_info[p[0]] = party

                if p[1] == 0 or p[1] == '0':
                    self.root_party = party
            print("所有通信组id获取完成... ---", '总获取到 {num}'.format(num=len(self.all_parties_ids))
                  + '个id.')
        except None:
            print("获取ids失败!")

    def get_all_user_info(self):
        """
        获取所有的通讯录下的用户信息
        :return:
        """
        print('获取用户数据开始...')
        try:
            regexp = r'{uin:"(\S*?)",pid:"(\S*?)",name:"(\S*?)",alias:"(\S*?)",sex:"(\S*?)",pos:"(\S*?)",' \
                     'tel:"(\S*?)",birth:"(\S*?)",slave_alias:"(\S*?)",department:"(\S*?)",mobile:"(\S*?)"}'

            count = 1
            for pid in self.all_parties_ids:
                url = self.party_user_url.format(sid=self.sid, pid=pid, limit=self.limit)
                print("第{i}条".format(i=count) + ': ' + url)

                request = requests.get(url, cookies=self.cookies)
                request.encoding = request.apparent_encoding
                request.raise_for_status()
                text = request.text
                results = re.findall(regexp, text)

                print('当前爬取链接包含数据数: {0}'.format(len(results)))
                if len(results) == 0:
                    print('当前链接没有数据...')
                    count += 1
                    continue
                for item in results:
                    user = dict(uin=item[0], pid=item[1], name=item[2], alias=item[3], sex=item[4], pos=item[5],
                                tel=item[6], birth=item[7], slave_alias=item[8], department=item[9], mobile=item[10])
                    self.all_user_info.append(user)

                count += 1
            print('获取数据完成... -- 总获取到{num}用户信息数据.'.format(num=len(self.all_user_info)))
        except None:
            print("获取用户内容失败!")

    def run(self):
        self.get_all_ids()
        self.get_all_user_info()
        # 写到文本文件中
        length = len(self.all_user_info)
        with open('all_user_info.txt', 'w', encoding='utf-8') as f:
            f.write('[')
            for i in range(0, length):
                f.write(str(self.all_user_info[i]))
                if i != length - 1:
                    f.write(',')
            f.write(']')


# Driver the program to test the methods above.
if __name__ == "__main__":
    spider = Spider()
    spider.run()
