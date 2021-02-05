#!/usr/bin/python3
'''
queries the Reddit API and returns the number of
subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
'''
from requests import get


def number_of_subscribers(subreddit):
    '''check number of subscribers'''
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    response = get(url, headers=headers)
    info = response.json().get('data').get('subscribers')
    if info:
        return info
    return 0
