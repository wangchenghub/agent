FROM ubuntu:20.04
LABEL maintainer = "wangcheng" version = "v1.0" description = "agent"
                   
RUN apt update -y \
    && mkdir -p /opt/src \
    && apt install -y python3 python3-pip && \
    apt clean 

RUN python3 -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && python3 -m pip install Flask==2.0.1 Flask-RESTful==0.3.9 gevent==21.1.2 gunicorn==20.1.0 requests==2.26.0

COPY dist/ /opt/src/
COPY run.sh /run.sh

ENV PUID=1000 PGID=1000 HOME=/var/dsmagent/
ENTRYPOINT ["sh", "/run.sh"]
