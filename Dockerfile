FROM python:3.9-bullseye as builder

COPY . /app
WORKDIR /app

# update ubuntu and pip with essential build packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# set up docker file to use a virtual environment
# https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN which python

COPY buildserver/app.py .
CMD ["flask", "run"]
