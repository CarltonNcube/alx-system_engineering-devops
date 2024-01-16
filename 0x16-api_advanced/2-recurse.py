#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieve the titles of all hot articles for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): A list to store the titles of hot articles.

    Returns:
    - list: A list containing the titles of all hot articles for the given subreddit, or None if invalid.
    """
    # Base case: if hot_list reaches 100 or more titles, stop recursion
    if len(hot_list) >= 100:
        return hot_list

    # Reddit API endpoint for hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        posts_data = response.json()['data']['children']

        # Append titles to hot_list
        for post in posts_data:
            hot_list.append(post['data']['title'])

        # Check if there are more pages (pagination) and make a recursive call
        if response.json()['data']['after']:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    elif response.status_code == 302:
        # This may happen if the subreddit is invalid (redirect to search results)
        return None
    else:
        # Other errors, return None
        return None

if __name__ == "__main__":
