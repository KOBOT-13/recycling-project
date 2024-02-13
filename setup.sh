VENV_DIR=venv

pip install -r requirements.txt

cp -f ./detect.py $VENV_DIR/lib/python3.11/site-packages/yolov5/detect.py

