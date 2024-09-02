from models import Customer, Contract


class TestContractModels:

    def test_create_customer_record(self, new_customer):
        assert isinstance(new_customer, Customer)
        assert getattr(new_customer, "id")
        assert new_customer.email_address == "john@doe.fr"

    def test_create_contract_record(self, new_contract):
        assert isinstance(new_contract, Contract)
        assert getattr(new_contract, "id")
        assert new_contract.name == "contract #1"