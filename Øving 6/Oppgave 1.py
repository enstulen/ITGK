__author__ = 'Morten Stulen'
li = [1, 2, 3, 4, 5, 6]

for items in li:
    if li[items] % 2 == 0:
        li[items] *= -1
li.sort(key = lambda x: -x)
# li.reverse()
print(li)
