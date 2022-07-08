# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
wsgi_app = "webapp_pomp_probe:server"
workers = 2
bind = "0.0.0.0:8050"
raw_env = [
    "URL_BASE_PATH=/pomp-probe/"
]
