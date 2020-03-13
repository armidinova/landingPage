from django.http import JsonResponse
from django.shortcuts import render
from .models import ProductInBasket


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    number = data.get("number")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)

    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     defaults={"number": number})
        if not created:
            new_product.number += int(number)
            new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_number = products_in_basket.count()
    return_dict["products_total_number"] = products_total_number
    return_dict["products"] = list()
    number = list('number')


    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["number"] = item.number
        return_dict["products"].append(product_dict)
        print(number)

    return JsonResponse(return_dict)
