""" Some general nice utils """

import nereus
import nereus.api.api_calls as api_calls

def find_sensors_in_system():
    """ Create a dict with info about every sensor in the system

    Uses the api-call "latestSamples" to get info from all available sensors.
    Populates the dictionary with:
        sensorID: {
            "alias": sensor-alias,
            "si": SI-units in values,
            "node": node,
            "type": type 
        }
    
    """
    sensors = {}
    result = api_calls.get_latest_samples()

    for element in result:
        if "alias" in element:
            sn = int(element['sn'])

            if sn not in sensors:
                sensors[sn] = {}

            sensors[sn]['alias'] = element['alias'].strip()
            sensors[sn]['si'] = element['si']
            sensors[sn]['node'] = element['node']
            sensors[sn]['type'] = element['type']

    return sensors