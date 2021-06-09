
import time
import os

os.environ['http_proxy'] = 'http://127.0.0.1:8888'
os.environ['https_proxy'] = 'http://127.0.0.1:8888'

def sleep(n_secs):
    time.sleep(n_secs)


