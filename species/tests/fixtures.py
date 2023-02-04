import pytest
from species.models import Species, Size, Category, Enviroment


@pytest.fixture
def category():
    return Category.objects.get_or_create(
        name='Spider'
    )[0]


@pytest.fixture
def size():
    return Size.objects.get_or_create(
        name='Small'
    )[0]


@pytest.fixture
def enviroment():
    return Enviroment.objects.get_or_create(
        name='Indoor'
    )[0]


@pytest.fixture
def species(category, size, enviroment):
    return Species.objects.get_or_create(
        name='Harry Larry',
        price=20.11,
        latin_name='Spiderus Wlochatus',
        description='very long and descriptive \
            comment about habits of this dangerous spider',
        dangerous_species=True,
        category=category,
        size=size,
        enviroment=enviroment
    )[0]
