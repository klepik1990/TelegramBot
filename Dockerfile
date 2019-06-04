FROM ubuntu
RUN apt-get update \
	&& apt-get -y upgrade \ 
	&& apt-get install -y python3 python-pip git
ADD . /telegrambot 
RUN git clone https://github.com/klepik1990/TelegramBot.git \
	&& cd /TelegramBot \
	&& pip install -r /TelegramBot/requirements.txt \
	&& ls -l
ENV HOME ~/TelegramBot
WORKDIR ~/TelegramBot
EXPOSE 5000
CMD ["python", "//TelegramBot/TelegramBot.py"]


