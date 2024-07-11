import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def filter_type(type):

    while True:
        input_x = input("Please inter which {} you want to analyse: ".format(type))
        cities = ["washington", "new york city", "chicago"]
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', "all"]
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "all"]

        if type == "city":
            date = cities
        elif type == "month":
            date = months
        elif type == "day":
            date = days
        if input_x != "all":
            if input_x not in date and input_x.title() not in date :
                if not input_x.isalpha():
                    print("Just string is allowed.")
                else:
                    print("Invalid {},please try again.".format(type))
            else:
                print("The {} you selected loaded successfully.☻".format(type))
                break
        else:
            print("All of them you selected loaded successfully.☻")
            break
    return input_x

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze•
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = filter_type("city")
    # get user input for month (all, january, february, ... , june)
    month = filter_type("month")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = filter_type("day")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["months"] = df["Start Time"].dt.month
    df["Days"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour
    if month != "all":
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
        month = months.index(month)+1
        df = df[df["months"] == month]
    if day != all:
        df = df[df["Days"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: {}".format(df["months"].mode()[0]))

    # display the most common day of week
    print("The most common day is: {}".format(df["Days"].mode()[0]))

    # display the most common start hour
    print("The most common hour is: {}".format(df["hour"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df["Start Station"].mode()[0])

    # display most commonly used end station
    print(df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    df["Start & End Station"] = df["Start Station"] + " _ " + df["End Station"]
    print(df["Start & End Station"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time in hours is: {}".format(total_travel_time / 3600))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The average travel time in hours is: {}".format(mean_travel_time / 3600))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    if city == 'chicago' or 'new york city':
        print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if city == 'chicago' or 'new york city':
        print("Earliest year of birth is: {}".format(int(df['Birth Year'].min())))
        print("Most recent year of birth is: {}".format(int(df['Birth Year'].max())))
        print("Most common year of birth is: {}".format(int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
