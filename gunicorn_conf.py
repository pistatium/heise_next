import multiprocessing

worker_class = 'uvicorn.workers.UvicornWorker'
workers = 2

reuse_port = True
