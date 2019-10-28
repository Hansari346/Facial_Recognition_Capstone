class student:
    def __init__(self, student_name, student_id, anchor_images, attendance_record, class_schedule):
        self.name = student_name
        self.ID = student_id
        self.anchors = anchor_images
        self.att = attendance_record
        self.sched = class_schedule
class classroom:
    def __init__(class_id, classroom_weight, class_students):
        self.ID = classID
        self.weight = weight 
        self.students = class_students
    
	
	
if __name__ == '__main__':
	student_list = []
	classroom_list = []
	#read student data in from csv file
	with open('student_list.csv', newline='') as csv_file:
		reader = csv.reader(csv_file)
		next(reader, None)  # Skip the header.
		# Unpack the row directly in the head of the for loop.
		for student_name, student_id, profile_picture, sched1, sched2, sched3, sched4, sched5, sched6 in reader:
			# Convert the numbers to floats.
			student_id = float(student_id)
			sched1 = float(sched1)
			sched2 = float(sched2)
			sched3 = float(sched3)
			sched4 = float(sched4)
			sched5 = float(sched5)
			sched6 = float(sched6)
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
		for class_id in reader:
			# Convert the numbers to floats.
			class_id= float(class_id)
			#Create blank instances to fill in student list and classroom weight
			students = []
			weight = ' '
			# Create the classroom instance and append it to the list.
			classroom_list.append(classroom(class_id, weight, students))
	#Loop through students and place them in classrooms
	for student in student_list:
		for i in range (len (student.class_schedule)):
			for classroom in classroom_list:
				if (student.class_schedule[i] == classroom.class_id):
					classroom.students.append(student)
					break
			