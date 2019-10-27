from VidsFrames_Final import *
from i2c_trigger_Final import *
from Passing_Time_Interrupt_Final import *
from Student_siamese_Test_Final import *
from GPIO_setup import *
import threading
import time

#load MTCNN network once to save time
detector = MTCNN()

VideosPath = "/home/hewitt/Desktop/Project/Videos" #folder for videos
FramesPath = "/home/hewitt/Desktop/Project/Frames" #folder for frames
FacesPath = "/home/hewitt/Desktop/Project/Faces" #folder for faces
LateFramesPath = "/home/hewitt/Desktop/Project/Late_Frames" #folder for late faces
LateFacesPath = "/home/hewitt/Desktop/Project/Late_Faces"
OldFramesPath = "/home/hewitt/Desktop/Project/Old_Frames"
OldFacesPath = "/home/hewitt/Desktop/Project/Old_Faces"

Thermal_trigger = False
PassingTimeBool = False


def Trigger():
    global Thermal_trigger
    while True:
        Thermal_trigger = Thermal_Values()
#        print(Thermal_trigger)
        time.sleep(0.1)


def PassingTime():
    global Thermal_trigger, PassingTimeBool, loaded_model

#    if PassingTimeBool == False: #while passing time is true
#    while PassingTimeBool == False:
#        if Thermal_trigger == True:
#            TakeVideo()

    while PassingTimeBool == False:
        if Thermal_trigger == True:
            FrameCapture(LateFramesPath) #note: must delete previous pictures 
            BoundingBox(LateFramesPath,LateFacesPath, detector)
            StudentPredict(LateFacesPath)
            #determine whether or not to open the door
            MoveImages(LateFacesPath,OldFacesPath,LateFramesPath,OldFramesPath)
        


def PassingTimeInterrupt():
    global PassingTimeBool
    PassingTimeBool = ReturnPassingTime()




func1 = threading.Thread(target=Trigger)
func2 = threading.Thread(target=PassingTime)
#func3 = threading.Thread(target=PassingTimeInterrupt)

func1.start()
func2.start()
#func3.start()

func1.join()
func2.join()
#func3.join()


cap.release()
