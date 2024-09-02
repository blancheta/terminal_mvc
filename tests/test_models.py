from sqlalchemy.util import merge_lists_w_ordering

from controllers import MainController
from models import Customer, Contract


class TestContractModels:

    def test_create_customer_record(self):

        customer_obj = MainController.create_customer_record({
            "email_address": "john@doe.fr"
        })
        assert isinstance(customer_obj, Customer)
        assert getattr(customer_obj, "id")
        assert customer_obj.email_address == "john@doe.fr"

    def test_create_contract_record(self, new_customer):
        contract_obj = MainController.create_contract_record({
            "name": "contact #1",
            "customer": new_customer
        })

        assert isinstance(contract_obj, Contract)
        assert getattr(contract_obj, "id")
        assert contract_obj.name == "contract #1"