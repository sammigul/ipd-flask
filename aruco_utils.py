import cv2
import cv2.aruco as aruco

'''
calculate_pixel_mm_ration --> takes path to the image, marker size in millimetres and aruco dictionary type as arguments
--> returns the pixel-to-mm ratio(float), by detecting the aruco marker and then using it's known perimeter(in mm) and
perimeter in pixels. 
--> returns 0.0 if there is no aruco marker detected 
'''

def calculate_pixel_mm_ratio(image_path, marker_size_mm, aruco_dict_type):
    # Load ArUco dictionary
    parameters = aruco.DetectorParameters()
    aruco_dict = aruco.getPredefinedDictionary(aruco_dict_type)
    
    # Create ArUco detector
    aruco_detector = aruco.ArucoDetector(aruco_dict, parameters)
    
    image = cv2.imread(image_path)
    pixel_mm_ratio = 0.0

    # Detect ArUco marker
    corners, ids, rejected = aruco_detector.detectMarkers(image)

    if ids is not None:
        # Perimeter of the ArUco marker
        aruco_perimeter = cv2.arcLength(corners[0], True)
        # Calculate pixel to mm ratio
        pixel_mm_ratio = aruco_perimeter / (marker_size_mm * 4)

    return pixel_mm_ratio



'''
calculate_pixel_mm_ratio_video --> takes frame, marker size in millimetres and aruco dictionary type as arguments
--> returns the pixel-to-mm ratio(float), by detecting the aruco marker and then using it's known perimeter(in mm) and
perimeter in pixels. 
--> returns 0.0 if there is no aruco marker detected 
'''

def calculate_pixel_mm_ratio_video(frame, marker_size_mm, aruco_dict_type):
    # Load ArUco dictionary
    parameters = aruco.DetectorParameters()
    aruco_dict = aruco.getPredefinedDictionary(aruco_dict_type)
    
    # Create ArUco detector
    aruco_detector = aruco.ArucoDetector(aruco_dict, parameters)
    
    pixel_mm_ratio = 0.0

    # Detect ArUco marker
    corners, ids, rejected = aruco_detector.detectMarkers(frame)

    if ids is not None:
        # Perimeter of the ArUco marker
        aruco_perimeter = cv2.arcLength(corners[0], True)
        # Calculate pixel to mm ratio
        pixel_mm_ratio = aruco_perimeter / (marker_size_mm * 4)

    return pixel_mm_ratio

