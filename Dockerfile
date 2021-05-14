FROM julianbei/alpine-opencv-microimage:p3-3.1

RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev

COPY requirements.txt /app/requirements.txt

# Configure server
RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Working directory
WORKDIR /app

ADD . .

#EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "RTSP.wsgi:application"]

# CMD gunicorn RTSP.wsgi:application --bind 0.0.0.0:$PORT

# ------- Command line help ---------------------

# Create Image:      docker build  --no-cache=true -t rtpcdock:latest .
# Run Container :    docker run -d -p 8000:8000 rtpcdock:latest

# ------- Command line help ---------------------
## Refrence https://www.youtube.com/watch?v=Oy71OgKZbOQ




