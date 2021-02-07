#!/usr/bin/python3
'''moudule with recursion'''


def recurse(subreddit, hot_list=[], page=None):
    '''requests with recurtion'''
    from requests import get

    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    data = {
        "headers": {
            "user-agent": "my-App",
        },
        "params": {
            "after": page
        }
    }

    response = get(api_url, **data)
    if response.status_code == 200:
        info = response.json()
        after = info.get('data').get('after')
        for data in info.get('data').get('children'):
            hot_list.append(data)
        if after is not None:
            return recurse(subreddit, hot_list, page=after)
        else:
            return hot_list
    else:
        return None
