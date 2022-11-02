# -*- coding: utf-8 -*-
# @File     : message.py
# @Time     : 2021/10/17 19:24
# @Author   : Jckling

import os
import requests

from V2EX import v2ex_checkin

# info
BARK_TOKEN = os.environ.get("BARK_TOKEN")

if __name__ == '__main__':
    content_lst = []
    if os.environ.get("V2EX_COOKIES"):
        content_lst.append(f"「V2EX」\n{v2ex_checkin.main()}")

    content = "".join(content_lst)

    # use bark
    if BARK_TOKEN:
        requests.get(f"https://api.day.app/{BARK_TOKEN}/{content}")
    else:
        print(content)
