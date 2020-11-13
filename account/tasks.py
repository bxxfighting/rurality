from rurality import celery_app


@celery_app.task
def hello_task():
    '''
    打印hello
    '''
    print('hello')


@celery_app.task
def timer_hello_task():
    '''
    打印hello
    '''
    print('timer hello')
