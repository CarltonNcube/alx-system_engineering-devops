#!/usr/bin/python3
"""Exporting csv files"""
import requests

def number_of_subscribers(subreddit):
    """Read Reddit API and return the number of subscribers"""
    username = 'Code_Break4560'
    password = '#Gombedza101'
    user_pass_dict = {
        'user': username,
        'passwd': password,
        'api_type': 'json'
    }
    headers = {
        'user-agent': 'personal use script by Code_Break4560/1.0'
    }
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    client = requests.session()
    client.headers = headers
    
    r = client.get(url, allow_redirects=False, auth=(username, password))
    
    if r.status_code == 200:
        return r.json()["data"]["subscribers"]
    else:
        return 0

if __name__ == "__main__":
