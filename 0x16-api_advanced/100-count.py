#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None):
    """
    Recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints
    a sorted count of given keywords.
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
            return

        titles = [post.get("data", {}).get("title", "").lower() for post in children]

        for word in word_list:
            count = sum(title.count(word.lower()) for title in titles)
            if count > 0:
                print(f"{word.lower()}: {count}")

        return count_words(subreddit, word_list, after)
    else:
        return None
