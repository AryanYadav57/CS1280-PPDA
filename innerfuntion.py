def outer_func():
    b = 20
    print("b =", b)
    def inner_func():
       c = 10 
       print("c =", c)
       print("a in innerloop =",a) 
    inner_func()
a = 1 
print("a =", a)
outer_func()
