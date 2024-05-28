from dotenv import load_dotenv
import os

load_dotenv('.env')

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
TEST_DATABASE_URL = f"postgresql://{os.getenv('DB_USER_TEST')}:{os.getenv('DB_PASSWORD_TEST')}@{os.getenv('DB_HOST_TEST')}:{os.getenv('DB_PORT_TEST')}/{os.getenv('DB_NAME_TEST')}"
