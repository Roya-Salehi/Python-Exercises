import random


def remove_dups_loop(org_list):
    new_list = []
    for i in org_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


def remove_dups_set(org_list):
    return list(set(org_list))


org_list = random.choices(range(1, 100), k=random.randint(1, 20))
new_list_s = remove_dups_set(org_list)
new_list_l = remove_dups_loop(org_list)
org_list.sort()
new_list_s.sort()
new_list_l.sort()
print(
    f"the orginal list : {org_list}\nthe new list-set : {new_list_s}\nthe new list-loop: {new_list_l}")
