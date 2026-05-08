####################阶乘计算####################
# Python原生支持大整数运算
####################阶乘计算####################
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input())
print(factorial(n))