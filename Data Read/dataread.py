import csv
import datetime
from datetime import date, timedelta
import structs  
		
    
	
	
def DataRead():
	student_list = []
	global classroom_list
	classroom_list = []
	dates_of_year = []
	sdate = date(2019, 1, 1)   # start date
	edate = date(2019, 12, 31)   # end date
	period = [None] * 6
	delta = edate - sdate       # as timedelta

	for i in range(delta.days + 1):
		day = sdate + timedelta(days=i)
		dates_of_year.append(day)		
	attendance_record = dict.fromkeys(dates_of_year, period)
	
	#read student data in from csv file
	with open('student_list.csv', newline='') as csv_file:
		reader = csv.reader(csv_file)
		next(reader, None)  # Skip the header.
		# Unpack the row directly in the head of the for loop.
		for student_name, student_id, profile_picture, sched1, sched2, sched3, sched4, sched5, sched6 in reader:
			#Initialize the arrays
			class_schedule = [sched1,sched2,sched3,sched4,sched5,sched6]
			anchor_images = [profile_picture]
			# Create the student instance and append it to the list.
			# Create the student instance and append it to the list.
			student_list.append(structs.student(student_name, student_id, anchor_images, attendance_record, class_schedule))
	#read classroom data from csv file
	with open('classroom_list.csv', newline='') as csv_file:
		reader = csv.reader(csv_file)
		next(reader, None)  # Skip the header.
		# Unpack the row directly in the head of the for loop.
		for class_name, class_id, camera_ID, thermal_ID in reader:
			#Create blank instances to fill in student list and classroom weight
			students = []
			weight = '0'
			# Create the classroom instance and append it to the list.
			classroom_list.append(structs.classroom(class_name, class_id, weight,  camera_ID, thermal_ID, students))
	#Loop through students and place them in classrooms
	for classroom in classroom_list:
		print(classroom)
		for student in student_list:
			for i in range (len(student.sched)):      
				if (student.sched[i] == classroom.ID):
					classroom.students.append(student)
					print(student)

