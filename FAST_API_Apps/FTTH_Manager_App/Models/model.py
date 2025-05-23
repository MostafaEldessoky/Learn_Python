from sqlmodel import SQLModel, Field, Relationship, select, Session
from typing import List


class address_passive_customer_with_active(SQLModel, table=True):

    id: int = Field(primary_key=True, unique=True)
    address_passive_with_customer_id: int = Field(
        ..., foreign_key="address_passive_with_customer.id"
    )
    active_ports_id: int = Field(..., foreign_key="active_ports.id")


# -------------------------------------------------------------------------------------------------
class address_passive_with_customer(SQLModel, table=True):

    id: int = Field(primary_key=True, unique=True)
    address_with_passive_id: int = Field(..., foreign_key="address_with_passive.id")
    customer_id: int = Field(..., foreign_key="customers.username")

    port_to_customers: "active_ports" = Relationship(
        back_populates="customers_on_port",
        link_model=address_passive_customer_with_active,
    )


# -------------------------------------------------------------------------------------------------
class address_with_passive(SQLModel, table=True):

    id: int = Field(primary_key=True, unique=True)
    passive_id: int = Field(..., primary_key=True, foreign_key="sub_passive_boxs.id")
    address_id: int = Field(..., primary_key=True, foreign_key="addresses.id")

    address_of_customers: List["customers"] = Relationship(
        back_populates="customer_address", link_model=address_passive_with_customer
    )


# -------------------------------------------------------------------------------------------------
class addresses(SQLModel, table=True):

    id: int = Field(primary_key=True, unique=True)
    exchange: str = Field(..., index=True)
    region: str = Field(..., index=True)
    streat: str = Field(..., index=True)
    building: str = Field(..., index=True)
    floor: int = None

    passive: "sub_passive_boxs" = Relationship(
        back_populates="address", link_model=address_with_passive
    )


# -------------------------------------------------------------------------------------------------
class main_passive_boxs(SQLModel):

    id: int = Field(primary_key=True, unique=True)
    cabinet: str = Field(None, index=True)
    splitter_id: int = Field(None, index=True)
    main_box: str = Field(None, index=True)
    main_box_space: int = None
    main_ready: bool = False


class sub_passive_boxs(main_passive_boxs, table=True):

    sub_box: str = Field(None, index=True)
    sub_box_space: int = None
    sub_ready: bool = False

    address: addresses = Relationship(
        back_populates="passive", link_model=address_with_passive
    )


# -------------------------------------------------------------
class customers(SQLModel, table=True):

    username: str = Field(primary_key=True, foreign_key="users.username", unique=True)
    name: str
    mobile: str
    tel: str

    customer_address: address_with_passive = Relationship(
        back_populates="address_of_customers", link_model=address_passive_with_customer
    )


# -------------------------------------------------------------------------------------------------
class active_ports(SQLModel, table=True):

    id: int = Field(primary_key=True, unique=True)
    msan: str = Field(None, index=True)
    card: int = Field(None, index=True)
    port: int = Field(None, index=True)
    card_ready: bool = False

    customers_on_port: List[address_passive_with_customer] = Relationship(
        back_populates="port_to_customers",
        link_model=address_passive_customer_with_active,
    )


# -------------------------------------------------------------------------------------------------


def add_address(session: Session, address: addresses) -> None:
    session.add(address)
    session.commit()
    session.refresh(address)


def get_all_addresses(session: Session, exchange: str) -> List[addresses]:
    return session.exec(select(addresses).where(addresses.exchange == exchange)).all()


def search_for_address(
    session: Session, exchange: str, region: str, streat: str, building: str, floor: int
) -> List[addresses]:
    return session.exec(
        select(addresses)
        .where(addresses.exchange == exchange)
        .where(addresses.region == region)
        .where(addresses.streat == streat)
        .where(addresses.building == building)
        .where(addresses.floor == floor)
    ).first()


def add_passive_project():
    pass


def update_passive_project():
    pass


def search_for_ready_passive_projects():
    pass


def assign_customer_to_port():
    pass


def get_all_customers_on_port():
    pass


def get_all_customers_on_box():
    pass
