###  Python异常处理

#### 基本介绍

异常处理是个很重要，也有点难度的概念。我们先理解基本的概念，后面再不断通过实践来加深掌握。 

官方文档如下：

[Errors and Exceptions]: https://docs.python.org/3/tutorial/errors.html

 Python 提供的异常处理机制可以用下面的模板来说明： 

```python
try:
    # 把有可能出现异常的代码放在 try 后面
    # 当出现异常时解释器会捕获异常
    # 并根据异常的类型执行后面的对应代码块
    do_something_nasty()
except ValueError:
    # 如果发生 ValueError 类型的异常则执行这个代码块
    pass
except (TypeError, ZeroDivisionError):
    # 可以一次指定几个不同类型的异常在一起处理exceptions
    # 如果出现 TypeError 或者 ZeroDivisionError 则执行这个代码块
    pass
except:
    # 所有上面没有专门处理的类型的异常会在这里处理
    pass
else:
    # 当且仅当 try 代码块里无异常发生时这个代码块会被执行
    pass
finally:
    # 无论发生了什么这个代码块都会被执行
    # 通常这里是清理性的代码，比如我们在 try 里面打开一个文件进行处理
    # 无论过程中有没有异常出现最后都应该关闭文件释放资源
    # 这样的操作就适合在这里执行
```

除了以上提到的内建错误类型（ValueError，ZeroDivisionError以及TypeError），Python还提供了多种内建错误类型，可以参考官方文档如下：

[Built-in Exceptions]: https://docs.python.org/3/library/exceptions.html#bltin-exceptions

如果打不开，可以参考以下版本：

[Python 异常处理]: https://www.runoob.com/python/python-exceptions.html

#### 相关代码测试

见`Built_in_Exception.py`

##### 关键字功能：          

| Keywords   | Explanation                                    |
| ---------- | ---------------------------------------------- |
| try/except | 捕获异常并处理                                 |
| pass       | 忽略异常                                       |
| as         | 定义异常实例                                   |
| else       | 如果try中语句没有引发异常，执行此代码块        |
| finally    | 无论是否出现异常，都要执行的代码块，如关闭文件 |
| raise      | 抛出/引发异常                                  |

##### 测试程序解释：

- 首先第一个Try语句里面包含了一个“0作除数错误”，它会被对应的异常捕获到，并执行了对应代码块（输出“OOPS……）
- 由于已经探测到错误，try之后的语句将不再执行，没错，说的就是你 `b = 2` 。这会带来什么问题呢？首先由于第二个异常捕获（`except (NameError, EOFError):`  中对应的输出语句没有输出，我们可以得知在捕获到了异常以后，之后的异常捕获不再进行。由于已经引发了异常，else后面跟的代码块也不会被执行，但是finally跟的代码块还是要执行的。
- 我选择打印出a和b的值，但根据我们之前的情况，a的值在第一个try中被初始化为1，而b的初始化实际上是没有进行的。所以这里再用一个try去捕获异常（NameError），被捕获到以后我们在最后的finally语句中打印出b的值1。
- 最后这句print是为了检测另外一种情况：假设我们将Line 16的NameError换成别的异常检测，比如ValueError，即我们的异常捕获是没有成功的，但实际发生了异常。那么程序会终止，但终止前仍然会去运行finally语句中的代码块。但后面的语句就不会再执行了。

##### 测试程序OUTPUT：

![img](file:///C:\Users\wwwxi\AppData\Roaming\Tencent\Users\123466188\QQ\WinTemp\RichOle\Q[W{SATJ8UXPUFKAU[4QAZH.png) 

#### 用户自定义异常

此外还有用户自定义异常。这部分代码我Copy了另一位博主的，很好理解。供大家参考：

 我们还可以从 `Exception` 派生出我们自己的异常类型，并使用 `raise` 关键字来在出现某种情况时抛出我们定义的异常，并在文档中做出清晰的说明。这样使用我们代码的其他程序员就知道什么情况是我们程序处理不了的，会抛出什么样的异常，并在调用端用捕获异常进行处理。 

在try语句块中，抛出用户自定义的异常后执行except部分，变量 e 是用于创建MyError类的实例。

##### 代码：

见`User_define_exception.py`

```python
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    
try:
    raise MyError('类型错误')
except MyError as e:
    print('My exception occurred', e.msg)
#  OUTPUT: My exception occurred 类型错误
```

