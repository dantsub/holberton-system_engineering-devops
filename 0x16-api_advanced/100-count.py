#!/usr/bin/python3
"""A file to make a query to an endpoint
"""
from requests import request


def count_words(subreddit, word_list, after="", count={}, ini=0, dup={}):
    """A recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not)
    """
    if ini == 0:
        count = {k: 0 for k in word_list}
        dup = {}
        for word in word_list:
            if word not in dup:
                dup[word] = 0
            dup[word] += 1

    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        top = response['data']['children']
        _after = response['data']['after']
        for item in top:
            for word in count:
                count[word] += item['data']['title'].lower(
                    ).split(' ').count(word.lower())
        if _after is not None:
            count_words(subreddit, word_list, _after, count, 1, dup)
        else:
            sorty = sorted(count.items(), key=lambda r: r[::-1])
            topics = sorted(sorty, key=lambda kv: kv[1], reverse=True)
            for name, num in topics:
                num *= dup[name]
                if num != 0:
                    print('{}: {}'.format(name.lower(), num))
    except Exception:
        return None
