names_dict = {}
with open('./assets/nameslist.txt', 'r') as names_list_file:
    names_list = names_list_file.read().split('\n')
    for name in names_list:
        value = names_list.count(name)
        names_dict.update({name: value})
        for _ in range(value):
            names_list.remove(name)

print(names_dict)

categories_dict = {}
with open('./assets/Training_01.txt', 'r') as training_file:
    images_names = training_file.read().split('\n')
    for img_name in images_names:
        img_ctg_list = img_name.split('/')[2:-1]
        img_ctg_name = '/'.join(img_ctg_list)
        if img_ctg_name in categories_dict:
            categories_dict[img_ctg_name] += 1
        else:
            categories_dict[img_ctg_name] = 1

print(categories_dict)
