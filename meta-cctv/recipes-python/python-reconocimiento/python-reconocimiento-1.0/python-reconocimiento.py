# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
from datetime import datetime
import numpy as np
import argparse
import imutils
import time
import cv2
import os.path
<<<<<<< HEAD
import io
import socket
import struct
import time
=======
>>>>>>> 51945bb8d2644665cca715824eb4b66e8705fdae

################# Getting and parsing datetime in one string ###################

def ParseDate(inputdate):
        year = inputdate.strftime("%Y")
        month = inputdate.strftime("%h")
        day = inputdate.strftime("%d")
        time = inputdate.strftime("%H: %M: %S")
        completeTime = "Registrado el " + day + " de " + month + " del " + year + " a las " + time + "."
        return completeTime
        
################################################################################

######################## Writing on files function #############################

def WritingFile(countperson, countdog, countcat, date):
    countp = str(countperson)
    countd = str(countdog)
    countc = str(countcat)
    mensaje = "Persona(s) = " + countp + ", Perro(s) = " + countd + " y Gato(s) = " + countc + ". " + date
    file_exists = os.path.isfile("SessionRecognition.txt")
    if (file_exists):
        #print("File already exists! Writing in that one...")
        f = open("SessionRecognition.txt", "a")
        #json.dump(data, f)
        f.write(mensaje)
        f.write("\n")
    else:
        print("File does no exist! Creating one...")
        f = open("SessionRecognition.txt", "w+")
        WritingFile(countperson, countdog, countcat, date)

################################################################################

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
ap.add_argument("-s", "--showimage", type=str, default="no",
	help="show or not show video")
args = vars(ap.parse_args())

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
dataperson = 0;
datadog = 0;
datacat = 0;
# Create an array for jason format
data = {}
<<<<<<< HEAD
showVideo = args["showimage"]
=======
>>>>>>> 51945bb8d2644665cca715824eb4b66e8705fdae
# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# initialize the consider set (class labels we care about and want
# to count), the object count dictionary, and the frame  dictionary
CONSIDER = set(["dog", "person", "cat"])
objCount = {obj: 0 for obj in CONSIDER}
frameDict = {}
# initialize the dictionary which will contain  information regarding
# when a device was last active, then store the last time the check
# was made was now
lastActive = {}
lastActiveCheck = datetime.now()

# initialize the video stream, allow the cammera sensor to warmup,
# and initialize the FPS counter
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
fps = FPS().start()

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# grab the frame dimensions and convert it to a blob
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
		0.007843, (300, 300), 127.5)

	# pass the blob through the network and obtain the detections and
	# predictions
	net.setInput(blob)
	detections = net.forward()
	
	objCount = {obj: 0 for obj in CONSIDER}

	# loop over the detections
	for i in np.arange(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the prediction
		confidence = detections[0, 0, i, 2]
                
		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
		if confidence > args["confidence"]:
			# extract the index of the class label from the
			# `detections`, then compute the (x, y)-coordinates of
			# the bounding box for the object
                        idx = int(detections[0, 0, i, 1])
                        box = detections[0, 0, i, 3:7]*np.array([w, h, w, h])
                        (startX, startY, endX, endY) = box.astype("int")
<<<<<<< HEAD
                        label = " ,".join("{}: {}".format(obj, count) for (obj, count) in objCount.items())
=======
>>>>>>> 51945bb8d2644665cca715824eb4b66e8705fdae
                        if CLASSES[idx] in CONSIDER:
                                objCount[CLASSES[idx]] += 1
                                # draw the prediction on the frame
                                cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)

                        label = " ,".join("{}: {}".format(obj, count) for (obj, count) in objCount.items())

                        getDate = datetime.now()
                        actualTime = ParseDate(getDate)
                        
                        data["person"] = objCount["person"]
                        data["dog"] = objCount["dog"]
                        data["cat"] = objCount["cat"]
                        
                        if (data["person"] != dataperson or data["dog"] != datadog or data["cat"] != datacat):
                                #print(data)
                                WritingFile(objCount["person"], objCount["dog"], objCount["cat"], actualTime)
                        
                        dataperson = data["person"]
                        datadog = data["dog"]
                        datacat = data["cat"]
                        
                        cv2.putText(frame, label, (10, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                                
                        y = startY - 15 if startY - 15 > 15 else startY + 15
                        
	# show the output frame
	#WritingFile(objCount["person"])
<<<<<<< HEAD
	if showVideo == "yes":
                cv2.imshow("Frame", frame)
        
=======
	cv2.imshow("Frame", frame)
>>>>>>> 51945bb8d2644665cca715824eb4b66e8705fdae
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

# USAGE
# python3 real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel
