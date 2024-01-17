#!/usr/bin/python3
"""
2-recurse
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "Custom"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data", {})
        children = data.get("children", [])
        after = data.get("after")

        if not children:
            return hot_list

        hot_list.extend([post.get("data", {}).get("title") for post in children])

        return recurse(subreddit, hot_list, after)
    else:
        return None
