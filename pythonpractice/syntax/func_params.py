# params and arguments
# default arguments
# dont use default argument for mutable types
# required arguments must come before default arguments
# keyword and positional arguments
# *args vs **kwargs. args is positional, kwargs is keyword

class FunctionParam:
    def optional_args(self, optional_arg="defaultstring"):
        """function that sets a default value for the argument if nothing was passed into the param"""
        print(optional_arg)

    def positional_args(self, arg1, arg2):
        print(arg1)
        print(arg2)

    def multiple_args(self, *args):
        """function that accepts any number of arguments"""
        print(args)

    def multiple_kwargs(self, **kwargs):
        """function that accepts any number of keyword arguments"""
        print(kwargs)

tester = FunctionParam()
tester.optional_args()
tester.optional_args("somestring")
tester.positional_args(arg2="2", arg1="1")
tester.multiple_args("one", "two", "three")
tester.multiple_kwargs(first="one", third="three", second="two")