f
import pytest
from ..models import Supplier, PurchaseInvoice


@pytest.fixture
def supplier():
    return Supplier.objects.get_or_create(
        name='Jumping spider suppliers'
    )[0]

@pytest.fixture
def purchase_invoice():
    return PurchaseInvoice.objects.get_or_create(
        invoice_number='15/2022',
        date_issued=
        total_net=15,
        VAT_percentage
        suplier
        delivery_date
        invoice_due_date
        paid=True
    )[0]
