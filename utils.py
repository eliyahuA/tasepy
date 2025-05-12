from typing import TypeVar, Type, cast, Any

T = TypeVar('T')

def safe_cast(obj: Any, target_type: Type[T]) -> T:
    """
    Cast an object to a specific type with runtime checking.

    Args:
        obj: The object to cast
        target_type: The type to cast to

    Returns:
        The object, with type hints matching target_type

    Raises:
        TypeError: If the object is not an instance of target_type
    """
    # Handle type vs instance cases (for classes)
    if isinstance(target_type, type):
        # Check if obj is a type (for class objects)
        if isinstance(obj, type):
            if issubclass(obj, target_type):
                return cast(target_type, obj)
            else:
                raise TypeError(f"Type {obj.__name__} is not a subclass of {target_type.__name__}")
        # Check if obj is an instance
        elif isinstance(obj, target_type):
            return cast(target_type, obj)
        else:
            raise TypeError(f"Object of type {type(obj).__name__} cannot be cast to {target_type.__name__}")
    else:
        # Handle typing module's special types (List, Dict, etc.)
        if hasattr(target_type, "__origin__"):
            # This is an approximate check for generic types
            # A more accurate implementation would need to check __args__ as well
            if isinstance(obj, target_type.__origin__):
                return cast(target_type, obj)
            else:
                raise TypeError(f"Object of type {type(obj).__name__} cannot be cast to {target_type}")
        else:
            raise TypeError(f"Cannot cast to {target_type} - not a valid type")


if __name__ == '__main__':
    from models.endpoints import Endpoints
    from pydantic.fields import FieldInfo

    x = safe_cast(FieldInfo, type(Endpoints.model_fields['funds']))


