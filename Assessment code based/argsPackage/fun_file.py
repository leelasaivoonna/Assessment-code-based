def dec_with_arg(el1,el2,el3):
    def outer_fun(fun):
        def inner_fun(*args):
            print("print 2 player names", el1, el2)
            fun(*args)
            print("getting the name of 3rd player" , el3)
        return inner_fun
    return outer_fun



