import pytest
import pandas as pd
from project import (
    load_data, unique_wind_speed_values, count_clear_weather, count_wind_speed_4,
    count_null_values, rename_weather_column, mean_visibility, std_pressure,
    variance_relative_humidity, count_snow_instances, count_wind_above_24_visibility_25,
    mean_values_per_weather_condition, min_values_per_weather_condition, 
    max_values_per_weather_condition, count_fog_instances,
    count_clear_weather_or_visibility_above_40, count_complex_condition
)

@pytest.fixture
def data():
    return pd.DataFrame({
        'Weather': ['Clear', 'Rain', 'Clear', 'Snow', 'Fog'],
        'Wind Speed_km/h': [4, 5, 4, 7, 8],
        'Visibility_km': [40, 30, 50, 25, 20],
        'Press_kPa': [101.2, 100.8, 101.5, 100.0, 99.5],
        'Rel Hum_%': [50, 60, 55, 80, 85]
    })

def test_unique_wind_speed_values(data):
    assert unique_wind_speed_values(data) == 4

def test_count_clear_weather(data):
    assert count_clear_weather(data) == 2

def test_count_wind_speed_4(data):
    assert count_wind_speed_4(data) == 2

def test_count_null_values(data):
    assert count_null_values(data) == 0

def test_rename_weather_column(data):
    rename_weather_column(data)
    assert 'Weather Condition' in data.columns

