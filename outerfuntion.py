def outer_func():
   global a
   a=20
   print("a =",a)
a=10
outer_func()
print("global value of a=",a)
