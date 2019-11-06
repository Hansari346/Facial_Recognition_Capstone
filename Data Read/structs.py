
class student:
    def __init__(self, student_name, student_id, anchor_images, attendance_record, class_schedule):
        self.name = student_name
        self.ID = student_id
        self.anchors = anchor_images
        self.att = attendance_record
        self.sched = class_schedule
    def __str__(self):
        return "Name: %s, ID: %s Class Schedule: %s Attendance Record: %s" % (self.name, self.ID, self.sched, self.att)
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