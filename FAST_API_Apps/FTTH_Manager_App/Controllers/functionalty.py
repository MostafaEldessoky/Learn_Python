from fastapi import APIRouter, Depends
from sqlmodel import Session

from Models.model import add_address, addresses, get_all_addresses, search_for_address
from Services.db import db_session


router = APIRouter()


@router.post("/addaddress")
def addaddress(address: addresses, session: Session = Depends(db_session)):
    add_address(session, address)
    return "done"


@router.get("/getalladdresses")
def getalladdresses(exchange: str, session: Session = Depends(db_session)):
    return get_all_addresses(session, exchange)


@router.get("/getaddresses")
def getaddresses(
    exchange: str,
    region: str,
    streat: str,
    building: str,
    floor: int,
    session: Session = Depends(db_session),
):
    return search_for_address(session, exchange, region, streat, building, floor)
