class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def print_exception(self):
        print("user defined exception: ", self.msg)




try:
    raise MemoryError('crash between two cars')
except MemoryError as e:
    print(e)