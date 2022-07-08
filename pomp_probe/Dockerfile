# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
FROM python:3.10-bullseye as builder
ARG VERSION="master"
RUN pip install -U pip \
 && pip install gunicorn \
 && pip install git+https://github.com/Waseda-TakeuchiLab/webapp-pomp-probe@${VERSION}

FROM python:3.10-slim-bullseye as runner
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages