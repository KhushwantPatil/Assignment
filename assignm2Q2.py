
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b = set()
b = []
c = dict()
for i in a:
    b.append(ord(i))
c = dict(zip(a,b))
print(c)
