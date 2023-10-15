import cv2
import numpy as np
import dlib


from aruco_utils import calculate_pixel_mm_ratio
from utils import midpoint

# Loading detector and predictor
detector = dlib.get_frontal_face_detector()
predectior = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


def imageAnalysis(image_path,marker_size_mm,aruco_dict_type):
    image = cv2.imread(image_path)
    grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = detector(grey_image)
    if len(faces) == 0:
        return "No Faces Detected"
    # If mulitle faces are detected we can still estimate the distance in between their pupils but that would be imprecise so only using the first face
    # add a loop for iterating the faces returned, also add a new list distances to store them all

    face = faces[0] 
    x, y = face.left(), face.top()
    x1, y1 = face.right(), face.bottom()
    cv2.rectangle(image, (x,y), (x1,y1), (0,255,0), 2)
    landmarks = predectior(grey_image, face)  # left eye is 36 to 41 and right eye is 42 to 47
    
    # pupil detection -- pupil is located between the center of these points
    pupil_left = midpoint(landmarks.part(36), landmarks.part(39))   # left eye
    pupil_right = midpoint(landmarks.part(42), landmarks.part(45))  # right eye
    cv2.circle(image, pupil_left, 1, (0, 0, 255), 1)
    cv2.circle(image, pupil_right, 1, (0, 0, 255), 1)

    cv2.line(image,pupil_left,pupil_right,(0,255,0),2)

    # Calculating the distance of this line that is the distance between the two pupils
    pixel_distance = (np.linalg.norm(np.array(pupil_left) - np.array(pupil_right)))
    px_mm_ratio = calculate_pixel_mm_ratio(image_path, marker_size_mm, aruco_dict_type)

    # If no aruco marker is detected then the px_mm_ratio will be 0.0
    if (px_mm_ratio == 0.0):
        return f"No Aruco Marker Detected, pixel Distance is {round(pixel_distance,2)}"
        # return f"No Aruco Marker Detected, IPD in pixels is {pixel_distance}"

    distance = round((pixel_distance/px_mm_ratio),1) 
    return distance

    cv2.imshow('Image', image)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
