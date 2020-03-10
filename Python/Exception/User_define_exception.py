class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    
try:
    raise MyError('类型错误')
except MyError as e:
    print('My exception occurred', e.msg)
#  OUTPUT: My exception occurred 类型错误