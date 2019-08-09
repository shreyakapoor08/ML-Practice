#Read a Video Stream from Camera(Frame by Frame)
import cv2

#first step is to capture the device from which you want to read your ip stream
#each vid is a series of frame and each frame is a img
cap = cv2.VideoCapture(0) #for default webcam

while True:
	ret,frame = cap.read() #this method returns 2 things one is the bool val return value and other is the frame that has been captured
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #if you want to convert img to gray

	if ret == False: #like if webcam is not started
		continue

	cv2.imshow("Video Frame",frame)
	cv2.imshow("Gray frame",gray_frame)

	#wait for user input -q, then you will stop the loop
	
	#check which key user has pressed

	#0xFF is a number with 8 ones waitKey(1) is a 32 bit number
	#we are trying to convert 32 bit number into 8 bit number
	#then we will compare the 8bit number with ascii value of q
	key_pressed = cv2.waitKey(1) & 0xFF #prog will wait for 1 millisec before next iteration comes up and we will do a bitwise and operation
	if key_pressed == ord('q'): #ord tells the ascii value of the specified character
		break


cap.release()
cv2.destroyAllWindows()
