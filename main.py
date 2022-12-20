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

"""
Project Overview
This open source uses the Media Pipe Library and the Opencv Library to track the hands of webcam streaming videos
Create a 3D virtual environment through WebGL with finger gestures
It's the source code that interacts with a three-dimensional model

If you have any questions, please contact us via email.
minjong4654@naver.com

프로젝트 개요
이 오픈 소스는 Media Pipe Library와 Opencv Library를 사용하여 웹캠 스트리밍 비디오의 손을 추적합니다.
손가락 제스처로 WebGL을 통해 3D 가상 환경 생성
3차원 모델과 상호작용하는 소스 코드입니다.

문의 사항이 있으시면 이메일로 문의해주세요.
minjong4654@naver.com
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
Initialize the options before loading a web browser.
This code disables the "Chrome is controlled by automated test software" output on the top alarm panel when the web browser is launched.

웹 브라우저를 불러오기 전 해당 옵션을 초기화합니다.
해당 코드는 웹 브라우저 실행 시 상단부 알람 패널에 "Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다." 출력되는 기능을 해제합니다.
"""
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)



"""
Initialize and load the link to run in your web browser.

웹 브라우저에서 실행할 링크를 초기화한 후 불러옵니다.
"""

#Get URL List
driver.get('https://sketchfab.com/models/2620f4a0e6cf456d84e3601eb77f090f/embed?autostart=1&internal=1&tracking=0&ui_infos=0&ui_snapshots=1&ui_stop=0&ui_watermark=0')
driver.execute_script('window.open("https://sketchfab.com/models/f9d97a3fffea46eb91f8c297f54b1888/embed?autostart=1&internal=1&tracking=0&ui_infos=0&ui_snapshots=1&ui_stop=0&ui_watermark=0");')
driver.execute_script(('window.open("https://sketchfab.com/models/64b73a627edd467fbf2b193112831ab0/embed?autostart=1&internal=1&tracking=0&ui_infos=0&ui_snapshots=1&ui_stop=0&ui_watermark=0");'))
tabs = driver.window_handles
tabs_index = 0
driver.switch_to.window(tabs[tabs_index])


"""
Insert the code if you want the full screen mode of your web browser.

웹 브라우저의 전체화면 모드를 원할 경우 해당 코드를 삽입합니다.

#pyautogui.press('f11')
"""



"""
Run the camera.cv.VideoCapture(prodID)
prodID number > 0:Integrated camera, 1:USB-connected external camera
If the program does not work properly after connecting the camera, try changing the value of the prodID.
Class Reference: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html

카메라를 실행합니다.cv.VideoCapture(prodID)
prodID number > 0:내장 카메라 , 1:USB-연결 외장 카메라
카메라 연결 후 프로그램이 정상적으로 작동이 안되면, prodID의 값을 바꿔볼 것.
클래스 참조: https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html
"""
cap = cv2.VideoCapture(0)

"""
#camera initialization cap.set (ID, resolution), ID> 3:horizontal resolution, 4:vertical resolution 5:FPS
#See class: https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get

#카메라 초기 설정 cap.set(ID, 해상도), ID > 3:가로 해상도, 4:세로 해상도 5:FPS
#클래스 참조: https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get
"""
width = 1280
height = 720

cap.set(3, width)
cap.set(4, height)

"""
Determined if the camera is connected.
cv2.If the camera fails to connect to the corresponding ID in VideoCapture(), exit the program.

카메라 연결 여부 확인
cv2.VideoCapture()의 해당 ID에 카메라를 연결하지 못하면, 프로그램을 종료.
"""

if not(cap.isOpened()):
    print('\n' + '\033[31m' + "[Error].Camera not found.")
    print("Connect a camera or change the input of the 'cv2.VideoCapture()' function to 0 or 1.")
    print("Terminates the program as it cannot find a camera. please try again.")
    print('\n' + "[오류].카메라를 찾을 수 없습니다.")
    print("카메라를 PC에 연결해 주세요. 그래도 문제가 발생하면, 'cv2.VideoCapture()' 함수의 매개변수 값을 0 혹은 1로 변경하세요.")
    print("해당 문제로 인해 프로그램을 강제 종료합니다.")
    exit()
else:
    print('\033[32m' + "카메라 연결 완료." + '\033[97m')

""""
Hand tracking Initialize functions and variables used.

핸드 트래킹 사용되는 함수 및 변수 초기화.
"""
detector = HandDetector(detectionCon=0.75)
startDist = None
scale_gap_value = 0
pTime = 0
scale = 0

"""
Initialization of hand motion 'weight' using dictionary {Dictionary}

딕셔너리{Dictionary}를 이용한 손 동작 'weighte(가중치)' 초기화.
"""
weighte = {"size": 0, "move": 0, "back": 0, "next": 0}
weighte_Log = {"log": None, "time":0}
weighte_Cnt = 0
maximum = 10
log = []
log_cnt = 0


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


    """
    Initialization of 'weighte' using dictionary {Dictionary}.
    If the command is repeated more than 10 times, initialize 'weighte'.
    If a particular hand gesture has 80% accuracy over 10 command iterations, it executes the event.
    
    딕셔너리{Dictionary}를 이용한 'weighte(가중치)' 초기화.
    명령어 반복한 횟수가 10번이 넘으면 'weighte(가중치)' 초기화 한다.
    특정 손 제스처가 10번의 명령어 반복 횟수 동안 80%의 정확도를 가지면, 해당 이벤트를 실행합니다.
    """
    for value in weighte.values():
        weighte_Cnt += value
    if weighte_Cnt > maximum:
        weighte = {"size": 0, "move": 0, "back": 0, "next": 0}

    # Logs events executed through the event gesture.
    # 이벤트 제스처를 통해 실행된 이벤트를 기록합니다.
    while True:
        if len(log) >= 55:
            del log[0]
        else:
            break

    weighte_Log["log"] = log

    # Initialize mouse control related functions
    # 마우스 제어 관련 함수 초기화
    mouse = Controller()

    """
    Initialize active Windows titles and Chrome Web browser titles.
    Only when Chrome Web Browser is enabled, hand tracking is enabled.
    
    활성화된 윈도우 타이틀과 크롬 웹 브라우저 타이틀 초기화.
    크롬 웹 브라우저가 활성화된 상태에서만, 핸드 트래킹 활성화.
    """
    winTitle = gw.getActiveWindowTitle()
    driver_title = driver.title + " - Chrome"

    """
    Get web browser resolution/location information and initialize it to that variable.
    The process of proactively preventing the mouse pointer from leaving the Chrome web browser frame.
    
    웹 브라우저 해상도/위치 정보 가져온 후 해당 변수에 초기화.
    마우스 포인터가 크롬 웹 브라우저 프레임 밖으로 나가는 것을 미연에 방지하는 과정.
    """
    WinSizeX, WinSizeY = driver.get_window_size().values()
    WinPosX, WinPosY = driver.get_window_position().values()

    # Initialize whether hand tracking readiness
    # 핸드 트래킹 준비 상태 확인 여부 초기화
    execution = False


    """
    Conditional statements to prevent software malfunction before computer interaction
    1. Has the user's hand been detected in the image stream?
    2. Is the currently active window Chrome web browser correct?
    3.Is the mouse pointer in the Chrome web browser frame?

    컴퓨터 상호작용 전 사전에 소프트웨어 오작동을 방지하기 위한 조건문
    1.영상 스트림에 사용자의 손이 검출되었는가?
    2.현재 활성화된 윈도우 창이 크롬 웹 브라우저가 맞는가?
    3.마우스 포인터가 크롬 웹 브라우저 프레임 안에 있는가?
    """
    if hands:

        if winTitle == driver_title:

            if WinPosX <= pyautogui.position().x and WinPosX + WinSizeX >= pyautogui.position().x and \
                    WinPosY <= pyautogui.position().y and WinPosY + WinSizeY >= pyautogui.position().y:

                execution = True

                """
                신축(stretch)
                the camera moves in the direction of the object to zoom in and out.  
                양손의 엄지 손가락과 검지 손가락만 핀 후 양팔을 벌리거나 오므리면 객체 방향으로 카메라가 움직여 확대 및 축소 됩니다.   
                """
                if len(hands) == 2:
                    if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and \
                            detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:

                        # Measure the distance of both hands relative to the center of the bounding box where the hand is detected.
                        # 손이 검출된 바운딩 박스 정중앙을 기준으로 양손의 거리 측정
                        if startDist is None:
                            length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                            startDist = length
                        length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                        scale = int((length - startDist) // 2)

                        weighte["size"] += 1
                        log.append('size')
                        log_cnt += 1
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
                            mouse.position = (WinPosX + (xVal * (WinSizeX / width)), WinPosY + (yVal * (WinSizeY / height)))
                            weighte["move"] += 1
                            log.append('move')
                            log_cnt += 1
                        else:
                            mouse.release(Button.left)

                        """
                        이전 탭 전환(Switch Previous Tabs)
                        If there is no tab to move on, go to the last tab.
                        다음으로 넘어갈 탭이 없다면, 마지막 탭으로 이동한다.
                        
                        trillion
                        #Thumb 2nd joint and thumb tip Y axis length is more than 95 pixels long,
                        #Thumb 2nd joint and thumb tip X axis height not more than 75 pixels high
                        #The thumb end Y axis must be lower than the index finger first joint Y axis.
                        
                        조건
                        #엄지 두번째 관절과 엄지 끝 Y축 길이가 95 픽셀 이상,
                        #엄지 두번째 관절과 엄지 끝 X축 높이가 75 픽셀 이하
                        #엄지 끝 Y축이 검지 첫번째 관절 Y축 보다 낮아야 한다.
                        """
                        if lmList[2][0]-lmList[4][0] >= 95 and lmList[2][1]-lmList[4][1] <= 75 and \
                                lmList[4][1] > lmList[5][1] and fingers == [1, 0, 0, 0, 0]:
                            weighte["back"] += 1
                            if weighte_Cnt == maximum:
                                if weighte["back"] >= maximum * 0.8:
                                    log.append('back')
                                    log_cnt += 1

                                    if tabs_index == 0:
                                        tabs_index = len(tabs) - 1
                                        driver.switch_to.window(tabs[tabs_index])
                                    else:
                                        tabs_index -= 1
                                        driver.switch_to.window(tabs[tabs_index])

                        """
                        다음 탭 전환(Switch Next Tab)
                        If there is no tab to move on, go to the first tab.
                        다음으로 넘어갈 탭이 없다면, 첫번째 탭으로 이동한다.
                        """
                        if fingers == [0, 0, 0, 0, 1]:
                            weighte["next"] += 1
                            if weighte_Cnt == maximum:
                                if weighte["next"] >= maximum * 0.8:
                                    log.append('next')
                                    log_cnt += 1

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
                            log.append('move')
                            log_cnt += 1
                        else:
                            mouse.release(Button.left)

                        if lmList[4][0] - lmList[2][0] >= 95 and lmList[2][1] - lmList[4][1] <= 75 and \
                                lmList[4][1] > lmList[5][1] and fingers == [1, 0, 0, 0, 0]:
                            weighte["back"] += 1
                            if weighte_Cnt == maximum:
                                if weighte["back"] >= maximum * 0.8:
                                    log.append('back')
                                    log_cnt += 1

                                    if tabs_index == len(tabs) - 1:
                                        tabs_index = 0
                                        driver.switch_to.window(tabs[tabs_index])
                                    else:
                                        tabs_index += 1
                                        driver.switch_to.window(tabs[tabs_index])

                        if fingers == [0, 0, 0, 0, 1]:
                            weighte["next"] += 1
                            if weighte_Cnt == maximum:
                                if weighte["next"] >= maximum * 0.8:
                                    log.append('next')
                                    log_cnt += 1


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


