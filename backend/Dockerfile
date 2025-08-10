FROM python:3.12.11-bookworm
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
# RUN chmod +x build.sh
# build.sh を実行
RUN ./build.sh
RUN 