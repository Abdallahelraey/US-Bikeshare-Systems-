# US Bikeshare Data Analysis Project

## Overview

This project is part of the Udacity Data Analyst Nanodegree and focuses on exploring bikeshare data for three major cities in the United States: Chicago, New York City, and Washington. The project uses Python to compute descriptive statistics and create an interactive terminal-based experience for analyzing the data.

## Dataset

The data files for the three cities are:
- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

These datasets contain information about individual rides made in a bike-sharing system.

## Files

- `bikeshare.py`: The main Python script that runs the analysis.

## How to Run

1. Make sure you have the required CSV files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) in the same directory as `bikeshare.py`.
2. Run the script using Python:

   ```bash
   python bikeshare.py
   ```

3. Follow the prompts to select the city, month, and day for which you want to analyze the data.

## Functionality

The script provides the following functionalities:

1. **User Input Filtering:**
    - Asks the user to specify a city, month, and day to analyze.
    - Handles invalid inputs and allows re-entry.

2. **Data Loading and Filtering:**
    - Loads data for the specified city.
    - Filters the data by month and day if applicable.

3. **Statistics Calculation:**
    - **Time Stats:** Displays statistics on the most frequent times of travel.
    - **Station Stats:** Displays statistics on the most popular stations and trips.
    - **Trip Duration Stats:** Displays statistics on total and average trip duration.
    - **User Stats:** Displays statistics on bikeshare users.

## Example Usage

After running the script, you will be prompted to input the city, month, and day for analysis. Based on the input, the script will calculate and display the following statistics:

1. The most common month, day, and start hour for bike rides.
2. The most commonly used start and end stations, as well as the most frequent combination of start and end stations.
3. Total and average trip durations.
4. Counts of user types, and for Chicago and New York City, counts of gender and birth years.

## Requirements

- Python 3.x
- pandas
- numpy

You can install the required libraries using:

```bash
pip install pandas numpy
```

## Project Structure

```plaintext
.
├── bikeshare.py
├── chicago.csv
├── new_york_city.csv
└── washington.csv
```

## Acknowledgements

This project is part of the Udacity Data Analyst Nanodegree program.
