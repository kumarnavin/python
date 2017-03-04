def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a',[])

print "list1 = %s" % list1 # 10,a
print "list2 = %s" % list2 # 123
print "list3 = %s" % list3 # 123, a

def multipliers():
  return [lambda x : i * x for i in range(4)]
    
for m in multipliers():
	print(str(m))
print [m(2) for m in multipliers()]