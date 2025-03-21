"""Various Validators"""


def validate_integer(
        arg_name, arg_value, min_value=None, max_value=None,
        custom_min_message=None, custom_max_message=None
):
    """Validates that 'arg_value' is an integer, and optionally falls within specific
    bounds.
    A custom override error message can be provided when mix/max bounds are exceeded

    Args:
        arg_name (str): _description_
        arg_value (obj): _description_
        min_value (int, optional): _description_. Defaults to None.
        max_value (int, optional): _description_. Defaults to None.
        custom_min_message (str, optional): _description_. Defaults to None.
        custom_max_message (str, optional): _description_. Defaults to None.
    
    Returns: 
        None: no exceptions raised if validation passes

    Raises:
        TypeError: if 'arg_value' is not an integer
        ValueError: if 'arg_value' does not satisfy the bounds 
    """
    if not isinstance(arg_value, int):
        raise TypeError(f'{arg_name} must be an integer.')
    
    if min_value is not None and arg_value < min_value:
        if custom_min_message is not None:
            raise ValueError(custom_min_message)
        raise ValueError(f'{arg_name} cannot be less than {min_value}')

    if max_value is not None and arg_value > max_value:
        if custom_max_message is not None:
            raise ValueError(custom_max_message)
        raise ValueError(f'{arg_name} cannot be greater than {max_value}')
