def myfunc():
    global y
    y=8
    x=10
    result=x+y
    print(result)
    print(f"b is local variable : {x}")


myfunc()
y=y+11
print(f"a is global variable : {y}")


