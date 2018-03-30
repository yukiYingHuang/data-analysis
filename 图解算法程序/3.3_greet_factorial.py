def greet2(name):
    print("how are you, ", name, "?")

def bye(name):
    print(name,", bye!")

def greet(name):
    print("hello, ", name, "!")
    greet2(name)
    print("It's time to say bye...")
    bye(name)


def factorial(number): #正整数才有阶乘
    if number < 0:
        print('阶乘不存在！')
        return None
    elif number ==0 or number == 1:
        return 1
    else:
        return number*factorial(number-1)

greet("yuki")

print(factorial(5))  # 5*4*3*2*1=120
print(factorial(0))  #1
print(factorial(-2)) #None，