try:
    a = 1
    print(1 / 0)#  will be detected Exception
    b = 2#  ‘ZeroDivisionError’ Has been detected，This assignment actually useless 
except ZeroDivisionError as err:#  useful
    print('Oops!There are something unexpected happened:', err)
except (NameError, EOFError):#  actually useless
    b = 1
    print('i\'m here')
else:
    print("else : ")
finally:
    try:
        print("finally a is", a)
        print("finally a is", b)
    except NameError:
        b = 1
#   except ValueError:
        '''  
        if we change 'NameError' To 'ValueError'
        Then the exception of variable b will match fail
        So the program will over after our finally function.
        In other words, print() in the last line will be ignore.
        '''
#       b = 1
    finally:
        print("after Exception b is ", b)
        print('i\'m Hhere')
print('i\'m still here')