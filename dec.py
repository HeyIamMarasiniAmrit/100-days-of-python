#def inc(x):
#    return x + 1

#def operate(func, x):
  #  result = func(x)
   # return result


#print(operate(inc, 3))

#def print_msg(message):
 #   greeting = "Hello"

  #  def printer():
  #      print(greeting, message)

  #  return printer

#func = print_msg("python is awasome")
#func()

def printer():
    print("Hello world")

def display_info(func):

    def inner():
        print("Executing", func._name_,"function")
        func()
        print("finished execution")

    return inner()

decorated_func = display_info(printer)
decorated_func()