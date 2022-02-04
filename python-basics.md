
## Data Structures
<pre>
A list is mutable: l = [1,2,3]
A dict is key/value pair: d = {“x”:1, “y”:2, “z”:3}
A tuple is an immutable list: t = (1,2,3)
A set contains distinct values: s = {1,2,3}
</pre>
## List
<pre>
x = [1,2,3,4,4]
y = [num** 2 for num in x]
print(y)
[1, 4, 9, 16, 16]

Item = lst.pop() # removes the last item from the list, and assigns to item
Item = lst.pop(0) # removes the first item from the list, and assigns to item
</pre>

## Dict
<pre>
z = {(num,num** 2) for num in x}
print(z)
{(3, 9), (1, 1), (4, 16), (2, 4)}

z.keys()
z.values()
z.items()

Dictionary does not retain the order.
</pre>

## Tuple
<pre>
a = (num** 3 for num in x)
print(a)
<generator object <genexpr> at 0x10c4cad50>
</pre>

## Set
<pre>
b = {num for num in x}
print(b)
{1, 2, 3, 4}
</pre>

## Filter using count and lambda
<pre>
s = 'This dog runs faster than the other dog dude!'
print(s.count('dog'))

words = s.split(' ')
dog_count = s.split(' ').count('dog')
print(words)
print('dog count {}',dog_count)

dog_count_filter = len([word for word in words if word =='dog'])
print('dog count using filter: {}',dog_count_filter)

seq = [1,2,3,4,5,6,7,8,9]
seqfiltered = list(filter(lambda num: num%3==0 ,seq))
print('seqfiltered: ', seqfiltered)
seqfiltered:  [3, 6, 9]
</pre>

## Lambda functions
<pre>
seq = ['Soup','dog','salad','cat','Sreat']

seq_filtered1 = [x.upper() for x in seq if x.lower().startswith('s')]
print(seq_filtered1)
  
seq_filtered2 = list(filter(lambda x: x.lower().startswith('s'),seq))
print(seq_filtered2)
['SOUP', 'SALAD', 'SREAT']
['Soup', 'salad', 'Sreat']
</pre>

## Lambda examples
<pre>
seq = [1,2,3,4,5]
newlist = list(map(lambda var:var**2, seq))
print('newlist: ', newlist)
  
newdict = dict(map(lambda var:(var**2,var**4), seq))
print('newdict: ', newdict)
  
newtuple = tuple(map(lambda var:(var**2,var**4), seq))
print('newtuple: ', newtuple)

newlist:  [1, 4, 9, 16, 25]
newdict:  {1: 1, 4: 16, 9: 81, 16: 256, 25: 625}
newtuple:  ((1, 1), (4, 16), (9, 81), (16, 256), (25, 625))
</pre>

## Tuple unpacking
<pre>
x = [(1,2),(3,4),(5,6)]</br>
for a,b in x:</br>
    print("a, b:", a, b)
</pre>
