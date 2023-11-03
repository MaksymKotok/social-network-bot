from typing import Sequence, get_type_hints

def get_typedict_fields(typedict_class) -> Sequence[str]:
    return tuple(get_type_hints(typedict_class).keys())
