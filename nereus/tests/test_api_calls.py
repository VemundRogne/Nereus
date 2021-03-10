import pytest

import nereus.api.api_calls as api_calls


def test_get_system_information():
    result = api_calls.get_system_information()
    assert result


def test_get_latest_samples():
    pytest.skip("Test not implemented")

def test_get_sensor_information():
    pytest.skip("Test not implemented")

def test_get_sensor_samples():
    pytest.skip("Test not implemented")

def test_add_sensor():
    pytest.skip("Lower-level function not implemented")

def test_get_sensor_types():
    pytest.skip("Test not implemented")