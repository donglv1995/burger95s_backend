from src.database.database import SessionLocal
from src.burger95s.models.models import Item, Burger, Order, StorageItem, BurgerItemAssociation
from src.burger95s import constant

session = SessionLocal()

white_bread = Item(name='white bread')
dark_bread = Item(name='dark bread')
beef = Item(name='beef')
chicken = Item(name='chicken')
bacon = Item(name='bacon')
fish = Item(name='fish')
shrimp = Item(name='shrimp')
eggs = Item(name='eggs')
cheese = Item(name='cheese')
salads = Item(name='salads')
tomatoes = Item(name='tomatoes')

session.add_all([
    white_bread,
    dark_bread,
    beef,
    chicken,
    bacon,
    fish,
    shrimp,
    eggs,
    cheese,
    salads,
    tomatoes
])

session.commit()

storage_white_bread=StorageItem(quantity=20,item_id=white_bread.id)
storage_dark_bread=StorageItem(quantity=20,item_id=dark_bread.id)
storage_beef=StorageItem(quantity=30,item_id=beef.id)
storage_chicken=StorageItem(quantity=30,item_id=chicken.id)
storage_bacon=StorageItem(quantity=50,item_id=bacon.id)
storage_fish=StorageItem(quantity=30,item_id=fish.id)
storage_shrimp=StorageItem(quantity=30,item_id=shrimp.id)
storage_eggs=StorageItem(quantity=50,item_id=eggs.id)
storage_cheese=StorageItem(quantity=80,item_id=cheese.id)
storage_salads=StorageItem(quantity=100,item_id=salads.id)
storage_tomatoes=StorageItem(quantity=100,item_id=tomatoes.id)


session.add_all([
    storage_white_bread,
    storage_dark_bread,
    storage_beef,
    storage_chicken,
    storage_bacon,
    storage_fish,
    storage_shrimp,
    storage_eggs,
    storage_cheese,
    storage_salads,
    storage_tomatoes
])

session.commit()



beef_burger = Burger(name='beef burger', type=constant.BURGER_TYPE_ORIGINAL)
double_beef_burger = Burger(name='double beef burger', type=constant.BURGER_TYPE_ORIGINAL)
chicken_burger = Burger(name='chicken burger', type=constant.BURGER_TYPE_ORIGINAL)
bacon_eggs_burger = Burger(name='bacon eggs burger', type=constant.BURGER_TYPE_ORIGINAL)
fish_burger = Burger(name='fish burger', type=constant.BURGER_TYPE_ORIGINAL)
shrimp_burger = Burger(name='shrimp burger', type=constant.BURGER_TYPE_ORIGINAL)
special = Burger(name='special', type=constant.BURGER_TYPE_ORIGINAL)

session.add_all([
    beef_burger,
    double_beef_burger,
    chicken_burger,
    bacon_eggs_burger,
    fish_burger,
    shrimp_burger,
    special
])

session.commit()

'''
white_bread,
dark_bread,
beef,
chicken,
bacon,
fish,
shrimp,
eggs,
cheese,
salads,
tomatoes

'''
# quantity default = 1
beef_burger.items.append(BurgerItemAssociation(white_bread, 1))
beef_burger.items.append(BurgerItemAssociation(beef, 1))
beef_burger.items.append(BurgerItemAssociation(cheese, 1))
beef_burger.items.append(BurgerItemAssociation(salads, 1))
beef_burger.items.append(BurgerItemAssociation(tomatoes, 1))

# beef, cheese with quantity = 2, else are 1

double_beef_burger.items.append(BurgerItemAssociation(white_bread,1))
double_beef_burger.items.append(BurgerItemAssociation(beef,2))
double_beef_burger.items.append(BurgerItemAssociation(cheese,2))
double_beef_burger.items.append(BurgerItemAssociation(salads,1))
double_beef_burger.items.append(BurgerItemAssociation(tomatoes,1))




# quantity default = 1

chicken_burger.items.append(BurgerItemAssociation(white_bread,1))
chicken_burger.items.append(BurgerItemAssociation(chicken,1))
chicken_burger.items.append(BurgerItemAssociation(cheese,1))
chicken_burger.items.append(BurgerItemAssociation(salads,1))
chicken_burger.items.append(BurgerItemAssociation(tomatoes,1))
    


# quantity default = 1

bacon_eggs_burger.items.append(BurgerItemAssociation(white_bread,1))
bacon_eggs_burger.items.append(BurgerItemAssociation(bacon,1))
bacon_eggs_burger.items.append(BurgerItemAssociation(eggs,1))
bacon_eggs_burger.items.append(BurgerItemAssociation(cheese,1))
bacon_eggs_burger.items.append(BurgerItemAssociation(salads,1))
bacon_eggs_burger.items.append(BurgerItemAssociation(tomatoes,1))




# quantity default = 1

fish_burger.items.append(BurgerItemAssociation(white_bread,1))
fish_burger.items.append(BurgerItemAssociation(fish,1))
fish_burger.items.append(BurgerItemAssociation(cheese,1))
fish_burger.items.append(BurgerItemAssociation(salads,1))
fish_burger.items.append(BurgerItemAssociation(tomatoes,1))




# quantity default = 1

shrimp_burger.items.append(BurgerItemAssociation(white_bread,1))
shrimp_burger.items.append(BurgerItemAssociation(shrimp,1))
shrimp_burger.items.append(BurgerItemAssociation(cheese,1))
shrimp_burger.items.append(BurgerItemAssociation(salads,1))
shrimp_burger.items.append(BurgerItemAssociation(tomatoes,1))


'''
    to create a burger with item's quantity > 1:
    - append into Associtation Objects
    - for item, value in enumerate(item_quantity_dict):
        BurgerItemAssociation(burger=special, item=item, quantity=value)
    
    In special burger, given:
        - dark_bread = 1
        - beef = 2
        - eggs = 1
        - cheese = 2
        - salads = 1
        - tomatoes = 1
'''

special.items.append(BurgerItemAssociation(dark_bread,1))
special.items.append(BurgerItemAssociation(beef,2))
special.items.append(BurgerItemAssociation(eggs,1))
special.items.append(BurgerItemAssociation(bacon,1))
special.items.append(BurgerItemAssociation(cheese,2))
special.items.append(BurgerItemAssociation(salads,1))
special.items.append(BurgerItemAssociation(tomatoes,1))



session.commit()


# orders
kyQuan = Order(consumer_name='ky quan')
dongLuong = Order(consumer_name='dong luong')
thanhHieu = Order(consumer_name='thanh hieu')

# order burgers
kyQuan.ordering.extend([fish_burger, shrimp_burger])
dongLuong.ordering.extend([double_beef_burger])
thanhHieu.ordering.extend([special, bacon_eggs_burger, chicken_burger])

session.commit()

