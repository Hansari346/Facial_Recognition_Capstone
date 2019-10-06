from datetime import datetime

#class start times are at 7 AM, 8 AM, 9 AM, 10 AM, 11 AM, 12 PM, 1 PM
ClassStartTimes = [25200, 28800, 32400, 36000, 39600, 43200, 46800]


def PassingtimeInterrupt():

    DT = datetime.now()
    time_in_seconds = DT.second + DT.minute * 60 + DT.hour * 3600

    if time_in_seconds == ClassStartTimes[0]:
        return True
    elif time_in_seconds == ClassStartTimes[1]:
        return True
    elif time_in_seconds == ClassStartTimes[2]:
        return True
    elif time_in_seconds == ClassStartTimes[3]:
        return True
    elif time_in_seconds == ClassStartTimes[4]:
        return True
    elif time_in_seconds == ClassStartTimes[5]: 
        return True
    elif time_in_seconds == ClassStartTimes[6]:
        return True
    else:
        return False


