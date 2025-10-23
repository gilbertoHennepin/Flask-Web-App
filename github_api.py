# TODO make requests to github API

import requests
import logging

def get_github_user_info(username):


    # 404 - username not found
    # other errors 
    # success 

    # retrurn a tuple of (data, error)
    # if things work, return (data, None)

    # if things font work theres an error, return (None, error_message)

    try:

        response = requests.get(f'https://api.github.com/users/{username}')
        if response.status_code == 404:
            return None, f'Username {username} not found'
        response.raise_for_status()
    # todo error handling
        response_json = response.json()
        user_info = extract_user_info(response_json)
        return user_info, None
    except Exception as e:
        logging.exception(e)
        return None, 'Error connecting to GitHub API'

def extract_user_data(json_response):
    # TODO extract useful info from github_response
    return {
        'login': json_response.get('login'),
        'name': json_response.get('name'),
        'avatar_url': json_response.get('avatar_url'),
        'home_page': json_response.get('html_url'),
        'repos': json_response.get('public_repos'),
        'bio': json_response.get('bio'),
    }



