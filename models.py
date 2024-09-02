from typing import List
from typing import Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Contract(Base):
    __tablename__ = "contract"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id", ))
    customer: Mapped["Customer"] = relationship(
        backref="contracts", lazy='subquery'
    )

    def __repr__(self) -> str:
        return f"Contract(id={self.id!r}, name={self.name!r})"


class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]

    def __repr__(self) -> str:
        return f"Customer(id={self.id!r}, email_address={self.email_address!r})"
