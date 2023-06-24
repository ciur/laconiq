import types

from laconiq.generators import generate_for_type


def generate_instance(model_klass, **desired_instance_attrs):
    """Generates one instance of given pydantic model class"""

    # model is considered pydantic if it has 'schema' class attr
    if not hasattr(model_klass, 'schema'):
        raise ValueError("Non pydantic model")

    attrs = {}

    for prop, value in model_klass.schema()['properties'].items():
        if prop in desired_instance_attrs.keys():
            attrs[prop] = desired_instance_attrs.get(prop)
        else:
            if 'type' in value:
                attrs[prop] = generate_for_type(
                    value.get('type'),
                    value.get('format', None)
                )
            else:
                # e.g. $ref, which is not yet implemented
                pass

    return model_klass(**attrs)


def make(model_klass, _quantity=1, **desired_instance_attrs):

    gen_attrs = {}
    result = []

    if _quantity > 1:
        for key, value in desired_instance_attrs.items():
            if isinstance(value, types.GeneratorType):
                gen_attrs[key] = list(value)

        for idx in range(0, _quantity):
            for attr_name, _list in gen_attrs.items():
                desired_instance_attrs[attr_name] = _list[idx]
            result.append(
                generate_instance(model_klass, **desired_instance_attrs)
            )

        return result

    return generate_instance(model_klass, **desired_instance_attrs)
