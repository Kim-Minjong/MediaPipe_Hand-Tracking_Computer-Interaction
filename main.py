"""
MIT License

Copyright (c) 2022 Kim-Minjong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

MIT 라이선스

저작권 (c) 2022 김민종

본 소프트웨어 및 관련 문서 파일(이하 "소프트웨어")의 사본을 입수하는 모든 사람에게 소프트웨어를 제한 없이 거래할 수 있는 권한이 부여되며,
여기에는 소프트웨어의 사용, 복사, 수정, 병합, 게시, 배포, 하위 라이센스 및 / 또는 판매 권한이 포함됩니다.
다음 조건에 따라 소프트웨어가 제공되는 경우:

위의 저작권 고지 및 이 허가 고지는 소프트웨어의 모든 사본 또는 상당 부분에 포함되어야 합니다.

소프트웨어는 상품성, 특정 목적에 대한 적합성 및 비침해에 대한 보증을 포함하지만 이에 국한되지 않는 어떠한 종류의 명시적 또는 묵시적 보증도 없이 "있는 그대로" 제공됩니다.
저작자 또는 저작권 소유자는 계약, 불법 행위 또는 기타 행위에 관계없이 소프트웨어 또는 소프트웨어의 사용 또는 기타 거래로 인해 발생하는 모든 청구, 손해 또는 기타 책임에 대해 책임을 집니다.
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
from selenium import webdriver
from pynput.mouse import Button, Controller
import time
import numpy as np
import pygetwindow as gw
import pyautogui


"""
Initialize and load the link to run in your web browser.

웹 브라우저에서 실행할 링크를 초기화한 후 불러옵니다.
"""

#Get URL List
driver.get('https://sketchfab.com/models/2620f4a0e6cf456d84e3601eb77f090f/embed?autostart=1&internal=1&tracking=0&ui_infos=0&ui_snapshots=1&ui_stop=0&ui_watermark=0')
tabs = driver.window_handles
tabs_index = 0
driver.switch_to.window(tabs[tabs_index])


"""
Insert the code if you want the full screen mode of your web browser.

웹 브라우저의 전체화면 모드를 원할 경우 해당 코드를 삽입합니다.

"""


cap = cv2.VideoCapture(1)
width = 1280
height = 720

cap.set(7, width)
cap.set(9, height)


""""
Hand tracking Initialize functions and variables used.

핸드 트래킹 사용되는 함수 및 변수 초기화.
"""
detector = HandDetector(detectionCon=1.5)
startDist = None
scale_gap_value = 0
pTime = 0
scale = 0



"""
Run a program
프로그램 구동
"""
while True:
    # Program Stress Measurement
    # While 반복문 실행 시간 측정 - Start Point (스트레스 측정)
    startTime = time.time()

    # Webcam streaming image output and hand tracking Initialize the functions and variables used
    # 웹캠 스트리밍 영상 출력 및 핸드 트래킹 사용되는 함수 및 변수 초기화
    success, img = cap.read()
    hands, img = detector.findHands(img)
    old_time = scale


    # Initialize mouse control related functions
    # 마우스 제어 관련 함수 초기화
    mouse = Controller()


    # Initialize whether hand tracking readiness
    # 핸드 트래킹 준비 상태 확인 여부 초기화
    execution = False

    if hands:
        execution = True
        """
        신축(stretch)
        the camera moves in the direction of the object to zoom in and out.  
        양손의 엄지 손가락과 검지 손가락만 핀 후 양팔을 벌리거나 오므리면 객체 방향으로 카메라가 움직여 확대 및 축소 됩니다.   
        """
        if len(hands) == 2:
            if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and \
                detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
                    if startDist is None:
                        length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                        startDist = length
                        length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                        scale = int((length - startDist) // 2)
                    else:
                        startDist = None
                # Left hand event gesture
                # 왼손 이벤트 제스처
                for hand in hands:
                    if hand["type"] == "Left":
                        lmList = hand["lmList"]
                        fingers = detector.fingersUp(hand)

                        # 1차원 선형 보간 (interpolation)
                        xVal = int(np.interp(lmList[8][0], [0, width], [0, width]))
                        yVal = int(np.interp(lmList[8][1], [0, height], [0, height]))
                        indexFinger = xVal, yVal

                        """
                        회전(Rotation)
                        The resolution of the image stream and the size of the web browser are different
                        The process of controlling the mouse after converting the two-dimensional position data of the index finger detected in the image stream proportionally to the frame size ratio of the Chrome web browser.
                        영상 스트림의 해상도와 웹 브라우저의 크기가 다르므로,
                        영상 스트림에 검출된 검지 손가락의 2차원 위치 데이터를 크롬 웹 브라우저의 프레임 크기 비율에 맞게 비례하여 변환한 후 마우스를 제어하는 과정.
                        """
                        if fingers == [0, 1, 0, 0, 0]:
                            mouse.press(Button.left)
                            mouse.position = (xVal, yVal)
                            weighte["move"] += 1
                            log.append('move')
                            log_cnt += 1
                        else:
                            mouse.release(Button.left)

                        """
                        다음 탭 전환(Switch Next Tab)
                        If there is no tab to move on, go to the first tab.
                        다음으로 넘어갈 탭이 없다면, 첫번째 탭으로 이동한다.
                        """
                        if fingers == [0, 0, 0, 0, 1]:
                            weighte["next"] += 1
                            if weighte_Cnt == maximum:
                                if weighte["next"] >= maximum * 0.8:

                                    if tabs_index == len(tabs) - 1:
                                        tabs_index = 0
                                        driver.switch_to.window(tabs[tabs_index])
                                    else:
                                        tabs_index += 1
                                        driver.switch_to.window(tabs[tabs_index])

                    # Right hand event gesture
                    # 오른손 이벤트 제스처
                    # The following description is omitted because it is the same as the left-hand event gesture algorithm
                    # 왼손 이벤트 제스처 알고리즘과 같으므로 다음 설명은 이하 생략
                    if hand["type"] == "Right":
                        lmList = hand["lmList"]
                        fingers = detector.fingersUp(hand)

                        WinSizeX, WinSizeY = driver.get_window_size().values()
                        WinPosX, WinPosY = driver.get_window_position().values()

                        xVal = int(np.interp(lmList[8][0], [0, width], [0, width]))
                        yVal = int(np.interp(lmList[8][1], [0, height], [0, height]))
                        indexFinger = xVal, yVal


                        if fingers == [0, 1, 0, 0, 0]:
                            mouse.press(Button.left)
                            mouse.position = (WinPosX + (xVal * (WinSizeX / width)), WinPosY + (yVal * (WinSizeY / height)))
                            weighte["move"] += 1

                        else:
                            mouse.release(Button.left)


                        if fingers == [0, 0, 0, 0, 1]:
                            weighte["next"] += 1
                            if weighte_Cnt == maximum:
                                if weighte["next"] >= maximum * 0.8:
                                    log.append('next')

                                    if tabs_index == 0:
                                        tabs_index = len(tabs) - 1
                                        driver.switch_to.window(tabs[tabs_index])
                                    else:
                                        tabs_index -= 1
                                        driver.switch_to.window(tabs[tabs_index])

    """
    신축(stretch) - 상호 작용 단계(Interaction Steps)
    두 손의 거리가 측정된 데이터를 활용하여 이전에 실행된 데이터 값과 대조해 오차 범위에 따라 확대 및 축소 가동 범위 조절
     Leverage measured two-hand distance data to match previously executed data values to adjust the range of operations for magnification and contraction according to the error range of error
    """
    try:
        time_now = scale
        scale_gap_value = time_now - old_time

        if scale_gap_value != 0:
            mouse.scroll(0, 0.03 * scale_gap_value)
    except:
        pass


    weighte_Cnt = 0

    # Image Stream FPS Measurements - Performance and Load Testing
    # 영상 스트림 FPS 측정 - 성능 및 부하 테스트
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Output fps to the image stream
    # 영상 스트림에 fps 출력
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
    # Hand tracking readiness check output
    # 핸드 트래킹 준비 상태 확인 여부 출력
    cv2.putText(img, f'Setting: {bool(execution)}', (20, 150), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
    # 영상 스트림 출력(Image stream output)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


    # While 반복문 실행 시간 측정 - End Point
    EndTime = time.time() - startTime
    print(EndTime)


