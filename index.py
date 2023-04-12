from appliances import CoffeeMaker, CanOpener
from appliances.kitchen import DishWasher
from appliances import Washer
from appliances import Refrigerator
from appliances import Dryer

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "electric")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

oxo_opener = CanOpener("black")
oxo_opener.open_can()
