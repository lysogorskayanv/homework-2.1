def read_recipes():
    with open('menu.txt') as f:
        recipe_dict = {}

        for line in f:
            dish_name = line.rstrip()
            quantity = int(f.readline())
            ingr_list = []

            for i in range(quantity):
                ingr = list(f.readline().rstrip().split(' | '))
                ingr_dict = {}
                ingr_dict.update({'ingredient_name': ingr[0], 'quantity': int(ingr[1]), \
                    'measure': ingr[2]})
                ingr_list.append(ingr_dict)

            recipe_dict[dish_name] = ingr_list
            f.readline()
        return recipe_dict

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  cook_book = read_recipes()
  for dish in dishes:
    for ingredient in cook_book[dish]:
      new_shop_list_item = dict(ingredient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingredient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  print ("Меню содержит следующие блюда. Омлет, Утка по-пекински, Запеченый картофель, Фахитос")
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .capitalize().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()