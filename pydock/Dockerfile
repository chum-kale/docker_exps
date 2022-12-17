FROM python:3.7-alpine
WORKDIR /pydock
ENV FLASK_APP=pythonxdocker.py
ENV FLASK_APP=code2.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]