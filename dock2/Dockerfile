FROM python:3.8-alpine
COPY ./reqs.txt /app/reqs.txt
WORKDIR /app
RUN pip install -r reqs.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]
 