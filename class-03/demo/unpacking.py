def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

if __name__=="__main__":
    nums = {3,7,5,6}
    print(my_sum(2,7,3,9,0,5))
    print(my_sum(4,5))
    print(my_sum(*nums))




def fun(*args):
    # for arg in args:
    #     print(arg)
    print(type(args))

fun(3,5,6,7,1,2,3,4,6)

arguments = (3,5,6,7,1,2,3,4,6)
fun(*arguments)