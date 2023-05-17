try:
    x = [1, 5]
    y = ''.join(x)
    z = int(y)//2
    print(z)
except Exception as e:
    print(e)