FROM python:3.4-alpine
ADD . /app
WORKDIR /app
RUN mkdir /data
RUN pip3 install flask
CMD ["python3", "writeFile.py"]
