FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

#RUN apt-get update \
# && apt-get install -y --no-install-recommends \
#    build-essential

RUN pip install --upgrade pip

ADD requirements.txt /usr/src/app
RUN pip install -r requirements.txt


COPY . /usr/src/app
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

