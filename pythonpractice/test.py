def somefunc(item_in_list):
    return item_in_list+2

mylist = [1, 2, 3, 4, 5]
newlist_it = map(somefunc, mylist)

print(newlist_it)
print(list(newlist_it))

lambda list: True if len(list) > 0 else False