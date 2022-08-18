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
print(
    f"the orginal list : {sorted(org_list)}\nthe new list-set : {sorted(new_list_s)}\nthe new list-loop: {sorted(new_list_l)}")
