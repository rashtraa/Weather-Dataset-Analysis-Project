import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def unique_wind_speed_values(data):
    return data['Wind Speed_km/h'].nunique()

def count_clear_weather(data):
    return data[data['Weather'] == 'Clear'].shape[0]

def count_wind_speed_4(data):
    return data[data['Wind Speed_km/h'] == 4].shape[0]

def count_null_values(data):
    return data.isnull().sum().sum()

def rename_weather_column(data):
    data.rename(columns={"Weather": "Weather Condition"}, inplace=True)

def mean_visibility(data):
    return data['Visibility_km'].mean()

def std_pressure(data):
    return data['Press_kPa'].std()

def variance_relative_humidity(data):
    return data['Rel Hum_%'].var()

def count_snow_instances(data):
    return data[data['Weather Condition'] == 'Snow'].shape[0]

def count_wind_above_24_visibility_25(data):
    return data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)].shape[0]

def mean_values_per_weather_condition(data):
    numeric_columns = data.select_dtypes(include='number').columns
    return data.groupby('Weather Condition')[numeric_columns].mean()

def min_values_per_weather_condition(data):
    numeric_columns = data.select_dtypes(include='number').columns
    return data.groupby('Weather Condition')[numeric_columns].min()

def max_values_per_weather_condition(data):
    numeric_columns = data.select_dtypes(include='number').columns
    return data.groupby('Weather Condition')[numeric_columns].max()

def count_fog_instances(data):
    return data[data['Weather Condition'] == 'Fog'].shape[0]

def count_clear_weather_or_visibility_above_40(data):
    return data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)].shape[0]

def count_complex_condition(data):
    return data[((data['Weather Condition'] == "Clear") & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)].shape[0]

def main():
    file_path = r"X:\data analytics project\Project 1 Weather Dataset\file.csv"
    data = load_data(file_path)
    
    print(f"Number of unique wind speed values: {unique_wind_speed_values(data)}")
    print(f"Number of times when the weather is exactly clear: {count_clear_weather(data)}")
    print(f"Number of times when the wind speed is exactly equals to 4 km/h: {count_wind_speed_4(data)}")
    print(f"Number of null values in the data: {count_null_values(data)}")

    rename_weather_column(data)
    print("The column Weather has been renamed to Weather Condition")
    print(data.head(1))

    print(f"Mean Visibility is equal to: {mean_visibility(data)}")
    print(f"Standard Deviation of Pressure column is: {std_pressure(data)}")
    print(f"Variance of Relative Humidity is equal to: {variance_relative_humidity(data)}")
    print(f"Number of instances Snow was recorded: {count_snow_instances(data)}")
    print(f"Instances when Wind Speed is above 24 and Visibility is 25: {count_wind_above_24_visibility_25(data)}")
    
    print("Mean Values:  ")
    print(mean_values_per_weather_condition(data))

    print("Minimum Values:  ")
    print(min_values_per_weather_condition(data))
    print("Maximum Values:  ")
    print(max_values_per_weather_condition(data))
    
    print(f'All the records where Weather Condition is fog: {count_fog_instances(data)}')
    print(f'All instances where "Weather is clear" or "Visibility is above 40": {count_clear_weather_or_visibility_above_40(data)}')
    print(f'1) All instances when Weather is Clear and Relative Humidity is greater than 50 OR 2) Visibility is above 40: {count_complex_condition(data)}')

if __name__ == "__main__":
    main()
