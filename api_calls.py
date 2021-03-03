""" https://neuronsensors.app/restApiDocs """
import requests
import json

api_url = 'https://us-central1-neuron2.cloudfunctions.net'
api_key = ''


class Api_not_200_error(Exception):
    """ This exception is raised whenever a requests.Reponse is not OK (200)

    The error can be one of many things, some simple things may be:
     - Wrong api_key
     - Wrong api_url
     - We do not have access to the server
    """
    def __init__(
        self,
        Response: requests.Response,
    ):
        self.Response = Response
        self.message = ("Error: Api returned statuscode [{}],"
            "look up the statuscode to get more information ({})").format(
            self.Response.status_code,
            "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes"
        )
        super().__init__(self.message)


def get_system_information(
        api_key,
        api_url: str = api_url
    ):
    """ Get some info about the system

    The information is mostly metadata about the system itself

    Returns a dict:
    {
        'admin': list of system-administrators,
        'description': the description of the system,
        'invoiceAddress': invoiceAddress,
        'name': system-name,
        'predefinedEventTags': ,
        'tags': [],
        'users': list of the users with access to the system
    }
    """
    Response = requests.post(
        api_url+"/systemInfo",
        {'Content-Type': 'application/json', 'apiKey': api_key}
    )

    if Response.status_code == 200:
        return Response.json()
    else:
        # We did not receive [200], which means _something_ went wrong.
        # The user must themselves try to figure out what the statuscode means
        raise Api_not_200_error(Response)


def get_latest_samples(
        api_key,
        api_url: str = api_url
    ):
    """ Gets latest samples from all sensors in a system

    This info comes in the form of a list of dictionaries, one dict per sensor:
    [
        {
            'added': dict{
                '_nanoseconds': int,
                '_seconds': int
            },
            'alias': str,       # A name given to the sensor
            'gatewayImei': str,
            'node': str,
            'pv': int,
            'rawValues': list,  # Raw values from the sensors
            'rssi': ,
            'si': list,         # Units in the SI-system
            'sn': str,          # SENSOR-ID
            'status': statuscode,
            'time': int,
            'type': int,
            'values': list      # Converted values (in the units given in si)
        },
        {
        },
    ]
    """
    Response = requests.post(
        api_url+"/latestSamples",
        {'Content-Type': 'application/json', 'apiKey': api_key}
    )

    if Response.status_code == 200:
        return Response.json()
    else:
        # We did not receive [200], which means _something_ went wrong.
        # The user must themselves try to figure out what the statuscode means
        raise Api_not_200_error(Response)


def get_sensor_information():
    pass

def get_sensor_samples():
    pass

def add_sensor():
    pass

def get_sensor_types():
    pass