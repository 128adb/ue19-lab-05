FROM python:3.12.3

WORKDIR /home/user

COPY app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
