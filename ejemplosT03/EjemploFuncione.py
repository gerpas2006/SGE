def buggy(arg,result=[]):
    result.append(arg)
    print(result)

buggy('a', [])
buggy('b',[])
buggy('a',['x','y','z'])
buggy('b',['x','y','z'])

buggy('a')

buggy('b')

def works(arg):
    result2 =[]
    result2.append(arg)
    return result2

print(works('a'))
print(works('b'))

def nobuggy(arg,result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nobuggy('a')
nobuggy('b')
nobuggy('a',['x','y','z'])
nobuggy('b',['x','y','z'])