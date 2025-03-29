def main():

    DAYS_IN_YEAR: int = 365
    HOURS_IN_DAY: int = 24
    MINUTES_IN_HOUR: int = 60
    SECONDS_IN_MINUTE: int = 60
    
    seconds_in_year: int = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE
    

    print("There are", seconds_in_year, "seconds in a year!")


if __name__ == '__main__':
    main()