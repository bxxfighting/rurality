'''
gunicorn -c gunicorn.py rurality.wsgi:application
'''
import os
import multiprocessing

# 设置gunicorn进程名称，ps和top时可以查看
# 需要安装: pip install setproctitle
proc_name = 'rurality'
default_proc_name = 'rurality'
CUR_DIR = os.path.dirname(__file__)

# 开启几个进程
workers = multiprocessing.cpu_count() * 2
# 每个进程开启几个线程
threads = multiprocessing.cpu_count() * 2
# 每个worker最大处理请求数量, 超过就重启此worker
max_requests = 1000
# 随机增加偏移量range(1, max_requests_jitter)，与max_requests配合，防止多个worker同时重启
max_requests_jitter = 100

bind = "0.0.0.0:18785"
chdir = CUR_DIR
preload = True
worker_class = 'gevent'
