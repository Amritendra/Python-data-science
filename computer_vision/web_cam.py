import cv2

def start_camera(cam_id=0):
    camera = cv2.VideoCapture(cam_id)
    while camera.isOpened():
        _, image = camera.read()
        cv2.imshow('Webcam output', image)
        if cv2.waitKey(1) == 27:  # escape key
            break
    camera.release()  # free up the camera
    cv2.destroyAllWindows()  # close all windows

if __name__ == '__main__':
    start_camera()  # 0 is the default camera
