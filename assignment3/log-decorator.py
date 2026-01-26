import logging

#Task1
def logger_decorator (func):
    def wrapper (*args, **kwargs):
        log_string = ""
        result = func(*args,**kwargs)
        log_args="none"
        if args:
            log_args=str(list(args))
        log_kwargs="none"
        if kwargs:
            log_kwargs=str(kwargs)
        log_string = f"function: {func.__name__}\n"
        log_string += f"positional parameters:  {log_args}\n"
        log_string += f"keyword parameters: {log_kwargs}\n"
        log_string += f"return: {result}\n"
        
        logger = logging.getLogger(__name__ + "_parameter_log")
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            logger.addHandler(logging.FileHandler("./decorator.log","a"))
        ...
        # To write a log record:
        #logger.log(logging.INFO, wrapper)
        logger.log(logging.INFO, log_string)
        return ""
    return wrapper

@logger_decorator
def no_param_f ():
    print("Hello, World!")

@logger_decorator
def pos_args_f(*args):
    return True

@logger_decorator
def kw_args_f(**kwargs):
    return logger_decorator


no_param_f()
pos_args_f(10,30)
kw_args_f (d=10,m=60)