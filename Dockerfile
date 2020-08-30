FROM python:latest
WORKDIR ./code
COPY . ./code
RUN pip install -r ./requirements.txt
EXPOSE 80
CMD ["python", "src/main.py"]