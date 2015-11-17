# -*- coding: utf-8 -*-

import sys
import weibo
import webbrowser

APP_KEY = '1037696311'
APP_SECRET = '1d229c06e0b883b1970c0d3173a4d050'

MY_APP_SECRET = APP_SECRET
REDIRECT_URL = 'https://about.me/tanvict'

local_api = weibo.APIClient(APP_KEY, MY_APP_SECRET)
authorize_url = local_api.get_authorize_url(REDIRECT_URL)

print(authorize_url)

# Testing the url
# webbrowser.open_new(authorize_url)

code = raw_input()

local_request = local_api.request_access_token(code, REDIRECT_URL)
access_token = local_request.access_token
expires_in = local_request.expires_in

local_api.set_access_token(access_token, expires_in)

# testing the public_time_line
statuses = local_api.statuses__public_timeline()['statuses']
length = len(statuses)

for i in range(0, length):
    print u'昵称：' + statuses[i]['user']['screen_name']
    print u'简介：' + statuses[i]['user']['description']
    print u'位置：' + statuses[i]['user']['location']
    print u'微博：' + statuses[i]['text']
    print '\n'

# print(local_api.statuses__public_timeline())

# print('user_timeline')
# res = local_api.statuses.user_timeline.get(uid=1700022427)

# print the text from the result
# for subres in res.statuses:
#    print ('[%s]' % subres.text)

# print the friends
# print('friendships')
# friends=local_api.friendships.friends(uid=1700022427, count=20)
# print friends
