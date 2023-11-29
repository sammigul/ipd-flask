from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import cv2
import cv2.aruco as aruco
import os

from ipd_image import imageAnalysis
from utils import is_valid_image

app = Flask(__name__)


# Constants for ArUco marker size and dictionary type
MARKER_SIZE_MM = 75
ARUCO_DICT_TYPE = aruco.DICT_4X4_100


@app.route('/measure_ipd',methods=['POST'])
@cross_origin()
def measure_ipd():
    try:
        # user_image = request.files['userImage']
        user_image = request.files.get('userImage')
        if user_image is None or not user_image.filename: # if no image is provided or the image is empty
            return jsonify({'error': 'No image provided'}), 400
        if (not is_valid_image(user_image)): 
            return jsonify({'error': 'Invalid File Provided, Please provide an image with .png,.jpg or jpeg extension'}), 400
        
        '''
        Save the user's image to a file, e.g., 'temp.jpg', 
        Call the imageAnalysis() function to calculate the IPD

        '''
        original_filename = user_image.filename
        file_extension = original_filename.rsplit('.', 1)[-1].lower()
        # Save the user's image with the same file extension
        saved_filename = f'temp.{file_extension}'
        user_image.save(saved_filename)

        result = imageAnalysis(saved_filename,MARKER_SIZE_MM,ARUCO_DICT_TYPE)
        os.remove(saved_filename)
        print(result)
        if (type(result) == str):
            return jsonify({'error': result}), 400 # bad image provided by user appropriate error code is returned
        else:
            return jsonify({'ipd_in_mm': result}), 200 
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# filename = '75mm.pdf'

@app.route('/aruco_marker',methods=['GET'])
def serve_pdf():
    return send_from_directory('static', '75mm.pdf')