FROM python:3.10-alpine

LABEL maintainer=clooooode<jackey8616@gmail.com>

EXPOSE 8090

WORKDIR /app

COPY . .

RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		make \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements.txt; \
	apk del .build-deps;

CMD ["python3", "app.py", "--port", "8090"]
