from views import get_contract_details, display_contract_details


class TestContractViews:

    def test_get_contract_details(self, mocker):

        mocker.patch("builtins.input",
            side_effect=["contract #1", "apple"]
        )

        details = get_contract_details()
        assert details == {"name": "contract #1", "customer": "apple"}


    def test_display_contract_details(self, capsys, new_contract):
        display_contract_details(new_contract)

        captured = capsys.readouterr()
        assert f"{new_contract.name} - {new_contract.customer.email_address}" in captured.out
