FROM python:alpine

# copy the requirements file
COPY ./requirements.txt .

# setup the virtualenv and create the user flask
RUN python -m venv flaskvenv \
  && /flaskvenv/bin/pip install --no-cache-dir -r /requirements.txt \
  && rm requirements.txt \
  && adduser -D flask

# copy over the application
COPY ./src /home/flask/src

# tighten the permissions for the flask user
RUN chown -Rv flask:nogroup /home/flask \
  && chmod -Rv 500 /home/flask

# set up the execution
USER flask
WORKDIR /home/flask/src
ENV FLASK_APP=app.py
CMD ["/flaskvenv/bin/flask", "run"]
