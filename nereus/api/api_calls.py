""" https://neuronsensors.app/restApiDocs """
import os

import requests
import json

api_url = 'https://us-central1-neuron2.cloudfunctions.net'
api_key = os.environ.get('NEREUS_API_KEY')


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
        api_key = api_key,
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
        api_key = api_key,
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


def get_sensor_information(
        sensor_id,
        api_key = api_key,
        api_url: str = api_url
    ):
    """ Gets all available info about a specific sensor in the system

    This requires the sensor_id (the api uses the name 'sn'). One way of getting
    this ID is through the get_latest_samples call, which will respond with some
    data from all sensors in the system.

    Returns a dictionary:
    {
        'alias': alias of the sensor,
        'config': {
            'binary': {},
            'calc': [],     # Information about calculation from raw to values
            'digitiser': {} # Info about the digitiser and units
            },
            'max': [],
            'min': [],
            'pv': int,
            'si': []    # Units
        },
        'created': int,
        'description': str,
        'owner': str,
        'regcode': str,
        'tags': [],
        'type': int,
        'userPresence': int,
    }
    """
    Response = requests.post(
        api_url+"/sensorInfo",
        {
            'Content-Type': 'application/json',
            'apiKey': api_key,
            'sn': str(sensor_id)
        }
    )

    if Response.status_code == 200:
        return Response.json()
    else:
        # We did not receive [200], which means _something_ went wrong.
        # The user must themselves try to figure out what the statuscode means
        raise Api_not_200_error(Response)


def get_sensor_samples(
        sensor_id,
        from_time: int,
        to_time: int,
        order: str = "desc",
        api_key = api_key,
        api_url: str = api_url
    ):
    """ Gets samples from a sensor within specified time 

    Args:
        api_key: The "password" to the API
        sensor_id: The ID of the specific sensor, called 'sn' by the root api
        from_time: Start time in epoch timestamp (milliseconds)
        to_time: End time in epoch timestamp (milliseconds)
        order: string - default "desc"
        api_urls. The url to the API, defaults to the value in api_calls.api_url

    Returns: 
        A list of sensor-readings
    
    Raises:
        Api_not_200_error if the status_code is not 200.
    """
    Response = requests.post(
        api_url+"/sensorStream",
        {
            'Content-Type': 'application/json',
            'apiKey': api_key,
            'sn': str(sensor_id),
            'from': int(from_time),
            'to': int(to_time)
        }
    )

    if Response.status_code == 200:
        return Response.json()
    else:
        # We did not receive [200], which means _something_ went wrong.
        # The user must themselves try to figure out what the statuscode means
        raise Api_not_200_error(Response)


def add_sensor():
    raise NotImplementedError("This api-call has not been implemented")


def get_sensor_types():
    Response = requests.post(
        api_url+"/getTypes",
        {
            'Content-Type': 'application/json',
            'apiKey': api_key
        }
    )

    if Response.status_code == 200:
        return Response.json()
    else:
        # We did not receive [200], which means _something_ went wrong.
        # The user must themselves try to figure out what the statuscode means
        raise Api_not_200_error(Response)
