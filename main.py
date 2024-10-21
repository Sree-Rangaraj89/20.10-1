lst = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi']

print("lengthof list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Updeated list:", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated list:", lst)

lst.reverse()
print("Reversed List:", lst)

print("Multiplication List:", lst)

lst = lst[:4]
print("Sliced list:", lst)

lst.clear()
print("Updated list:", lst)
