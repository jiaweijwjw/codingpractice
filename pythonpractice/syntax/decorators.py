# https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=527s

def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print("inside a decorator func")
        return original_func(*args, **kwargs)
    return wrapper_func

def another_decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print("inside another decorator func")
        return original_func(*args, **kwargs)
    return wrapper_func

class DecoratorClass():
    def __init__(self, original_func) -> None:
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("inside a decorator class")
        return self.original_func(*args, **kwargs)

@another_decorator_func
@decorator_func
@DecoratorClass
def display_func():
    print("display some text")
# decorating
# display_func = another_decorator_func(decorator_func(decorator_class_instance(display_func)))

@DecoratorClass
def display_func_with_args(arg1, arg2):
    print(f"display some args: {arg1} and {arg2}")

display_func()
display_func_with_args(1,2)


# LEARNINGS
# functions are first class objects in python, meaning we can pass them to other functions as arguments and can return them as values
# the () parenthesis after a function name indicates "calling" or "running" the function
# decorators are basically wrappers around functions to add functionalities within altering the original function
# decorators can be implemented either as a function or as a class
# as the wrapper functions here take functions as arguments, we have to account for different varying number of arguments
# naming convention is to use *args and kwargs**
# more than one decorator can be used on a function, but they are called in order. easier way to remember this is to understand what happens when we "decorate"
# see the above comments for more info
# if more than one decorator is used, check out functools @wrap decorator for decorators. used to preserve the original func
