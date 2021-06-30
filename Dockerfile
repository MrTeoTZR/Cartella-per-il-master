FROM python:slim-buster
RUN mkdir -p /home/materiale/results && chmod -R 777 /home/materiale
COPY requirements.txt main.py /home
WORKDIR /home
RUN pip install -r requirements.txt
RUN rm requirements.txt
ENTRYPOINT ["python","main.py"]


