from django.shortcuts import render
from MyOrder.models import McDonaldsFastFoods


def fast_foods_menu(request):

    context = {
        'foods': McDonaldsFastFoods.objects.all(),
    }

    return render(request, "main_menu.html", context)
