FROM python:3.6.6-alpine

MAINTAINER sean2525<madness48596@gmail.com>

EXPOSE 80

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

CMD ["python3", "app.py", "--port", "80"]
