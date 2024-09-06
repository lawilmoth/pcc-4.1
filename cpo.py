import sys, io

def capture_print_output(func):
    """This function wraps around functions redirecting printed output to the out variable 
    and returns the printed value
    This can be used as a decorator, or it can be wrapped around prewritten function for testing purposes
    Ex: 
    def hello_world():
        print("hello")
    ans = capture_print_output(hello_world)()"""
    def inner(*args, **kwargs):
        out = io.StringIO()
        sys.stdout = out
        func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return out.getvalue().strip()
    return inner