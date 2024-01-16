#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    - None
    """
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

        # Print titles of the first 10 posts
        for i, post in enumerate(posts_data[:10], 1):
            print(f"{i}. {post['data']['title']}")
    elif response.status_code == 302:
        # This may happen if the subreddit is invalid (redirect to search results)
        print("None")
    else:
        # Other errors, print None
        print("None")

if __name__ == "__main__":
