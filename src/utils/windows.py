import winreg
from typing import Optional


def get_registry_value(key: int, sub_key: str, value_name: str) -> Optional[str]:
    """Get registry value for key->sub_key.

    Args:
        key (int): key to be searched.
        sub_key (str): subkey of key.
        value_name (str): value name for subkey.

    Returns:
        Optional[str]: value for key->sub_key or None.
    """

    try:
        with winreg.OpenKey(
            key,
            sub_key,
            access=winreg.KEY_READ,
        ) as registry_key:
            value, regtype = winreg.QueryValueEx(registry_key, value_name)
            return value
    except WindowsError as err:
        # todo: log error
        return None
