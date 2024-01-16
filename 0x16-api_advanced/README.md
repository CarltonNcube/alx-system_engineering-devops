Project 0x16. API Advanced
Project Description
This project focuses on interacting with the Reddit API to perform various tasks related to subreddit information retrieval. The tasks involve querying the API to obtain the number of subscribers for a given subreddit, printing the titles of the top 10 hot posts, recursively fetching all hot article titles, and counting occurrences of specified keywords in the titles.

Tasks
0. How many subs? (Mandatory)
Write a function number_of_subscribers(subreddit) that queries the Reddit API and returns the number of subscribers (total subscribers) for a given subreddit. If the subreddit is invalid, the function should return 0.

Requirements:

Prototype: def number_of_subscribers(subreddit)
If not a valid subreddit, return 0.
Ensure that you are not following redirects when handling invalid subreddits.
1. Top Ten (Mandatory)
Write a function top_ten(subreddit) that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:

Prototype: def top_ten(subreddit)
If not a valid subreddit, print None.
Ensure that you are not following redirects when handling invalid subreddits.
2. Recurse it! (Mandatory)
Write a recursive function recurse(subreddit, hot_list=[]) that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Requirements:

Prototype: def recurse(subreddit, hot_list=[])
If not a valid subreddit, return None.
Ensure that you are not following redirects when handling invalid subreddits.
Use recursion for fetching results.
3. Count it! (Advanced)
Write a recursive function count_words(subreddit, word_list) that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces).

Requirements:

Prototype: def count_words(subreddit, word_list)
If word_list contains the same word (case-insensitive), the final count should be the sum of each duplicate.
Results should be printed in descending order by count and alphabetically if counts are the same.
Words with no matches should be skipped and not printed.
Ensure that you are not following redirects when handling invalid subreddits.
Use recursion for fetching results.
