n,m=map(int ,input("first number is the number of athlets,\n \
2nd no. is the no. of attribute for each athlet.\n Write:").split())

print()
print("so we have {} athlets and {} in out databse\n" .format(n,m))
l=[]
for i in range(1,n+1):
    l.append(list(map(int ,input("write attributes for athlete number {}:" .format(i)).split())))

l_Athletes=dict()

for i in range (1,n+1):
    l_Athletes[tuple(l[i-1])] = 'Athlete number{}'.format(i)

k=int(input('write the attribute to use as key of sorting from 0 to {}:'.format(m-1)))

l_sorted = sorted(l,key=lambda elem:elem[k])

print()

print("sorted on the {}th attribute:\n\n".format(k))
print("Attribute sorted by colomn {} (from 0 to {})".format(k,m-1).rjust(65))
for elem in l_sorted:
    print('\n')
    print(l_Athletes[tuple(elem)],'--->',end =' ')
    s=map(str,elem)
    for i in range(m):
        print(next(s).center(5),end=' ')
    print('\n')
