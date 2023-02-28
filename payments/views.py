import json
import stripe
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from payments.models import Order, Item
from payments.utils import get_session_id
from stripe_project.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY
User = get_user_model()


@api_view(http_method_names=['GET'])
def buy_view(request, item_id):
    session_id = get_session_id(item_id)
    return Response(json.dumps([{'session_id': session_id}]))


@api_view(http_method_names=['GET'])
def order_view(request):
    ids = request.GET.get('ids', 'None')
    if ids == 'None':
        return Response('Неверное значение ключа ids',
                        status=status.HTTP_400_BAD_REQUEST)
    ids = ids.split(sep=',')
    for item in ids:
        if not item.isdigit():
            return Response('Неверное значение ключа ids',
                            status=status.HTTP_400_BAD_REQUEST)

    ids = list(map(int, ids))
    order = Order()
    order.save()
    order.items.add(*ids)
    session_id = get_session_id(ids)
    return Response([{"session_id": session_id}])


def item_view(request, pk):
    template_name = "item.html"
    context = {'item': Item.objects.get(pk=pk), 'key': STRIPE_API_KEY}
    return render(request, template_name, context)