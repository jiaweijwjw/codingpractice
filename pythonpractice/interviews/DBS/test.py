# have_dups = [1,2,2,2,3,4]
# no_dups_set = set()
# no_dups_set.update(have_dups)
# no_dups = list(no_dups_set)
# print(no_dups)

have_dups = [1,2,3,4,3,2,4]
no_dups = set()
for item in have_dups:
    no_dups.add(item)
print(list(no_dups))
