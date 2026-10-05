from passlib.context import CryptContext #importing CryptContext class from passlib that is used for managing passwords in python
from jose import jwt
from datetime import datetime, timedelta, timezone
import os


password_tool = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    hashed_password = password_tool.hash(password)
    return hashed_password


def verify_password(password_entered: str, password_from_database: str) -> bool:
    is_correct = password_tool.verify(
        password_entered,
        password_from_database
    )
    return is_correct

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )