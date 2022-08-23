listc = [1,2,3]
liste = [1,2,3,4]
lista = [1,2,3,4,5]
listb = [1,2,3,4,5,6,7]
list_all = [listc,liste,lista,listb]

pattern = []
for i in list_all:
    i_tmp = i[:]
    i_tmp.pop()
    # print(i_tmp)
    # print(i)
    # print('\n')
    if i_tmp in pattern:
        index = pattern.index(i_tmp)
        pattern.pop(index)
        pattern.append(i)
    else:
        pattern.append(i)
print(pattern)
print(list_all)
newlist = list(reversed(list_all))
print(newlist)