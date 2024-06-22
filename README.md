# Weather-Dataset-Analysis-Project
This project analyzes weather data from a CSV file using Python and the pandas library. It performs various data analysis tasks, such as finding the number of unique wind speed values, counting occurrences of clear weather, and calculating statistical values like mean visibility and standard deviation of pressure.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Project Structure](#project-structure)
4. [Functions and Features](#functions-and-features)
5. [Testing](#testing)
6. [Dependencies](#dependencies)
7. [How to Use](#how-to-use)
8. [Conclusion](#conclusion)

## Introduction
This project aims to analyze weather data using Python and the pandas library. The analysis includes various tasks such as finding unique wind speed values, counting occurrences of clear weather, calculating statistical values like mean visibility and standard deviation of pressure, and more. The project is structured according to course guidelines, with a main function and additional functions for specific data analysis tasks.

## Project Overview
The project uses a CSV file containing weather data as its data source. It loads the data into a pandas DataFrame and performs a series of analyses to extract useful information about the weather conditions recorded in the dataset. The analyses include both simple tasks, such as counting occurrences of specific weather conditions, and more complex tasks, such as calculating statistical values for different weather conditions.

## Project Structure
The project is structured into two main files: `project.py` and `test_project.py`. The `project.py` file contains the main function and additional functions for data analysis tasks. Each function is defined at the same indentation level as the main function, as required by the course guidelines. The `test_project.py` file contains test functions for each of the additional functions in `project.py`, ensuring the correctness of the analysis.

## Functions and Features
- `load_data(file_path)`: Loads the weather data from a CSV file into a pandas DataFrame.
- `unique_wind_speed_values(data)`: Calculates the number of unique wind speed values in the dataset.
- `count_clear_weather(data)`: Counts the occurrences of clear weather in the dataset.
- `count_wind_speed_4(data)`: Counts the occurrences when the wind speed is exactly 4 km/h.
- `count_null_values(data)`: Counts the number of null values in the dataset.
- `rename_weather_column(data)`: Renames the "Weather" column to "Weather Condition" in the DataFrame.
- `mean_visibility(data)`: Calculates the mean visibility in the dataset.
- `std_pressure(data)`: Calculates the standard deviation of the pressure column in the dataset.
- `variance_relative_humidity(data)`: Calculates the variance of the relative humidity column in the dataset.
- `count_snow_instances(data)`: Counts the occurrences of snow in the dataset.
- `count_wind_above_24_visibility_25(data)`: Counts the occurrences when the wind speed is above 24 km/h and visibility is 25 km.
- `mean_values_per_weather_condition(data)`: Calculates the mean values of each column grouped by weather condition.
- `min_values_per_weather_condition(data)`: Calculates the minimum values of each column grouped by weather condition.
- `max_values_per_weather_condition(data)`: Calculates the maximum values of each column grouped by weather condition.
- `count_fog_instances(data)`: Counts the occurrences of fog in the dataset.
- `count_clear_weather_or_visibility_above_40(data)`: Counts the occurrences when the weather is clear or visibility is above 40 km.
- `count_complex_condition(data)`: Counts the occurrences when the weather is clear and relative humidity is greater than 50, or visibility is above 40 km.

## Testing
The project uses the pytest framework for testing. Each function in `project.py` has a corresponding test function in `test_project.py` that tests its functionality. The tests cover various scenarios to ensure the correctness of the analysis functions.

## Dependencies
The project requires the following dependencies, which are listed in the `requirements.txt` file:
- pandas
- pytest

These dependencies can be installed using `pip install -r requirements.txt`.

## How to Use
To use the project, follow these steps:
1. Clone the project repository to your local machine.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the `project.py` file to perform the data analysis.
4. Run the `test_project.py` file to run the tests and ensure the correctness of the analysis functions.

## Conclusion
The Weather Data Analysis Project provides a comprehensive analysis of weather data using Python and the pandas library. It demonstrates various data analysis techniques and provides a structured approach to analyzing and extracting useful information from weather datasets. The project's adherence to course guidelines and use of testing ensures the correctness and reliability of the analysis functions.

For a more detailed demonstration, please refer to the video demo linked above.

