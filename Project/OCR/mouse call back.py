import cv2
import imutils
import numpy as np

mouse_is_pressing = False
start_x, start_y = -1, -1
end_x, end_y = 1,1

#1. 마우스 이벤트 발생시 호출함 함수 정의
def Mouse_callback(event, x, y, flags, param):
    global mouse_is_pressing, start_x, start_y, end_x, end_y

    img_result = image.copy()

    #왼쪽 마우스 버튼 누르고 있을때 발생
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_is_pressing = True

        start_x, start_y = x, y

        #누른 시작 지점에 원 그림
        cv2.circle(img_result, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow("Test", img_result)

        print('왼쪽 마우스 누르는 중')

    #마우스 이동 할때 발생
    elif event == cv2.EVENT_MOUSEMOVE:

        #누르고 이동하면 사각형 그림
        if mouse_is_pressing:
            cv2.rectangle(img_result, (start_x, start_y), (x, y), (0, 255, 0), 3)
            cv2.imshow("Test", img_result)

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_is_pressing = False

        end_x = x
        end_y = y
        #버튼때면 사각형 영역의 Grayscale 이미지 새로 만들기
        roi = image[start_y:y, start_x:x]
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Test", img_result)
        cv2.imshow("Roi", roi)



        return (start_y,y, start_x,x)


vid = cv2.VideoCapture('./img/digit2.mp4')


ret, image =vid.read(0)


#2. 마우스 이벤트 감지할 윈도우 설
cv2.namedWindow('Test')

#3. 마우스 이벤트 감지하면 함수 실행
cv2.setMouseCallback('Test',Mouse_callback)

cv2.imshow('Test',image)
cv2.waitKey(0)

cv2.destroyAllWindows()

n_frame = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

for i in range(n_frame):
   ret, frame =vid.read()

   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   blurred = cv2.GaussianBlur(gray, (5, 5), 0)
   thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)[1]
   #edged = cv2.Canny(blurred, 50, 200, 255)

   result = thresh[start_y:end_y, start_x:end_x]

   cv2.imshow('Result',result)
   cv2.waitKey(30)





