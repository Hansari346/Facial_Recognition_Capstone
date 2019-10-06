import cv2
from mtcnn.mtcnn import MTCNN
detector = MTCNN()

cap = cv2.VideoCapture(0)
#resolution
cap.set(3, 480)
cap.set(4,480)
cap.set(5,5)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


while True: 
    #Capture frame-by-frame
    __, frame = cap.read()
    
    #Use MTCNN to detect faces
    result = detector.detect_faces(frame)
    if result != []:
        for person in result:
            bounding_box = person['box']
            keypoints = person['keypoints']

            pt1 = bounding_box[0],bounding_box[1]
            pt2 = bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]
            color = (255,0,0)
            thickness = 1
            lineType = 4
            shift = 0
            cv2.rectangle(frame,pt1,pt2,color,thickness,lineType,shift)

            cv2.circle(frame,(keypoints['left_eye']),2,color,thickness,lineType,shift)
            cv2.circle(frame,(keypoints['right_eye']),2,color,thickness,lineType,shift)
            cv2.circle(frame,(keypoints['nose']),2,color,thickness,lineType,shift)
            cv2.circle(frame,(keypoints['mouth_left']),2,color,thickness,lineType,shift)
            cv2.circle(frame,(keypoints['mouth_right']),2,color,thickness,lineType,shift)
    #display resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
#When everything's done, release capture
cap.release()
cv2.destroyAllWindows()
