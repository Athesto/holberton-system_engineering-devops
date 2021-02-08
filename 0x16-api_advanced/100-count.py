#!/usr/bin/python3
'''advanced task'''


def count_words(subreddit, word_list, hot_list=[], page=None):
    '''count words'''
    from requests import get
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    data = {
        "headers": {
            "user-agent": "App-1.0"
        },
        "params": {
            "after": page
        }
    }
    response = get(api_url, **data)
    if response.status_code == 200:
        for item in response.json().get('data').get('children'):
            title = item.get('data').get('title')
            hot_list.append(title)

        after = response.json().get('data').get('after')
        if after is not None:
            return count_words(subreddit, word_list, hot_list, after)
        else:
            low_list = []
            multiply = []
            uniq_list = []
            for word in word_list:
                low_list.append(word.lower())
            for word in low_list:
                if word not in uniq_list:
                    uniq_list.append(word)
                    multiply.append(low_list.count(word))

            n = len(uniq_list)
            quantity = [None] * n

            for i in range(n):
                number = 0
                for title in hot_list:
                    number += title.lower().count(uniq_list[i])
                quantity[i] = number * multiply[i]

            times, word = zip(*sorted(zip(quantity, uniq_list), reverse=True))

            for i in range(n):
                if times[i]:
                    print("{}: {}".format(word[i], times[i]))
            return hot_list
    else:
        return None
