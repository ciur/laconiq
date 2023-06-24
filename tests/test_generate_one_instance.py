import pytest

from collections import namedtuple
from laconiq import generate_instance, make

from .schema import User


def test_generate_instance_basic():
    user = generate_instance(User)

    assert isinstance(user, User)
    assert isinstance(user.email, str)


def test_generate_instance_with_custom_field():
    user = generate_instance(User, email="john@doe.com")

    assert isinstance(user, User)
    assert user.email == "john@doe.com"


def test_generate_instance_for_non_pydantic_model():
    """Laconiq works only with pydantic models

    Given model/class which is not an instance of pydantic, will
    raise ValueError.
    Model is considered as being pydantic model if it has 'schema'
    class attribute
    """
    MyModel = namedtuple('NonPydanticModel', 'username, id')

    with pytest.raises(ValueError):
        generate_instance(MyModel)


def test_make():
    user = make(User)

    assert isinstance(user, User)
    assert isinstance(user.email, str)


def test_make_with_custom_field():
    user = make(User, email="john@doe.com")

    assert isinstance(user, User)
    assert user.email == 'john@doe.com'


def test_make_for_non_pydantic_model():
    MyModel = namedtuple('NonPydanticModel', 'username, id')

    with pytest.raises(ValueError):
        make(MyModel)
