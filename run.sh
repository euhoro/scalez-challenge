virtualenv venv-scalez --python=python3
. venv-scalez/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=flask_end_point
flask run