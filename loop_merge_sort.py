def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp

l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
print loop_merge_sort(l1, l2)
