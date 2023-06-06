#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
   @author: Oke Oladunsi Samuel

   Created on Tue Jun 06 13:46:22 2023
"""
from json import loads
from requests import get


def top_ten(subreddit):
    """ This a function that returns the top 10 hottest
        topics for a given subreddit.

    Returns:
           None if subreddit is invalid or no result
           else
           ten of most discussed topics in the subreddit if valid
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
            Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    response = get(url, headers=headers, allow_redirects=False)
    reddits = response.json()
    try:
        hottest = reddits.get('data').get('children')
        for topic in hottest[:10]:
            print(topic.get('data').get('title'))
    except Exception:
        print('None')
