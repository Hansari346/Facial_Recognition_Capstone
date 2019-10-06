from datetime import datetime

#class passing times are 6:55 AM, 7:55 AM, 8:55 AM, 9:55 AM, 10:55 AM, 11:55 AM, 12:55 PM
ClassPassingTimes = [24900, 28500, 32100, 35700, 39300, 42900, 46500]


def PassingtimeInterrupt():

    DT = datetime.now()
    time_in_seconds = DT.second + DT.minute * 60 + DT.hour * 3600

    if time_in_seconds == ClassPassingTimes[0]:
        return True
    elif time_in_seconds == ClassPassingTimes[1]:
        return True
    elif time_in_seconds == ClassPassingTimes[2]:
        return True
    elif time_in_seconds == ClassPassingTimes[3]:
        return True
    elif time_in_seconds == ClassPassingTimes[4]:
        return True
    elif time_in_seconds == ClassPassingTimes[5]: 
        return True
    elif time_in_seconds == ClassPassingTimes[6]:
        return True
    else:
        return False


