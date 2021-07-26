#!/bin/bash

echo "\033[36m------| 解压init_agent源码包 |------\033[0m"
cd /opt/src/
tar -xvf agent-1.0.tar.gz

echo "\033[36m------| 创建日志目录 |------\033[0m"
mkdir -p /var/log/agent

echo "\033[36m------| 启动agent进程 |------\033[0m"
# cd agent-1.0 && gunicorn -c gunicorn.py  main:app && ./dsmagent
cd agent-1.0 && ./dsmagent -gui-address="http://0.0.0.0:8384"
