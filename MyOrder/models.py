from django.db import models


class FastFoodChain(models.Model):

    MCDONALDS = "McDonald's"
    KFC = "KFC"
    SUBWAY = "Subway"
    BURGERKING = "Burger King"

    fast_food_companies_types = [
        (MCDONALDS, "McDonald's"),
        (KFC, "KFC"),
        (SUBWAY, "Subway"),
        (BURGERKING, "Burger King")
    ]

    # If you can't choose, the obvious choice would be McDonald's
    type_of_food = models.CharField(max_length=25, choices=fast_food_companies_types,
                                    blank=None, default=MCDONALDS)


class McDonaldsFastFoods(models.Model):
    MCBURGER = "McBurger"
    MCTOAST = "McToast"
    MCFLURRY = "McFlurry"

    fast_food_mcdonalds_types = [
        (MCBURGER, "McBurger"),
        (MCTOAST, "McToast"),
        (MCFLURRY, "McFlurry")
    ]

    # Everyone enjoys the occasional McBurger
    type_of_McFood = models.CharField(max_length=25, choices=fast_food_mcdonalds_types,
                                      blank=None, default=MCBURGER)

    name_of_McFood = models.CharField(max_length=25, blank=None, default=MCBURGER)
