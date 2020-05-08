#!/usr/bin/python3
""" Module subs
Return number of subscribers according to subreddit param
"""
from requests import *


def number_of_subscribers(subreddit):
    """ Return number of subscribers """
    # ===================== Request ===========================
    api = 'https://api.reddit.com/r/{}/about'.format(subreddit)
    headers = {'User-Agent': 'Holbi'}
    response = get(api, headers=headers).json()
    # =========================================================
    # Attempt to return number of subscribers
    try:
        return response.get('data')['subscribers']
    except Exception:
        return 0
