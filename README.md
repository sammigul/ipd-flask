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
## Downloading shape_predictor_68_face_landmarks.dat
  - This file can be downloadeed from [this github repository](https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat
)
  - Place this in the root of repository 

## Running the App

1. Setting the Environment Variables
  ```bash
    set FLASK_APP=app.py
    set FLASK_ENV=development
  ```
2. Running the App
   
   ```bash
   flask run -p PORTNO  # Replace PORTNO with the desired port number (default is 5000)
   ```
   
   OR use this command if flask is not set in path variable
   
   ```bash
   python -m flask run -p PORTNO  # Replace PORTNO with the desired port number (default is 5000)
   ```
## API Endpoint to measure ipd

   Send an HTTP POST request to http://127.0.0.1:5000/measure_ipd, server will return the ipd distance in millimetres 

## Image Input Instructions
- Aruco Marker File([75mm.pdf](https://github.com/sammigul/ipd-flask/edit/main/75mm.pdf)) is to be downloaded and printed.
- Some sample images have been uploaded ([5.jpg](https://github.com/sammigul/ipd-flask/edit/main/5.jpg) and [6.jpg](https://github.com/sammigul/ipd-flask/edit/main/6.jpg)), you can use them for testing purpose
 


   
