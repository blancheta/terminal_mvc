from controllers import MainController


class TestContractController:
    def test_create_contract_controller(self, mocker):
        get_contract_details__mock = mocker.patch(
            "controller.get_contract_details"
        )
        create_contract_into_db_mock = mocker.patch(
            "controller.MainController.create_contract_record"
        )
        display_contract_details = mocker.patch(
            "controller.display_contract_details"
        )

        MainController().create_contract_controller()

        get_contract_details__mock.assert_called_once()
        create_contract_into_db_mock.assert_called_once()
        display_contract_details.assert_called_once()

