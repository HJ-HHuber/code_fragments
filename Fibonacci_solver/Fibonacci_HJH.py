# Fibonacci solver
#https://github.com/HJ-HHuber
#https://github.com/HJ-HHuber/ML_course


n = int(input('How many results would you like? '))
fibonacci = []
def fibonacci_f(n):
    a=0
    b=1
    if n==0:
      fibonacci.append('null')
    elif n==1:
        fibonacci.append(a)
    else:
        fibonacci.append(a)
        fibonacci.append(b)
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            fibonacci.append(c)
fibonacci_f(n)

if n==0:
  print('No index request possible!')
  print(fibonacci)
elif n==1:
  print('set index = 1, otherwise: n<i')
  print(fibonacci)
else:
  i1 = int(input('First index:'))
  i2= int(input('Second index:'))
  if n<i1 or n<i2:
    print('Are you kidding me? ! n<i ! ->ERROR')
  else:
    print('value 1:', fibonacci[i1-1])
    print('value 2:', fibonacci[i2-1])
