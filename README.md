# ipd-flask
Simple flask app that provides api endpoint for ipd distance measurement.

## Requirements

- Flask
- NumPy
- OpenCV-Python
- Dlib 
- Shape predictor file (shape_predictor_68_face_landmarks.dat)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sammigul/ipd-flask.git
   
2. Installing packages
   ```bash 
   pip install flask numpy opencv-python
   ```
3. Installing dlib (depends on the python version for ver 3.11 this file that I provided in the repo is required)
   ```bash 
   pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
   ```
## Downloadin shape_predictor_68_face_landmarks.dat
  -- This file can be downloadeed from [this github repository](https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat
)

## Running the App

1. Download shape_predictor_68_face_landmarks.dat file (Apprx 95 mb) and place it in the root of the repo
2. Setting the Environment Variables
  ```bash
    set FLASK_APP=app.py
    set FLASK_ENV=development
  ```
3. Running the App
   ```bash
   flask run -p PORTNO  # Replace PORTNO with the desired port number (default is 5000)
   ```
4. API Endpoint to measure ipd
   Send an HTTP POST request to http://127.0.0.1:5000/measure_ipd, server will return the ipd distance in millimetres 
 


   
