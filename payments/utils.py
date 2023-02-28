import stripe

from payments.models import Item


def update_items():
    '''Функция, которая обновляет БД Items значениями из stripe'''
    product = stripe.Product.list()
    for item in product.data:
        price = stripe.Price.search(
            query=f'product: "{item["id"]}"'
            )['data'][0]['unit_amount']/100
        Item.objects.get_or_create(
            name=item['name'],
            description=item['description'],
            price=price)


def get_session_id(item_ids):
    '''Функция, которая возвращает необходимый session_id'''
    update_items()
    line_items = []
    if not isinstance(item_ids, list):
        item_ids = list(item_ids)
    for item_id in item_ids:
        item = Item.objects.get(pk=item_id)
        product = stripe.Product.search(query=f'name: "{item.name}"')
        price = stripe.Price.search(
            query=f'product: "{product.data[0]["id"]}"'
            )
        line_items.append({
            "price": price['data'][0]['id'],
            "quantity": 1,
        })
    request = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=line_items,
        mode="payment",
    )
    session_id = request['url']
    return session_id
