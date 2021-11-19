import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
months=['January','Febraury','March', 'April','May','June','All']
days=['Sunday','Monday','Tuesday','wedensday','Thrusday','Friday','Saturday','All']


print('Hello! Let\'s explore some US bikeshare data!')
def get_filters():
  #gets user input for city!
    while True:
        try:
            city =input('Please enter the name of the city? ').lower()
            if city in CITY_DATA:
                break
            else:
                print('This is a wrong city, please choose from Chicago, New york city or Washington')
        except ValueError:
           print("please enter the correct value")
#gets user input for month
    while True:
        try:
            month=input('Please enter the name of Month? ').lower()
            if month.title() in months:
                break
            else:
                print('Please enter the correct Month  ')
        except ValueError:
                print("Please don't enter a number or a special character!")
    #gets user inout for day
    while True:
        try:
            day=input('Please enter the name of day? ').lower()    
            if day.title() in days:
                break
            else:
                print('please enter the correct day')
        except ValueError:
                print('Please enter the correct value')
    print('-'*40)
    return city, month, day

def load_data(city, month, day):

   #read the predefined city! 
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day']= df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
   

    # filter by month if applicable
    if month.title() != 'All':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.title() != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #prints the most common month,day and hour of the data frame
    most_common_month = df['month'].mode()[0]
    print('Most common month of month is: \n',most_common_month)
    #prints the most common day
    most_common_day= df['day'].mode()[0]
    print('Most Common day of hour of the day is: \n',most_common_day)
    #prints the most common hour
    most_common_hour= df['hour'].mode()[0]
    print('Most common hour of the day \n',most_common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    #prints the most common start, end and trip of the data frame
    most_Common_start=df['Start Station'].mode()[0]
    #prints the most common start station
    print('most common start station: ',most_Common_start)
    #prints the most common end station
    most_common_end=df['End Station'].mode()[0]
    print('most common end station: ',most_common_end)
    #prints the most common trip (start and end)
    common_trip= df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1)
    print('most common trip from start to end is: \n',common_trip)
    
    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\n Calculating Trip Duration...\n')
    start_time = time.time()
    #prints the total travel time, total trip duration and average travel time
    total_tavel_time=df['Trip Duration'].sum()
    print('total travel time is : \n',total_tavel_time)
    #prints the average travel time
    average_travel=df['Trip Duration'].mean()
    print('average travel time is: \n',average_travel)
    
    print("\n This took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
   
    print('\n Calculating User Stats...\n')
    start_time = time.time()    
    #counts the user from subscriber and customer.
    counts_of_user= df['User Type'].value_counts()
    print('\n counts of each user type: \n',counts_of_user)
    
    #checks the input of the city
    #gets the most common birth year, and most recent birth year and earliest birth year
    while True:
        try:
            df = pd.read_csv(CITY_DATA[city])
                   
            if city.title()== 'Chicago' or 'New York City':
                print(df['Gender'].value_counts())
                print('\n Most common Birth Year is: \n', df['Birth Year'].mode()[0])
                print('\n Most recent Birth Year is: \n',df['Birth Year'].max())
                print('\n Most Earlist Birth Year is: \n',df['Birth Year'].min())
                break
           
        except KeyError:
                print('Gender infromation only avilable for Chicago and New york City!!')
                break
def ask_more(df,city):
    print('\n Raw Data is avilable to check')
    ask_for_more = input('Would you like to see raw data? Yes or No. ').lower()
    while ask_for_more =='yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                    print(chunk)
                    ask_for_more = input('\nWould you like to view more 5 rows? Enter Yes or No.\n').lower()
                    if ask_for_more !='yes':
                        print('Thank you')
                        break
            break   
     
        except KeyboardInterrupt:
                print('Thank you...')   
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)    
        ask_more(df, city)
        
        
       
#asks the user if they want restart the programme 
        restart = input('Would you like to restart? Enter yes or no.')
        if restart.lower() != 'yes':
            break   

if __name__ == "__main__":
	main()
