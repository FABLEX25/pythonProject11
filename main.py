def zadacha1():
    class Restaurant:
        def __init__(self,restaurant_name,cuisine_type):     #init - метод, позволяющий принимать аргументы для класса
            self.restaurant_name = restaurant_name      #self - параметр, который передаётся первым аргументом в метод класса и представляет собой ссылку на экземпляр класса
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name ,"\nКухня ресторана: ",self.cuisine_type)
        def open_restaurant(self):
            print("Ресторан открыт к посещению!")
    newRestaurant = Restaurant(input(),input())
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()


def zadacha2():
    class Restaurant:
        def __init__(self,restaurant_name,cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name ,"\nКухня ресторана: ",self.cuisine_type)
        def open_restaurant(self):
            print("Ресторан открыт к посещению!")
    newRestaurant = Restaurant(input(),input())
    secondRestaurant=Restaurant(input(),input())
    thirdRestaurant=Restaurant(input(),input())
    newRestaurant.describe_restaurant()
    secondRestaurant.describe_restaurant()
    thirdRestaurant.describe_restaurant()


def zadacha3():
    class Restaurant:
        def __init__(self,restaurant_name,cuisine_type,rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name,"\nКухня ресторана: ",self.cuisine_type,"\nРейтинг",self.rating)
        def open_restaurant(self):
            print("Ресторан открыт к посещению!")
        def changerating(self,newrating):
            self.rating=newrating

    newRestaurant = Restaurant("Клодмане","Французская",rating=3)
    newRestaurant.describe_restaurant()
    newRestaurant.changerating(5)
    newRestaurant.describe_restaurant()


zadacha3()