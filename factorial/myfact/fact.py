"myfact module"
def factorial(num):
    """
    fanhui geiding shuzi de jiecheng
    """
    if num >= 0:
        if num == 0:
            return 1
        return num*factorial(num-1)
    else:
        return -1
