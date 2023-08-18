"""A simple module to hold the necessary functions.

Not much to add.

"""


def find_session_duration(dates_array, minimum_duration=60*10, ignore_isolated=False, isolated_duration=60):
    """Reads an array of timestamps and determines groups of them, when each differs from previous one for less than a minimum duration
    
    Arguments:
        dates_array: An pandas.Series of datetime objects
        minimun_duration: An int or float, denoting a time interval in seconds
        ignore_isolated: A bool flag, when false each action not in a session gets a user defined duration.
        isolated_duration: the user defined duration for actions outside of sessions. Active when ignore_isolated=False

    Returns:
        A pandas.Series of floats. Each item in the list, is the time elapsed between two datetimes in minutes.

    Special cases:
        Returns empty Series when 1) List length less than two, 2) not found any matching intervals
    
    Examples:
       Inputs: [Timestamp('2021-05-11 12:12:45'),  Timestamp('2021-05-12 12:02:45'),  Timestamp('2021-05-14 12:02:44')], 60*60*24
       Outputs: [1430*60]
       Explanation: From first date to second is 24hours bar 10 minutes. From second to third, is much more than 24 hours

       Inputs: [Timestamp('2021-05-11 12:12:45'),  Timestamp('2021-05-12 12:02:45'),  Timestamp('2021-05-13 02:02:44')], 60*60*24
       Outputs: [2150*60]
       Explanation: From first date to second is a bit less than 24hours bar 10 minutes. From second to third, is exactly 24 hours
       
       Inputs: [Timestamp('2021-05-11 12:12:45'), Timestamp('2021-08-06 16:47:15')], 60*60
       Outputs: []
       Explanation: From beginning to end is almost 3 months, or a quarter of a year - no valid period to return.
    """
    import pandas as pd

    ## lists are slower than series, but easier to manipulate when developing
    ## consider refactoring to series
    dates_array = dates_array.tolist()

    ## covers cases without enough data points, no need to wait, just return
    if len(dates_array) <= 1:
        return pd.Series([])


    ## we have to sort for the concept to work - earlier dates first
    dates_array.sort()  

    start = dates_array[0]

    previous =  dates_array[0]

    duration = 0

    to_return = []


    for date in dates_array[1:] :
        
        if  ( (date - previous).total_seconds() ) < minimum_duration:
            duration = (((date - start).total_seconds()) )  ## we record duration here
            previous = date
        
        else:
            if (duration == None) and (ignore_isolated == False):  ## conditions catching actions outside of sessions
                to_return.append(isolated_duration)
            else:
                to_return.append((duration))  ## and we commit duration here
                duration = None            
            
            start = date
            previous = date

    to_return.append(duration) ## just a last time for the case the last date < minimum_duration and we haven't appended
        


    ## the process above adds unnecessary None's ## and we switch back to minutes
    to_return = [round((duration/60), 2) for duration in to_return if duration is not None ]  
    return pd.Series(to_return)





if __name__ == "__main__":
    print("Nothing much to run, without the correct inputs")
