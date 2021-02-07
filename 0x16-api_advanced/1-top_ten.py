#!/usr/bin/python3
'''check the host post'''


def top_ten(subreddit):
    from requests import get
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'my-app/0.0.1'}
    info = get(api_url, headers=headers)
    if info.status_code == 200:
        top10 = info.json().get('data').get('children')[0:10]
        for item in top10:
            print(item.get('data').get('title'))
    else:
        print(None)
