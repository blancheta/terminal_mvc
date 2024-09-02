import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Customer, Contract

@pytest.fixture(autouse=True)
def mock_environment_variables(monkeypatch):
	monkeypatch.setenv("SQLALCHEMY_URL", "sqlite:///test/test.db")


@pytest.fixture
def engine(mocker):
    engine = create_engine("sqlite:///test.db", echo=True)
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture
def session(mocker, engine):
    session = Session(engine)
    return session

@pytest.fixture
def new_customer(session):
    customer = Customer(
        email_address="john@doe.fr",
    )
    session.add(customer)
    session.commit()
    session.refresh(customer)
    session.close()
    return customer

@pytest.fixture
def new_contract(session, new_customer):
    contract = Contract(
        name="contract #1",
        customer=new_customer,
    )
    session.add(contract)
    session.commit()
    session.refresh(contract)
    session.close()
    return contract


@pytest.fixture(autouse=True)
def drop_db(engine):
    yield
    os.remove("test.db")
