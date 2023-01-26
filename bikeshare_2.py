import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('=' * 40)

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("choose city from this options ... chicago, new york city or washington.\n")

    while city not in CITY_DATA.keys():
        print("Please choose a valid city, you should choose from chicago, new york city or washington\n")
        city = input()
        if city not in CITY_DATA.keys():
            print("Please check your inputs")
    print("You choose " + city.title() + " as your city\n")

    # get user input for month (all, january, february, ... , june)
    month = input("choose month from this options ... all, january, february, ... june.\n")
    month_data = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    while month not in month_data:
        print("Please choose a valid month, you should choose from all, january, february, ... june.\n")
        month = input()
        if month not in month_data:
            print("Please check your inputs")
    print("You choose " + month.title() + " as your month")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("choose day of week from this options ... all, monday, tuesday, ... or sunday.\n")
    day_data = {'all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'}

    while day not in day_data:
        print(" you should choose from all, monday, tuesday, ... sunday.")
        day = input()
        if day not in day_data:
            print("Sorry, check your inputs")
    print("You choose " + day.title() + " as your week day")

    print('-' * 40)
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

    # convert start time from column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # convert start time to month
    df['month'] = df['Start Time'].dt.month

    # convert start time to month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # convert start time to hour
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # common_month =
    df['month'] = df['Start Time'].dt.month
    print('the most common month = ', df['month'].mode()[0])

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('the most common day of week = ', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('the most common hour = ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('common start station = ', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('common end station = ', common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep='to')
    combination_station = df['Start To End'].mode()[0]
    print('combination station = ', combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time = ", total_travel_time)

    # display mean travel time
    average_travel_time = round(df['Trip Duration'].mean())
    print("total travel time = ", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("counts of user types = ", user_type)

    try:
        # Display counts of gender
        user_gender = df['Gender'].value_counts()
        print("counts of user types = \n", user_gender)
    except:
        print("\n there is no user gender's stats to display or this city is \n")

    try:
        # Display earliest, most recent, and most common year of birth
        user_birth = df['Birth Year']
        earliest_common_year = user_birth.min()
        print("earliest common year = ", int(earliest_common_year))

        recent_common_year = user_birth.max()
        print("recent common year = ", int(recent_common_year))

        most_common_year = user_birth.mode()[0]
        print("most common year = ", int(most_common_year))

    except:
        print("\n there is no user gender's stats to display or this city is \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('results are as below')

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
