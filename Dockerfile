FROM python:3.8-alpine
RUN apk add --update build-base zlib-dev jpeg-dev freetype-dev

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY pyxo pyxo
COPY library library
COPY wsgi.py ./

RUN chown -R nobody: /app
USER nobody

ENV HOME=/app

EXPOSE 8000
CMD gunicorn wsgi:app -b 0.0.0.0 --preload
