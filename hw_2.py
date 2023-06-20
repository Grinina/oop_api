import os
current = os.getcwd()
from pprint import pprint
file_name = 'recipes.txt'
full_path = os.path.join(current, file_name)
with open(full_path, 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredient_count = int(file.readline().strip())
        ingredient = []
        for _ in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredient.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredient

def get_shop_list_by_dishes(dishes, person_count):
    dish_list = []
    for dish in dishes:
        for dish_name in cook_book:
            if dish == dish_name:
                dish_list.append(cook_book[dish_name])
    list_ing_name = []
    for dish in dish_list:
        for ingredient in dish:
            list_ing_name.append(ingredient)
    list_ingredient = []
    for ingredient in list_ing_name:
        list_ingredient.append(ingredient['ingredient_name'])
    list_ingredient = list(set(list_ingredient))
    list_ingredient_modern = []
    for ingredient in  list_ing_name:
        ingredient_modern = {ingredient['ingredient_name'] : {'measure': ingredient['measure'], 'quantity': ingredient['quantity']}}
        list_ingredient_modern.append(ingredient_modern)
    ingredient_book = {}
    for ingredient in list_ingredient:
        quantity = 0
        for ingredient_modern in list_ingredient_modern:
            for k, v in ingredient_modern.items():
                if ingredient == k:
                    measure = v['measure']
                    quantity += int(v['quantity'])
        new = {ingredient : {'measure': measure, 'quantity': quantity * person_count}}
        for k, v in new.items():
            ingredient_book[k] = v
    return(ingredient_book)
pprint(get_shop_list_by_dishes(['Запеченный картофель'], 10))