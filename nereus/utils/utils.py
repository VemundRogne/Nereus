""" Some general nice utils """

import nereus
import nereus.api.api_calls as api_calls
import pandas as pd

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


def download_sensor_samples(
        sn,
        from_time,
        to_time,
        name:str = "value"
    ):
    """ Download all sensor samples from a sensor """
    rawdata = nereus.api_calls.get_sensor_samples(sn, from_time, to_time)
    print("rawdata[0]", rawdata[0])

    timestamps = [data['time'] for data in rawdata]

    # Extract all values from the rawdata
    values = [data['values'] for data in rawdata]

    # Convert from [[val1, val2], [val1, val2]] to [[val1, val1], [val2, val2]]
    values = [[val[i] for val in values] for i in range(len(values[0]))]

    # Convert to a series
    si = rawdata[0]['si']   # SI-unit to be used in the series names
    values = [pd.Series(val, index=timestamps, name=name+" [{}]".format(si[i])) for i, val in enumerate(values)]

    # Convert the series into dataframes
    values = [pd.DataFrame(val) for val in values]

    # Concatenate the dataframes along the column axis to merge them together
    values = pd.concat(values, axis=1)

    return values