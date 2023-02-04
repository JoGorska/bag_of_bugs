import pytest
from orders.models import OrderItem, CustomerOrder
from core.tests.fixtures import user_one
from species.tests.fixtures import category, size, enviroment, species


# todo add setup.cfg to ignore errors with imports in tests

@pytest.fixture
def order_one(user_one):
    print(f'CHECK IF USER HAS BEEN CREATED {user_one.id}')
    return CustomerOrder.objects.get_or_create(
        user=user_one,
        delivery_address='Long street',
        postcode='WD3 2AD'
    )


@pytest.fixture
def order_item(order_one, species):
    print(f'CHECK IF SPECIES WAS  CREATED {species.name}')
    return OrderItem.objects.get_or_create(
        order=order_one,
        species=species,
        quantinty=1,

    )[0]
