import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_USER = "postgres"
DB_PASSWORD = "postgres123"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "QA"

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


@pytest.fixture(scope="session")
def engine():
    eng = create_engine(DATABASE_URL, echo=False)
    yield eng
    eng.dispose()


@pytest.fixture
def session(engine):
    Session = sessionmaker(bind=engine)
    sess = Session()
    yield sess
    sess.close()
