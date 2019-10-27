from datetime import datetime

#class passing times are 6:55 AM, 7:55 AM, 8:55 AM, 9:55 AM, 10:55 AM, 11:55 AM, 12:55 PM
#class passing times are 5 minutes long
ClassPassingTimes = [24900, 28500, 32100, 35700, 39300, 42900, 46500]

ClassStartingTimes = [25200, 28800, 32400, 36000, 39600, 43200, 46800]

def ReturnPassingTime():

    DT = datetime.now()
    time_in_seconds = DT.second + DT.minute * 60 + DT.hour * 3600

    if time_in_seconds >= ClassPassingTimes[0] and time_in_seconds <= ClassStartingTimes[0]:
        return True
    elif time_in_seconds >= ClassPassingTimes[1] and time_in_seconds <= ClassStartingTimes[1]:
        return True
    elif time_in_seconds >= ClassPassingTimes[2] and time_in_seconds <= ClassStartingTimes[2]:
        return True
    elif time_in_seconds >= ClassPassingTimes[3] and time_in_seconds <= ClassStartingTimes[3]:
        return True
    elif time_in_seconds >= ClassPassingTimes[4] and time_in_seconds <= ClassStartingTimes[4]:
        return True
    elif time_in_seconds >= ClassPassingTimes[5] and time_in_seconds <= ClassStartingTimes[5]: 
        return True
    elif time_in_seconds >= ClassPassingTimes[6] and time_in_seconds <= ClassStartingTimes[6]:
        return True
    else:
        return False

def Take_Attendance(img,person):
    
    #example format of img: 2019-10-13 19:20:40.733783

    timing = img[0:-4]

    year = int(timing[0:4])
    month = int(timing[5:7])
    day = int(timing[8:10])
    hour = int(timing[11:13])
    minute = int(timing[14:16])
    second = int(timing[17:19])
    microsecond = int(timing[20:26])





