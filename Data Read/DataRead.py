import csv

class student:
    def __init__(self, student_name, student_id, anchor_images, attendance_record, class_schedule):
        self.name = student_name
        self.ID = student_id
        self.anchors = anchor_images
        self.att = attendance_record
        self.sched = class_schedule
    def __str__(self):
        return "Name: %s, ID: %s Class Schedule: %s" % (self.name, self.ID, self.sched)
class classroom:
    def __init__(self, class_name, class_id, classroom_weight, camera_ID, thermal_ID, class_students):
        self.name = class_name
        self.ID = class_id        
        self.weight = classroom_weight 
        self.students = class_students
        self.cameraID = camera_ID
        self.thermalID = thermal_ID
    def __str__(self):
        return "Name: %s, ID: %s Class Camera ID: %s Thermal ID: %s" % (self.name, self.ID, self.cameraID, self.thermalID)        
		
    
	
	
if __name__ == '__main__':
	student_list = []
	classroom_list = []
	attendance_record = []
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
			student_list.append(student(student_name, student_id, anchor_images, attendance_record, class_schedule))
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
			classroom_list.append(classroom(class_name, class_id, weight,  camera_ID, thermal_ID, students))
	#Loop through students and place them in classrooms
	for classroom in classroom_list:
		print(classroom)
		for student in student_list:
			for i in range (len(student.sched)):      
				if (student.sched[i] == classroom.ID):
					classroom.students.append(student)
					print(student)