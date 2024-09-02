def get_client_details():

    details = {}

    for info in ["email_address"]:
        details[info] = input(f"Enter a value for {info}")

    return details




def get_contract_details():

    details = {}

    for info in ["name", "customer"]:
        details[info] = input(f"Enter a value for {info}")

    return details

def display_contract_details(contract_details):
    print("Details of the contract")
    print(f"{contract_details.name} - {contract_details.customer.email_address}")
