from VidsFrames_Final import *
from i2c_trigger_Final import *
from Passing_Time_Interrupt_Final import *
from Student_siamese_Test_Final import *
from GPIO_setup import *
import threading
import time
import cv2

ProjectPath = "/home/hewitt/Desktop/Project/"
VideosPath = ProjectPath + "Videos" #folder for videos
FramesPath = ProjectPath + "Frames" #folder for frames
FacesPath = ProjectPath + "Faces" #folder for faces
LateFramesPath = ProjectPath + "Late_Frames" #folder for late faces
LateFacesPath = ProjectPath + "Late_Faces"
OldFramesPath = ProjectPath + "Old_Frames"
OldFacesPath = ProjectPath + "Old_Faces"
RoomPath = ProjectPath + "Rooms/101"
StudentsPath = ProjectPath + "Student_Pictures"


#load MTCNN network once to save time
dummyFrame = ProjectPath + "Dummy_Frame"
detector = MTCNN()
TakeFrames(LateFramesPath)
BoundingBox(LateFramesPath,LateFacesPath,detector)
for img in os.listdir(LateFacesPath):
    os.remove(LateFacesPath + "/" + img)
for img in os.listdir(LateFramesPath):
    os.remove(LateFramesPath + "/" + img)


Thermal_trigger = False
PassingTimeBool = False


def Trigger():
    global Thermal_trigger
    while True:
        Thermal_trigger = Thermal_Values()
        time.sleep(0.05)

def ClassTime():
    global Thermal_trigger, PassingTimeBool, init, detector

    while PassingTimeBool == False:
        if Thermal_trigger == True:
            TakeFrames(LateFramesPath) 
            BoundingBox(LateFramesPath,LateFacesPath, detector)
            student, studentMins = StudentPredict(LateFacesPath,RoomPath,StudentsPath)
            isStudent = StudentValidity(student,studentMins,StudentsPath)
            if isStudent == True:
                Unlock_Door()
                #take attendance of student here
            else:
                Lock_Door()
                #notify teacher here
            MoveData(LateFacesPath,OldFacesPath)
            MoveData(LateFramesPath,OldFramesPath)


def ClassTimeAttendance():
    while PassingTimeBool == True:
        if Thermal_trigger == True:
            Vids2Frames(VideosPath,FramesPath)
            BoundingBox(FramesPath, FacesPath, detector)
            total_predictions = StudentPredict2(FacesPath,RoomPath,StudentPath)
            Students = StudentValidity2(total_predict, StudentsPath)
            #AttendanceAlgorithm

def PassingTime():
    global Thermal_trigger, PassingTimeBool

    #while passing time is false
    while PassingTimeBool == True:
        if Thermal_trigger == True:
            TakeVideo(VideosPath)



def PassingTimeInterrupt():
    global PassingTimeBool
    PassingTimeBool = ReturnPassingTime()




func1 = threading.Thread(target=Trigger)
func2 = threading.Thread(target=PassingTime)
func3 = threading.Thread(target=PassingTimeInterrupt)
func4 = threading.Thread(target=ClassTime)

func1.start()
func2.start()
func3.start()
func4.start()

func1.join()
func2.join()
func3.join()
func4.join()

cap.release()
