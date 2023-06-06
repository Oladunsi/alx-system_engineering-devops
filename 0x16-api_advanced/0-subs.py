#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
   @author: Oke Oladunsi Samuel

   Created on Tue Jun 06 13:46:22 2023
"""
from json import loads
from requests import get


def number_of_subscribers(subreddit):
    """ This a function that returns the number of subscribers
    (not non active users, total subscribers) for a given subreddit.

    Returns:
           0 if subreddit is invalid or no result
           else
           (int) num of subcribers in subreddit if valid
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
            Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    response = get(url, headers=headers)
    reddits = response.json()
    try:
        subs = reddits.get('data').get('subscribers')
        # print(reddits.get('data'))
        return int(subs)
    except Exception:
        return 0
