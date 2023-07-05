from collections import namedtuple

import pytest

from laconiq import make

from .schema import DocumentNode, Node, OCRStatusEnum, Tag, User


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


def title_generator(items):
    for item in items:
        yield item


def test_make_two_node_instances():
    nodes = make(Node, _quantity=2)

    assert len(nodes) == 2
    assert all([
     isinstance(node, Node) for node in nodes
    ])


def test_make_one_node():
    node = make(Node)

    assert isinstance(node, Node)
    assert isinstance(node.tags, list)
    assert isinstance(node.tags[0], Tag)


def test_make_2_instances_with_custom_fields():
    nodes = make(Node, _quantity=2, ctype="folder", title="X")

    assert len(nodes) == 2
    assert ["X", "X"] == [item.title for item in nodes]


def test_make_3_instances_with_custom_fields():
    nodes = make(
        Node,
        _quantity=3,
        ctype="folder",
        title=title_generator(["X1", "X2", "X3"])
    )

    assert len(nodes) == 3
    assert {"X1", "X2", "X3"} == set([item.title for item in nodes])


def test_make_enum():
    status = make(OCRStatusEnum)

    assert isinstance(status, OCRStatusEnum)


def test_make_two_enum():
    statuses = make(OCRStatusEnum, _quantity=2)

    assert len(statuses) == 2
    assert all([
     isinstance(status, OCRStatusEnum) for status in statuses
    ])


def test_make_document_node():
    doc_node = make(DocumentNode)

    assert isinstance(doc_node, DocumentNode)
