# MediaPipe_Hand-Tracking_Computer-Interaction
Source code that uses the Media Pipe library to interact with your computer with real-time streaming images through finger gestures.  
Media Pipe 라이브러리를 사용하여 손가락 제스처를 통해 실시간 스트리밍 이미지로 컴퓨터와 상호 작용하는 소스 코드입니다.


# Getting Started
1. The software below must be pre-installed prior to running the project.  
해당 프로젝트를 실행하기 전에 아래 소프트웨어를 사전적으로 설치해야 합니다.  

> * Install PyCham IDE (Recommended latest version)  
> 파이참IDE 설치 (최신 버전 권장)  
> https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows
> * Install Python (3.10 version recommended)  
> 파이썬 설치 (3.10 버전 권장)  
> https://www.python.org/downloads/  
> * Chrome Installation (Recommended Latest Version)  
> 크롬 설치 (최신 버전 권장)  
> https://www.google.co.kr/intl/ko/chrome/  

2. When you have finished installing the software, install and connect a webcam to your computer.  
소프트웨어 설치가 끝났다면, 사용자 컴퓨터에 웹캠을 설치 및 연결합니다.  

3. Download the project file on the GitHub.  
깃 허브에 있는 프로젝트 파일을 다운로드 받습니다.  

4. Load the project file after running Python.  
파이참을 실행한 후 프로젝트 파일을 불러옵니다.

5. After that, the interpreter is set.  
그 이후 인터프리터를 설정한다.  
[File] - [Setting] - [Python Interpreter] - [Add Interpreter] - [Add Local Interpreter] - [Virtualenv Environment] - [OK] - [OK]  


<img src="https://user-images.githubusercontent.com/62827269/208565717-d5d7ee78-eeb3-4f3d-8610-c13b90008448.png" width="70%" height="70%"/>

<img src="https://user-images.githubusercontent.com/62827269/208566673-b9b63781-2401-4e40-9a26-f8222e7215d2.png" width="70%" height="70%"/>

6. Press the [alt] + [Ins] key to install the following package files:  
[alt] + [Ins] 키를 눌러 다음 패키지 파일을 설치합니다.  
<img src="https://user-images.githubusercontent.com/62827269/208567264-38d6a791-e338-4364-b768-3cf08bc28d83.png" width="70%" height="70%"/>   

> ```python
> 1. cvzone
> 2. mediapipe
> 3. selenium
> 4. pynput
> 5. pygetwindow
> 6. pyautogui
>```
After installation, press [OK] to return to the main screen.  
설치 이후 [OK]를 눌러 메인 화면으로 돌아갑니다.  

7. Then set the drive interpreter.  
그 다음 구동 인터프리터를 설정합니다.  
<img src="https://user-images.githubusercontent.com/62827269/208568516-ca98145a-620a-4d09-92f6-9598ca6a6287.png" width="70%" height="70%"/>   
우측 상단(Upper right) [Current File] - [Edit Configurations] - [Add New Configurations] - [Python] - [Unnamed] - [Script path] - main.py - [OK]  
  

8. You can now press the drive button to run the program.  
Top right play button or [Shift] + [F10]  
이제 구동 버튼을 눌러 프로그램을 실행할 수 있습니다.  
우측 상단 재생 버튼 혹은 [Shift] + [F10]  

# User's Manual
> * **신축(stretch)**   
> ![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/62827269/208485978-5c9ad4e4-9e21-46ee-8758-0069970d3b01.gif)  
> If you open or close both arms after only pulling out the thumb and index finger of both hands,  
> the camera moves in the direction of the object to zoom in and out.  
> 양손의 엄지 손가락과 검지 손가락만 핀 후 양팔을 벌리거나 오므리면 객체 방향으로 카메라가 움직여 확대 및 축소 됩니다.    
> * **회전(Rotation)**  
> ![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/62827269/208490553-43013336-c76a-4c92-a0e2-a609f4e3dc56.gif)  
> If you move your hand after only pulling out your thumb, the camera rotates according to the direction you moved.  
> 엄지 손가락만 핀 후 손을 움직이면, 움직인 방향에 따라 카메라가 회전 합니다.  
>  * **전환(Switch tabs)**   
> ![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/62827269/208494561-9fff82ff-0a60-4907-89cc-07fc22d3a090.gif)  
> You can switch tabs in your web browser depending on the direction of your thumb or fingers.  
>  If the next tab is missing, it switches to the first or last tab.  
>  엄지 손가락 혹은 소지 손가락만 피면, 손가락 방향에 따라 웹브라우저의 탭 전환이 가능합니다.  
>  다음 탭이 없으면 첫 번째 혹은 마지막 탭으로 전환됩니다.  


# Help me!
Various situations can cause errors when running the program.  
프로그램 실행 시 여러 가지 상황으로 인해 오류가 발생할 수 있습니다.  
1. 크롬 브라우저의 드라이버 버전 문제
> 해당 문제가 발생한 경우, 프로젝트 파일 내부에 크롬 드라이버를 업로드해야 합니다. 
>  
> 1-1. 먼저, 사용자 컴퓨터에 크롬이 설치되어 있는지 확인해 보세요.  
> 
> 1-2. 다음 링크를 통해 사용자 컴퓨터의 크롬 브라우저 버전에 맞는 크롬 드라이버를 설치합니다.
> https://chromedriver.chromium.org/downloads  
> 
> 1-3. 크롬 브라우저 버전 확인 방법은 크롬 브라우저 주소창에 chrome://version을 입력하여 확인해 볼 수 있습니다.  
> 예를 들어, 108.0.5359.125 버전의 크롬 브라우저의 경우 108.0.5359.XXX 버전을 크롬 드라이버를 설치하면 됩니다.  
> 
> 1-4. 그 이후, 프로젝트 파일 내부에 업로드 후 실행하면 됩니다.

2. 사용되는 라이브러리 버전 문제
> 사용되는 파이썬 인터프리터 내부에 있는 라이브러리 버전 문제로 인한 오류가 발생할 수 있습니다.  
> 새로운 인터프리터로 변경하신 후 다음 라이브러리를 순서대로 설치해 보세요.
> [파일] - [Python 인터프리터]
> ```python
> 1. cvzone
> 2. mediapipe
> 3. selenium
> 4. pynput
> 5. pygetwindow
> 6. pyautogui
3. 웹캠 연결이 안된 상태
> 먼저, 웹캠이 정상적으로 연결되어 있는지 확인해 보세요.
> 그래도 안된다면, 프로젝트 파일에 있는 소스 코드를 다음과 같이 수정하세요.  
> 관련 속성은 다음 [OpenCV 웹페이지에서 확인해 볼 수 있습니다.](https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#ga023786be1ee68a9105bf2e48c700294d)
> ```python
> cap = cv2.VideoCapture(0) or
> cap = cv2.VideoCapture(1)
4. 프로그램이 정상적으로 실행 가능하나 핸드 트레킹이 안되는 문제 혹은 상호 작용에 대한 문제  
> 프로그램 오작동 방지로 인해 상호 작용이 안될 수 있습니다.  
> 크롬 웹브라우저를 클릭하여 활성화한 후 다시 시도해 보세요.  
> 프로그램이 정상적으로 작동한다면, 영상 스트림 출력창에 "Setting" 값이 True 상태이어야 합니다.  
> 혹은 상호 작용이 제대로 안될 경우 카메라 부터 손의 위치를 가깝게 혹은 조금 멀리 떨어져서 시도해 보세요.  



# Reference
Depending on the distance between the camera and the hand, the accuracy may decrease slightly  
There is a possibility that the program will not run normally when more than one hand is detected or in hand movements similar to the   
event gesture in addition to that manual.  
카메라와 손의 거리에 따라서, 정확도가 다소 떨어질 수 있으며, 두 사람 이상의 손이 검출되거나 해당 메뉴얼 외에   
이벤트 제스처와 유사한 손 동작 상태에서는 정상적으로 프로그램이 구동되지 않을 가능성이 있습니다.

