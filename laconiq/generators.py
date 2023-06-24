import string
import uuid
from datetime import datetime
from random import choice, randint


def gen_integer(min_int: int = 10, max_int: int = 1000) -> int:
    return randint(min_int, max_int)


def gen_string(max_length: int) -> str:
    return str(
        "".join(choice(string.ascii_letters) for _ in range(max_length))
    )


def gen_date_time() -> datetime:
    return datetime.now()


def gen_uuid() -> uuid.uuid4:
    return uuid.uuid4()


def gen_email() -> str:
    return f'{gen_string(5)}@example.com'


def gen_boolean() -> bool:
    return choice([True, False])


def generate_str(format: str) -> str | datetime | uuid.UUID:
    if format is None:
        return gen_string(10)
    elif format == 'date-time':
        return gen_date_time()
    elif format == 'uuid':
        return gen_uuid()
    elif format == 'email':
        return gen_email()
    else:
        raise ValueError(f"Unsupported format {format}")


def generate_for_type(_type: str, _format: str | None = None):
    if _type == 'string':
        return generate_str(_format)
    elif _type == 'integer':
        return gen_integer()
    elif _type == 'boolean':
        return gen_boolean()
    else:
        raise ValueError(f"Unsupported type {_type}")
