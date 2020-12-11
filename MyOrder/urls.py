from django.urls import path
from MyOrder.views import fast_foods_menu

urlpatterns = [
    path('', fast_foods_menu)
]
