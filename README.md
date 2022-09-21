python -m venv fstapi
source fstapi/bin/activate
(fstapi) code .
python -r install requirements.tx
uvicorn main:app --reload
http://127.0.0.1:8000/docs
