FROM ubuntu:latest


RUN apt-get update 
RUN apt-get install -y python3-pip python3-dev
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN cd /usr/local/bin
RUN ln -s /usr/bin/python3 python
RUN pip3 install --upgrade pip
		


WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]




