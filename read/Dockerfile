FROM python:3.4-alpine
RUN pip3 install flask
ADD . /app
WORKDIR /app
RUN mkdir /data
CMD ["python3", "readFile.py"]
