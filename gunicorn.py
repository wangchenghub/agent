import os
ENVIRON = os.environ

import multiprocessing
bind = str(ENVIRON.get("LOCAL_IP", "0.0.0.0")) + ":" + str(ENVIRON.get("AGENT_HTTP_PORT", 8900))  # 绑定ip和端口号
backlog = 512                                                                                     # 监听队列
chdir = './'                                                                                      # gunicorn要切换到的目的工作目录
timeout = 30                                                                                      # 超时
pidfile = './gunicorn.pid'                                                                        # pid 文件路径
# daemon = True                                                                                     # 守护进程
worker_class = 'gevent'                                                                           # 使用gevent模式，还可以使用sync 模式，默认的是sync模式
workers = multiprocessing.cpu_count() * 2 + 1                                                     # 进程数
threads = 2                                                                                       # 指定每个进程开启的线程数
loglevel = 'debug'                                                                                # 日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'                  # 设置gunicorn访问日志格式，错误日志无法设置
accesslog = "/var/log/agent/gunicorn_access.log"                                                  # 访问日志文件
errorlog = "/var/log/agent/gunicorn_error.log"                                                    # 错误日志文件