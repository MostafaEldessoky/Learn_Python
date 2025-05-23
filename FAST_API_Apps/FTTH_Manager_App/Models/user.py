from typing import List
from sqlmodel import SQLModel, Field, Relationship, select, Session
from enum import Enum
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/log_in")


class roles(Enum):

    admin = "admin"
    customer = "customer"
    infrastructure_tech = "infrastructure_tech"
    installation_tech = "installation_tech"
    distribution_tech = "distribution_tech"


class user_func:

    def verification(token: str, endpoint_roles: List[str], session: Session) -> str:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if (
            session.exec(select(users).where(users.username == payload["username"]))
            .first()
            .is_active
        ):
            if payload["role"] in endpoint_roles:
                if datetime.fromtimestamp(payload["exp"]) < datetime.now():
                    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
                else:
                    return payload["username"]
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        else:
            raise HTTPException(status_code=status.HTTP_410_GONE)

    def update_password(session: Session, username: str, password: str) -> None:

        user: users = session.exec(
            select(users).where(users.username == username)
        ).first()

        if user:

            user.password = pwd_context.hash(user_func.password_validation(password))
            session.add(user)
            session.commit()
            session.refresh(user)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    def validate_role(role: str):
        if role not in roles.__dict__:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        else:
            return role

    def delete_account(session: Session, username: str) -> None:

        user: users = session.exec(
            select(users).where(users.username == username)
        ).first()
        session.delete(user)
        session.commit()

    def logout(username: str, session: Session) -> None:
        user: users = session.exec(
            select(users).where(users.username == username)
        ).first()
        user.is_active = False
        session.add(user)
        session.commit()
        session.refresh(user)

    def password_validation(password: str):
        if len(password) > 7 and len(password) < 12:
            return password
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)


class base_users(SQLModel):

    username: str = Field(..., primary_key=True, unique=True, index=True)
    password: str

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def login_user(self, session: Session):

        user: users = session.exec(
            select(users).where(users.username == self.username)
        ).first()

        if user:
            if pwd_context.verify(self.password, user.password):
                user.is_active = True
                session.add(user)
                session.commit()
                session.refresh(user)
                payload = {
                    "username": user.username,
                    "role": user.role,
                    "exp": datetime.now()
                    + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
                }
                return {
                    "access_token": jwt.encode(
                        payload, SECRET_KEY, algorithm=ALGORITHM
                    ),
                    "token_type": "bearer",
                }
            else:
                raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


class users(base_users, table=True):

    role: str
    is_active: bool

    def __init__(
        self,
        username: str,
        password: str,
        role: str = "customer",
        is_active: bool = True,
    ) -> None:
        super().__init__(
            username=username, password=user_func.password_validation(password)
        )
        self.role = user_func.validate_role(role)
        self.is_active = is_active

    def signin(self, session: Session) -> None:
        self.password = pwd_context.hash(str(self.password))
        session.add(self)
        session.commit()
        session.refresh(self)
