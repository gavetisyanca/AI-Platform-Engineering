FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app
RUN pi3 --no-cache-dir install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]