from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session

from models import Base, Contract, Customer
from views import get_contract_details, display_contract_details

engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)


class MainController:


    @classmethod
    def create_customer_record(cls, customer_details: dict):
        session = Session(engine)
        customer = Customer(
            email_address=customer_details["email_address"],
        )
        session.add(customer)
        session.commit()
        session.refresh(customer)
        session.close()
        return customer

    @classmethod
    def create_contract_record(cls, contract_details: dict):
        session = Session(engine)
        contract = Contract(
            name=contract_details["name"],
            customer=contract_details["customer"],
        )
        session.add(contract)
        session.commit()
        session.refresh(contract)
        session.close()
        return contract

    @classmethod
    def create_contract_controller(cls):
        details = get_contract_details()
        contract = cls.create_contract_record(details)
        display_contract_details(contract)

    @classmethod
    def main(cls):
         cls.create_contract_controller()
