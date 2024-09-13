from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

class SQLAlchemyFactory:
    def __init__(self, sql_uri: str):
        self.sql_engine = create_async_engine(sql_uri, echo=True)
        self.sql_session_factory = sessionmaker(
            bind=self.sql_engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    def get_session(self):
        return self.sql_session_factory()