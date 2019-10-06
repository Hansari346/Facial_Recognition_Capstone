

import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()

image = cv2.imread("frame0.jpg")

result = detector.detect_faces(image)

bounding_box = result[0]['box']

keypoints = result[0]['keypoints']

pt1 = bounding_box[0],bounding_box[1]

pt2 = bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]

color = (255,0,0)

thickness = 1

lineType = 4

shift = 0

cv2.rectangle(image,pt1,pt2,color,thickness,lineType,shift)

cv2.imwrite("frame0.jpg",image)
cv2.namesWIndow("image")
cv2.imshow("image",image)
cv2.waitKey(0)


