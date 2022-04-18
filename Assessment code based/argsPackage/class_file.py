








def StartStopwitharguement(ele1,ele2,ele3):
    def outer_fun(fun):
        def inner_fun(*args):
            fun(*args)
        return inner_fun
    return outer_fun

