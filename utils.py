import cv2


#  Helper Method to calculate midpoit between two coordinates
def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

# Cheking if the image provided in the request is valid or not 
def is_valid_image(file):
    try:
        # Check if the file has an allowed extension (e.g., 'jpg', 'jpeg', 'png',  etc.)
        allowed_extensions = {'jpg', 'jpeg', 'png'}
        file_extension = file.filename.rsplit('.', 1)[1].lower()
        if file_extension not in allowed_extensions:
            return False


        return True
    except Exception:
        return False

def template_matching(image_path,template_path):
    img = cv2.resize(cv2.imread(image_path, 0), (0, 0), fx=0.8, fy=0.8)
    template = cv2.imread(template_path, 0)
    
    # Preprocess the template by applying guassian blur
    # template = cv2.GaussianBlur(template, (5, 5), 0)
    
    h, w = template.shape
    
    # Choose 
    method = cv2.TM_CCORR_NORMED
    
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # threshold for matching
    threshold = 0.8
    
    if max_val > threshold:
        location = max_loc
        bottom_right = (location[0] + w, location[1] + h)
        cv2.line(img2, location, bottom_right, 255, 5)
        # cv2.rectangle(img2, location, bottom_right, 255, 5)
        cv2.imshow('Match', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Template not found")

