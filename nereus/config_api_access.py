""" Script to help the user to set the API key and URL """

import os

def get_api_url_and_key():
    api_url = os.environ.get('NEREUS_API_URL')
    api_key = os.environ.get('NEREUS_API_KEY')
    return api_url, api_key


def set_api_url(api_url, verbose = False):
    os.environ['NEREUS_API_URL'] = api_url
    if verbose:
        print("Api_url set to: {}".format(api_url))


def set_api_key(api_key, verbose = False):
    os.environ['NEREUS_API_KEY'] = api_key
    if verbose:
        print("Api_key set to: {}".format(api_key))


def user_config_api_url_and_key():
    api_url, api_key = get_api_url_and_key()

    # ------------ CONFIG API URL -------------
    # If no url is present, then set the default one which probably is the correct one
    if api_url == None:
        api_url = 'https://us-central1-neuron2.cloudfunctions.net'

    print("Current api_url: {}".format(api_url))
    new_api_url = input("Type new URL (type nothing to keep curent url): ")

    # Only use the new_api_url if there is actually something there
    if new_api_url != '':
        api_url = new_api_url

    set_api_url(api_url, verbose=True)

    # -------------- CONFIG API KEY ---------------
    print("Current api_key: {}".format(api_key))
    new_api_key = input("Type new KEY (type nothing to keep curent key): ")

    # Only use the new_api_key if there is actually something there
    if new_api_key != '':
        api_key = new_api_key

    set_api_key(api_key, verbose=True)

    return api_url, api_key


if __name__ == '__main__':
    user_config_api_url_and_key()