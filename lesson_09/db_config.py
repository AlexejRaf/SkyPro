from sqlalchemy import create_engine


DB_USER = "postgres"
DB_PASSWORD = "postgres123"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "QA"

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("Подключение к БД успешно!")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
