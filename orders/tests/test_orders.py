from django.urls.base import reverse
import pytest


@pytest.mark.django_db
def test_orders_list_returns_orders(client):
    response = client.get(reverse('orders_list'))
    assert response.status_code == 200