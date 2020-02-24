def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))


foo(huda="M",Qualis="F")
foo(large="Intestine",small="intestine")
