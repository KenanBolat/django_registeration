FROM python:3.9
LABEL maintainer='Kenan BOLAT'

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /tmp/requirements.txt
#COPY ./requirements.dev.txt /tmp/requirements.dev.txt
#COPY ./auth_service/sqlite3.db /auth_service/sqlite3.db
COPY ./scripts/run.sh /scripts/run.sh
WORKDIR /auth_service
COPY . .
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update && apt-get install apt-utils acme -y && \
    apt-get install libgl1 libpq-dev -y && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol/* && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts/* && \
    chown -R django-user:django-user /scripts/*
#

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

#CMD ["run.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
