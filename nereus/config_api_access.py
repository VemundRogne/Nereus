""" Script to help the user to set the API key and URL """

import os

## ------------ HARDCODE API KEY AND URL HERE ----------------------
# This is an option to hardcode the api_url and api_key

# Type the URL and key inside the "", for example:
# api_url = "https://eit_neuronsensors_api.no/"
# api_key = "12354863faefs4685"

hardcoded_api_url = ""
hardcoded_api_key = ""
## ----------- END HARDCODE API KEY AND URL HERE -------------------


def get_api_url_and_key():
    """ Gets the configured API-url and key

    Uses the hardcoded url and key if they have been configured in config_api_acces file, if that
    has not been configured try to get ones from the environment variables.
    
    Returns api_url, api_key
    """
    if hardcoded_api_url != "":
        api_url = hardcoded_api_url
    else:
        api_url = os.environ.get('NEREUS_API_URL')

    if hardcoded_api_key != "":
        api_key = hardcoded_api_key
    else:
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