# recycling-project Setup 문서

### 요구사항
* Python 3.11.2
* Raspberry Pi 4 Model B
* Raspberry Pi OS 64bit

### 가상환경 세팅
```bash
virtualenv venv
```
또는
```bash
python -m venv venv
```
명령어를 활용하여 가상환경을 만들어 줍니다.

```bash
source venv/bin/activate
```
명령어를 활용하여 가상환경을 활성화 시켜줍니다.

### 의존성 패키지 설치
```bash
pip install -r requirements.txt
```
requirements.txt를 활용하여 의존성 패키지를 설치하여 줍니다.

마지막으로 /venv/lib/python3.11/site-packages/yolov5/detect.py 내부 폴더를 detect.py의 내용으로 대체합니다.
