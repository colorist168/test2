import cv2 as cv

def video_test():
	cap = cv.VideoCapture(10)      # 10为usb的设备ID号
	while(cap.isOpened()):
		ref,frame = cap.read()
		cv.imshow('1',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cap.release()
			break
video_test()
