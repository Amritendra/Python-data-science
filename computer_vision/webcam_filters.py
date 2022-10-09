import cv2

def start_camera(cam_id=0):
    camera=cv2.VideoCapture(cam_id)
    while camera.isOpened():
        _,image=camera.read()
        image2=image*225
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        cv2.imshow('Webcam output',image)
        cv2.imshow('image2',image2)
        cv2.imshow('Gray',gray)
        cv2.imshow('RGB',rgb)
        if cv2.waitKey(1)==27: #escape key
            break
    camera.release()  #free up the camera
    cv2.destroyAllWindows()  #close all windows

start_camera()
