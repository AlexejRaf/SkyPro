from sqlalchemy import inspect
from db_config import engine


inspector = inspect(engine)

print("Таблицы в БД:")
for table in inspector.get_table_names():
    print(f"  - {table}")

print()

print("Колонки таблицы student:")
for column in inspector.get_columns("student"):
    print(f"  {column['name']} — {column['type']}")
