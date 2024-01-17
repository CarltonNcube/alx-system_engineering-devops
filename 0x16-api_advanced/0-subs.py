#!/usr/bin/python3
"""
Queries the Reddit API and retrieves the total number of subscribers
for a specified subreddit. If the subreddit is invalid, returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}

    response = requests.get(url, headers=headers)
    return (
    response.json().get("data", {}).get("subscribers", 0)
    if response.status_code == 200
    else 0
)
