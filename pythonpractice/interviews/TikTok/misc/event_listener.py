def function1(*arguments):
    print(arguments)
    sum = 0
    for arg in arguments:
        sum += arg
    return sum

class EventListener():
    def __init__(self) -> None:
        self.events = {}

    def assign(self, key, function):
        self.events[key] = function

    def call(self, key, *extra_args):
        print(extra_args)
        # how to unpack multiple args
        return self.events[key](*extra_args)

    def remove(self, key):
        del self.events[key]

    def print_events(self):
        print(self.events)

if __name__ == "__main__":
    event_listener = EventListener()
    event_listener.print_events()
    event_listener.assign("add", function1)
    event_listener.print_events()
    print(event_listener.call("add", 2, 3, 4))
    event_listener.remove("add")
    event_listener.print_events()



# e.g. eventListener.assign("key", function)  // this assigns function to "key"
# eventListener.call("key", extra_args) // this calls function assigned to "key" and pass in extra_args to the function
# evetnListener.remove("key") // this removes the function assigned to "key"