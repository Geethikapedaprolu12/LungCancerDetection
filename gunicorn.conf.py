# gunicorn.conf.py

# Server socket
bind = '0.0.0.0:8000'
backlog = 2048

# Worker processes
workers = 3
worker_class = 'sync'
threads = 2
timeout = 30

# Logging
loglevel = 'info'
errorlog = '-'
accesslog = '-'
