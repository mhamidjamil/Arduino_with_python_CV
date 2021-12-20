import cv2
import serial
import time
arduino = serial.Serial(port='COM11', baudrate=9600, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

# def detect_face():


time.sleep(3)
print(write_read("26"))
time.sleep(2)
# 26 to use sensor 1
# 980 to use sensor 2
# votes = 15
# time.sleep(3)
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
video = cv2.VideoCapture(0)
# load "haarcascade_frontalface_default.xml" by creating a CascadeClassifier
# object as cascade
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imgDetected = False
imgcheck = False
print(write_read("98"))
while True:
    check, frame = video.read()

    # Image from webacm is in the format of BGR i.e combination of 3 colours
    # which will basicall require more amount of computation.
    # so we convert it into a gray scale image which is only single colour
    # and requires less computation.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Now we use detectMultiScale method to detect the faces in the video
    # stream. Which will return x,y,w,h which are basically the positions
    # with which we create a rectangle box.
    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

    # using for loop to go through the locations x,y,w,h and drow a rectangle
    for x, y, w, h in face:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3)
        imgcheck = True
        # if not imgDetected and votes < 0:
        #     print(write_read("98"))
        #     imgDetected = True
        #     time.sleep(0.9)
        #     votes = 15
        # elif not imgDetected:
        #     votes -= 1
    # print("no face detected")
    # if imgDetected and votes < 0:
    #     print(write_read("44"))
    #     time.sleep(0.9)
    #     imgDetected = False
    #     votes = 15
    # elif imgDetected:
    #     votes -= 1
    if not imgcheck:
        print("no face detected")
        # if imgDetected and votes < 0:
        print(write_read("44"))
        time.sleep(0.9)
            # imgDetected = False
            # votes = 15
        # elif imgDetected:
            # votes -= 1
    elif imgcheck:
        print("Face detected")
        print(write_read("98"))
        time.sleep(0.9)
    cv2.imshow("Video", frame)
    imgcheck = False
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break

video.release()
cv2.destroyAllWindows()
