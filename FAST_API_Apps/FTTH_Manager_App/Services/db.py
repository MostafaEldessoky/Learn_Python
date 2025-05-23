from sqlmodel import create_engine, Session, SQLModel

url = ""

engine = create_engine(url=url)


async def start_db():
    SQLModel.metadata.create_all(engine)


async def db_session():
    with Session(engine) as session:
        yield session
