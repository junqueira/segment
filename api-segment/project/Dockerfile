FROM python:3.5

RUN mkdir -p /opt/app
WORKDIR /opt/app

ENV TZ 'America/Sao_Paulo'
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get -y update && apt-get -y install awscli
#RUN apt-get install awscli libmemcached-dev -y

# This command requires AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to be
# present in the environment variables.
#ENV AWS_ACCESS_KEY_ID AWS_ACCESS_KEY_ID
#ENV AWS_SECRET_ACCESS_KEY AWS_SECRET_ACCESS_KEY

ADD . /opt/app
ADD requirements.txt /opt/app/requirements.txt
RUN pip install -r /opt/app/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8082"]