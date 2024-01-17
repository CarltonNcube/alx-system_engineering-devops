#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API
    and prints the titles of the first 10 hot posts
    for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Custom"}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        for post in data:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
