# Task_2

class Hotel:
    def __init__(self, name, place, room_mid, mid_room_price, room_lux, lux_room_price, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.place = place
        self.room_mid = {"room1": "free", "room2": "free", "room3": "free"}
        self.mid_room_price = mid_room_price
        self.room_lux = {"room1": "free", "room2": "free", "room3": "free"}
        self.lux_room_price = lux_room_price

    def presentation(self):
        return self.name, self.place, self.room_mid, self.mid_room_price, self.room_lux, self.lux_room_price

    def booking(self):
        for i in self.room_mid.keys():
            self.room_mid[i] = "busy"
        return print(F"will book the rooms {self.room_mid}")

    def avaliable_room_check(self):
        check = True
        for i in self.room_mid.values():
            if i == "free":
                check = True
            else:
                check = False
        return check

    def discount(self):
        return F"{self.mid_room_price - self.mid_room_price * 30 / 100}"


class Taxi(Hotel):
    def __init__(self, name, car_type, price_for_tour, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.car_type = car_type
        self.price_for_tour = price_for_tour

    def presentation(self):
        return self.name, self.car_type, self.price_for_tour

    def discount(self):
        return f"{self.price_for_tour - self.price_for_tour * 15 / 100}"


class Tour(Taxi, Hotel):
    def __init__(self, name,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        # self.price_mid = self.mid_room_price + self.price_for_tour
        # self.price_lux = self.lux_room_price + self.price_for_tour

    def global_presentation(self):
        return print(F"we have middle services, in price{self.mid_room_price + self.price_for_tour} \n", F"we have lux services in price{self.lux_room_price + self.price_for_tour}")


client_1 = Tour("Geghard_tur", "Bmw", "sedan", 10000, "Leran", "geghart", {},
                20000, {}, 40000, )

# print(Tour.__mro__)
print(client_1.presentation())
# print(client_1.booking())
# print(client_1.discount())
print(client_1.avaliable_room_check())
print(client_1.global_presentation())