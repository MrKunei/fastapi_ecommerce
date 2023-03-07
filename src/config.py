from dotenv import load_dotenv
import os


load_dotenv()


class Settings:

    DB_HOST = os.environ.get('DB_HOST')
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_PORT = os.environ.get('DB_PORT')

    DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    SECRET_AUTH = os.environ.get('SECRET_AUTH')

    CART_SESSION_ID = os.environ.get('CART_SESSION_ID')


settings = Settings()
