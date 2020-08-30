FROM ubuntu:16.04 
COPY . ./code
WORKDIR ./code
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev
RUN apt-get install -y git
RUN pip3 install -r requirements.txt
RUN export GIT_PYTHON_REFRESH=quiet
ENTRYPOINT [ "python3" ]
CMD [ "src/main.py" ]
