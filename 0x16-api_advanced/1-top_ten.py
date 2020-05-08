#!/usr/bin/python3
"""Module top ten
Print the titles of the first 10 hot posts listed for a given subreddit.
"""
from requests import *


def top_ten(subreddit):
    """ Print the titles of the first 10 hot posts """
    # ===================== Request ===========================
    api = 'https://api.reddit.com/r/{}/hot?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Holbi'}
    response = get(api, headers=headers).json()
    # =========================================================
    try:
        [print(top['data']['title']) for top in response['data']['children']]
    except Exception:
        print(None)
