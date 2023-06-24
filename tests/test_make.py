import pytest

from laconiq import make

from .schema import Node


def title_generator(items):
    for item in items:
        yield item


@pytest.mark.skip()
def test_make_2_instances():
    nodes = make(Node, _quantity=2)

    assert len(nodes) == 2


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
