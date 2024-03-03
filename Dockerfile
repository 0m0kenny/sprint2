FROM python:3.12
WORKDIR /app
VOLUME /app
RUN mkdir /usr/local/share/logs
RUN apt-get update
RUN apt-get -y install git
RUN pip install --upgrade pip
RUN pip install -e .
RUN pip install requirements.txt
ENTRYPOINT []
CMD ["python", "__main__.py", "tail", "-f", "/dev/null"]