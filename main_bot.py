#!/bin/env python
# coding:utf-8

from wxpy import *
import platform
from random import randrange

'''
微信登录二维码显示终端
初始化机器人微信
加载cache,无需重新扫码
保存历史记录1000000
'''

console_qr = (False if platform.system() == 'Window' else True)
og_bot = Bot(cache_path=True, console_qr=console_qr)
og_bot.enable_puid('wxpy_puid.pkl')
og_bot.messages.max_history = 1000000

'''
定义关键字
机器微信登录后update所有群组
获取所有关键群组（OG）群
'''
key_words = "OG"
og_bot.groups(update=False, contact_only=False)
key_groups=og_bot.groups().search(key_words)


@og_bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    if '客户' in msg.text.lower():
        new_friend = msg.card.accept()
        new_friend.send('你好，我是小志，回复口令进入群聊天哦！')

'''
微信WEB API 被封，暂时无法调用对应接口
'''
'''
@og_bot.register(msg_types=TEXT)
def auto_firend_into_groups(msg):
    if "OG" in msg.text.lower():
        if len(key_groups) > 0:
            lengroup = len(key_groups)
            print(lengroup)
            for i in range(0, len(key_groups)):
               if user in key_groups[i]:
                    str = "您已经加入了 {} [微笑]".format(key_groups[i].nick_name)
                    user.send(str)
                    return
            if len(key_groups) == 1:
                target_group = key_groups[0]
                print(1)
            else:
                index = randrange(len(key_groups))
                target_group = key_groups[index]
                print(2)
        try:
            target_group.add_members(user, use_invitation=True)
        except:
            user.send("邀请错误！机器人邀请好友进群已达当日限制。请您明日再试")
    else:
        user.send("要不要换个关键字？")
'''


'''
群里被@后
调用图灵机器人自助聊天
'''

@og_bot.register(Group, TEXT)
def auto_reply(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        tuling = Tuling(api_key='ee5a12ca7e1d43b0aef969a1605f9208')
        tuling.do_reply(msg)



bug_group = ensure_one(og_bot.groups().search('XXXXX'))
bug_user = ensure_one(bug_group.search('XXXXXX'))
@og_bot.register(bug_group)
def forward_bug_user_message(msg):
    if msg.member == bug_user:
        if "bug" in msg.text.lower():
            msg.forward(og_bot.file_helper, prefix='bug内容:')


embed(banner='欢迎使用小志，给个好评哦！')
