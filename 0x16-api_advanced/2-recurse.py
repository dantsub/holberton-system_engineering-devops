#!/usr/bin/python3
"""Module recurse
Returns a list containing the titles
of all hot articles for a given subreddit.
"""
from requests import *


def recurse(subreddit, hot_list=[], after=""):
    """ Function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should
    return None.
    """
    # ===================== Request ===========================
    api = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    headers = {'User-Agent': 'Holbi'}
    response = get(api, headers=headers).json()
    # =========================================================
    try:
        # ======== add hot posts to hot_list ========
        for top in response.get('data')['children']:
            hot_list.append(top['data']['title'])
        # ===========================================
        # ============ It calls itself if after exists =============
        if response['data']['after'] is not None:
            recurse(subreddit, hot_list, response['data']['after'])
        # ==========================================================
        return hot_list  # return list
    except Exception:
        return None
