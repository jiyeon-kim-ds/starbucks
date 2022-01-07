from django.db import models
from django.db.models.deletion import CASCADE

class Menu(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=30)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    korean_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'

class Nutrition(models.Model):
    one_serving_kca = models.IntegerField()
    sodium_mg = models.IntegerField()
    saturated_fat_g = models.IntegerField()
    sugars_g = models.IntegerField()
    protein_g = models.IntegerField()
    caffeine_mg = models.IntegerField()
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    drink = models.ForeignKey(Drink, on_delete=CASCADE)
    img_url = models.CharField(max_length=200)

    class Meta:
        db_table = 'images'

class Allergen(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'allergens'


class Drink_Allergen(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks_allergens'

class Size(models.Model):
    name = models.CharField(max_length=10)
    size_ml = models.CharField(max_length=10)
    size_fluid_ounce = models.CharField(max_length=10)

    class Meta:
        db_table = 'sizes'