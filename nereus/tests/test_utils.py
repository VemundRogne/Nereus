import nereus

import pandas as pd

import matplotlib.pyplot as plt

def test_find_sensors_in_system():
    sensors = nereus.utils.find_sensors_in_system()
    print(sensors)


def test_download_sensor_samples():
    # Download 'Water pressure in well', a few weeks of data
    sensors = nereus.utils.find_sensors_in_system()

    samples = [
        nereus.utils.download_sensor_samples(
            sn,
            1614600055000,
            1615982455000,
            name = sensors[sn]['alias']
        )
        for sn in sensors.keys()
    ]
    print(samples)

    full_df = pd.concat(samples, axis=1)
    full_df.fillna(inplace=True, method='ffill')
    print(full_df)
    full_df.plot(subplots=True, kind='line')
    plt.show()