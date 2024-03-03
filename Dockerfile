FROM python:3.12
WORKDIR /app
RUN ls /app
COPY . /app
RUN ls /app
VOLUME /app
RUN mkdir /usr/local/share/logs
RUN apt-get update
RUN apt-get -y install git
RUN pip install --upgrade pip
RUN pip install -e .
RUN ls /app
RUN pip install -r requirements.txt
ENTRYPOINT []
CMD ["python", "my_application.__main__.py", "tail", "-f", "/dev/null"]