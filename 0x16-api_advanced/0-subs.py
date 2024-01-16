#!/usr/bin/python3

"""
Module Name: reddit_api
Description: This module interacts with the Reddit API to get the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: Number of subscribers if the subreddit is valid, 0 otherwise.
    """
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        subreddit_info = response.json()

        # Extract and return the number of subscribers
        return subreddit_info['data']['subscribers']
    elif response.status_code == 302:
        # This may happen if the subreddit is invalid (redirect to search results)
        return 0
    else:
        # Other errors, return 0
        return 0

if __name__ == "__main__":
