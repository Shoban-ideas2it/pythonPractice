def myFun(*args,**kid):
    print("args: ", args)
    print("kwargs: ", kid['mid'])
  
  
# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks','for','geeks',first="Geeks",mid=12,last="Geeks")