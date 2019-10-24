def div(a,b):
    print(a/b)

def smart_div(func):  ## function taking function as parameter

    def inner(a,b):         ## function taking variables as parameter
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

NewDiv=smart_div(div)
div(2,4)  ## calling original div function
NewDiv(2,4)  ## calling new smart div function