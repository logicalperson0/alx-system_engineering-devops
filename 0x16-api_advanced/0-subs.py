#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers
    (not active users, total subscribers) for a given subreddit"""
    if subreddit is None:
        return 0

    urlReddit = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    datas = requests.get(urlReddit).json()

    if 'data' not in datas:
        return 0

    data_subs = datas['data']['subscribers']

    return (data_subs)
