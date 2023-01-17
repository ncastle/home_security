from picamera2 import Picamera2
import time
import os

picam2 = Picamera2()
camera_config = picam2.create_still_configuration()
picam2.configure(camera_config)
picam2.start(show_preview=False)
time.sleep(1)


""" function find current directory that this file lives in
    checks if the images directory exists, makes it if not
    captures image and stores it in images directory
    using the file_name and pic parameters to create a name
"""
def take_picture(file_name, pic):
    dir_name = os.path.dirname(os.path.realpath(__file__))  ## get current directory

    if (not os.path.exists(dir_name + '/images/')):     ## create images directory if it does not exist
        os.mkdir(dir_name + '/images/')

    full_file_name = dir_name + '/images/' + file_name + '%03d.jpg' % pic   ## create full path & file name

    time.sleep(1)
    picam2.capture_file(full_file_name) ## capture picture after 1 second
