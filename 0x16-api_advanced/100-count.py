#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, results=None):
    """
    Recursively count occurrences of keywords in the titles of hot articles for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.
    - word_list (list): A list of keywords to count.
    - results (dict): A dictionary to store the counts of each keyword.

    Returns:
    - None
    """
    # Initialize the results dictionary in the first call
    if results is None:
        results = {}

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

        # Iterate through the titles of hot articles
        for post in posts_data:
            title = post['data']['title'].lower()

            # Check each keyword in the word_list
            for keyword in word_list:
                keyword = keyword.lower()

                # Check if the keyword is in the title
                if keyword in title:
                    # Update the count in the results dictionary
                    results[keyword] = results.get(keyword, 0) + title.count(keyword)

        # Check if there are more pages (pagination) and make a recursive call
        if response.json()['data']['after']:
            return count_words(subreddit, word_list, results)
        else:
            # Print the results in descending order by count and ascending order alphabetically
            sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))

            for keyword, count in sorted_results:
                print(f"{keyword}: {count}")
    elif response.status_code == 302:
        # This may happen if the subreddit is invalid (redirect to search results)
        print("None")
    else:
        # Other errors, print nothing
        pass

if __name__ == "__main__":
