# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
FROM python:3.10-bullseye as builder
ARG VERSION="master"
RUN pip install -U pip \
 && pip install gunicorn \
 && pip install git+https://github.com/Waseda-TakeuchiLab/webapp-photo-luminescence@${VERSION}

FROM python:3.10-slim-bullseye as runner
RUN apt-get update \
 && apt-get install -y python3-opencv
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
