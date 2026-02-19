 # Purana version hata kar naya 'bullseye' version use karein
FROM python:3.9-slim-bullseye

# System update aur git install ek saath (Best practice)
RUN apt-get update && apt-get upgrade -y && apt-get install git -y

COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /fwdbot
WORKDIR /fwdbot
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
