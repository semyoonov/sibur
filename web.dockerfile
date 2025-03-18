FROM python:3.12

COPY . /sibur
WORKDIR /sibur
RUN pip install --no-cache -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "/sibur/main.py"]
