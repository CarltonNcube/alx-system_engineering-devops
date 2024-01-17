#!/usr/bin/python3
"""
Queries the Reddit API and retrieves the total number of subscribers
for a specified subreddit. If the subreddit is invalid, returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}
    reddit_username = 'Code_Break4560'
    reddit_password = '#Gombedza101'

    response = requests.get(
        url,
        headers=headers,
        auth=(reddit_username, reddit_password)
    )

    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)

    print(f"Unexpected status code: {response.status_code}")
    return 0

if __name__ == "__main__":
