import datetime
import dataread
import structs


def TakeAttendance(name, date_time_str, class_ID):
  date_time_str = "2019-11-03 15:14:10.866418.avi"
  date_time_str = date_time_str[:-4]
  date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

  print('Date:', date_time_obj.date())
  print('Time:', date_time_obj.time())
  print('Date-time:', date_time_obj)
  period = 1
  for structs.classroom in dataread.classroom_list:
    print (structs.classroom.ID)
    if (class_ID == structs.classroom.ID):
      this_classroom = structs.classroom
  for dataread.student in this_classroom.students:
    if (dataread.student.name == name):
      dataread.student.att[date_time_obj.date()][period] = 'P'
      print(dataread.student)