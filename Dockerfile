FROM python:3.5-alpine
ADD src /src
WORKDIR /src
RUN apk update && apk add build-base mysql-dev python3-dev
RUN pip install -r requirements.txt
CMD ["sh", "run.sh"]
