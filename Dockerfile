FROM python:3.8-alpine
RUN apk add --no-cache build-base zlib-dev jpeg-dev freetype-dev

WORKDIR /app
ENV HOME=/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY pyxo pyxo
COPY library library
COPY setup.py wsgi.py ./

RUN chown -R nobody:nobody ${HOME}
USER nobody:nobody

EXPOSE 8000
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0", "--preload"]
