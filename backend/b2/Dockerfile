FROM python:3.9-alpine
WORKDIR /usr/src/app/
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN /opt/venv/bin/python3 -m pip install --upgrade pip
COPY app-b2.py ./
RUN pip install flask
ENTRYPOINT ["flask","run","-p","80","--host=0.0.0.0"]
