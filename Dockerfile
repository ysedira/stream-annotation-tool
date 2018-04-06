FROM ubuntu:17.10

# -- Install Pipenv:
RUN apt-get update \
  && apt-get install software-properties-common python-software-properties -y \
  && add-apt-repository ppa:pypa/ppa -y \
  && apt-get update \
  && apt-get install git pipenv nodejs npm -y
RUN node --version
RUN npm --version
RUN npm install -g @angular/cli

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# -- Install Application into container:
RUN set -ex && mkdir /app

WORKDIR /app


RUN git clone https://github.com/ysedira/stream-annotation-tool.git /app 


RUN cd /app/client \
    && npm install \
    && ng build --prod --env=prod -bh /static --deploy-url /static

ENV FLASK_ENV="docker"
EXPOSE 5000
# -- Install dependencies:
RUN cd /app
RUN pipenv install --deploy --system
RUN source `pipenv --venv`/bin/activate
CMD python /app/server/sat/app.py


