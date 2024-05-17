FROM python:3.11-alpine
RUN apk add --no-cache bash
RUN apk add gcc musl-dev mariadb-connector-c-dev
COPY backend_despacho backend_despacho
RUN pip install -r /backend_despacho/requirements.txt
EXPOSE 8000