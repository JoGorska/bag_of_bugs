from django.urls.base import reverse
import pytest
from core.tests.fixtures import user_one
from species.tests.fixtures import category, size, enviroment, species
from .fixtures import order_one, order_one_item, order_two, order_two_item
from ..models import CustomerOrder


@pytest.mark.django_db
def test_orders_list_returns_orders(client, order_one, order_two):
    response = client.get(reverse('orders_list'))
    assert response.status_code == 200
    json_response = response.json()
    orders_in_db = CustomerOrder.objects.count
    print(len(json_response))
    assert orders_in_db == len(json_response)


