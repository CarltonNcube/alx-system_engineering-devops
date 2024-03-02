#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API
    and prints the titles of the first 10 hot posts
    for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Custom"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Extract the list of posts from the JSON response
        data = response.json().get("data", {}).get("children", [])

        # Print the titles of the first 10 posts
        for post in data:
            print(post.get("data", {}).get("title"))
    else:
        # Print None if the subreddit is not valid or there is an error
        print(None)

if __name__ == "__main__":
    top_ten(sys.argv[1])
