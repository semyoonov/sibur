FROM python:3.12

COPY . /sibur
WORKDIR /sibur
RUN pip install --no-cache -r requirements.txt

ENTRYPOINT ["python", "/sibur/refresh.py"]
