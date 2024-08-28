from django.contrib import admin
from .models import Buyer, Game

# Регистрация модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля, по которым можно осуществлять поиск
    list_filter = ('age',)  # Поля, по которым можно фильтровать

# Регистрация модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'age_limited')  # Поля, которые будут отображаться в списке
    search_fields = ('title', 'description')  # Поля, по которым можно осуществлять поиск
    list_filter = ('age_limited',)  # Поля, по которым можно фильтровать