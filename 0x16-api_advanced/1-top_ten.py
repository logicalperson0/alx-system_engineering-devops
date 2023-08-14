#!/usr/bin/python3
"""
function that queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed for a given subreddit"""
    if subreddit is None:
        return 0

    # from https://www.reddit.com/dev/api/#GET_r_{subreddit}_about!!!

    urlReddit = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    limits = {'limit': 10}

    datas = requests.get(urlReddit, params=limits).json()

    if 'data' not in datas:
        return 0

    data_subs = datas['data']['children']

    if data_subs is None:
        print(None)

    else:
        for pop in data_subs:
            # in children there is data, then within data there is title!!
            print(pop['data']['title'])
