FROM python:3.11-slim
RUN mkdir -p /srv/mces
WORKDIR /srv/mces
RUN python -m pip install --upgrade pip
COPY Pipfile Pipfile.lock /srv/mces/
RUN pip install pipenv
RUN pipenv install --system
EXPOSE ${APP_PORT}
ENTRYPOINT ["sh","entrypoint.sh"]