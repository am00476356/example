"""
classmethod use case

to make multiple constructor classes.
"""

# class GPL:
#
#     def __init__(self):
#         pass
#
#     def __init__(self, team_a, team_b):
#         self.team_a = team_a
#         self.team_b = team_b
#
#
# gpl = GPL()


# class GPL(object):
#
#     def __init__(self, *args, **kwargs):
#         pass
#
#     @classmethod
#     def info(cls):
#         print("WELCOME TO GPL")
#         return cls()
#
#     @classmethod
#     def conduct_match(cls, team_a, team_b):
#         cls.info()
#         print(f"Today's match is {team_a} vs {team_b}")
#         return cls(team_a, team_b)
#
# gpl = GPL() # object
# print(gpl)
# gpl1 = GPL.info() # return an object
# print(gpl1)
# gpl2 = GPL.conduct_match("Tappu", "Bhide")
# print(gpl2)

# paneer bhurji
# dal fry
# maggi
# masala papad


class OrderAtHotel:

    def __init__(self, ingredient):
        self.ingredient = ingredient

    def __repr__(self):
        return f"{self.ingredient}"

    @classmethod
    def paneer_bhurji(cls):
        return cls(["paneer", "tomato", "cheese", "onion"]) # OrderAtHotel([])

    @classmethod
    def dal_fry(cls):
        return cls(["dal", "fry"])

    @classmethod
    def maggi(cls):
        return cls(["maggi_packet", "water"])

    @classmethod
    def masala_papad(cls):
        return cls(["tomato", "papad", "onion", "cucumber", "sev"])


# single constructor
paneer_bhurji = OrderAtHotel(["paneer", "tomato", "cheese", "onion"])
print(paneer_bhurji)
# dal_fry = OrderAtHotel(["dal", "fry"])

# mutiple constructor
pb = OrderAtHotel.paneer_bhurji()
print(pb)
#
df = OrderAtHotel.dal_fry()
print(df)

print(OrderAtHotel.maggi())
print(OrderAtHotel.masala_papad())


