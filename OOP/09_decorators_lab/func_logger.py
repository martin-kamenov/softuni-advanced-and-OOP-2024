class func_logger:

    _log_file = 'text.txt'

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        log_string = self.function.__name__ + ' was called'

        with open(self._log_file, 'a') as file:
            file.write(log_string + '\n')

        return self.function(*args)

@func_logger
def say_hi(name):
    print(f"Hi, {name}")
@func_logger
def say_bye(name):
    print(f"Bye, {name}")

say_hi("Peter")
say_bye("Peter")