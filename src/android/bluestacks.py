import platform
from src.data.constants import BLUESTACKS_REG_PATH, BLUESTACKS_EXE_NAME
from src.utils.windows import get_registry_value
import winreg
from typing import Optional


class BlueStacks:
    def __init__(self):
        self.platform = platform.system()
        self.path = self._get_path()

    def _get_path(self) -> Optional[str]:
        """Get bluestacks path.

        Returns:
            Optional[str]: Bluestacks path or None.
        """

        if self.platform == "Windows":
            return self._get_path_windows()
        elif self.platform == "Linux":
            # todo: implement
            return None
        elif self.platform == "Darwin":
            # todo: implement
            return None

    def _get_path_windows(self) -> Optional[str]:
        """Get bluestacks path for Windows.

        Returns:
            Optional[str]: Bluestacks path for Windows or None.
        """

        install_dir = get_registry_value(
            winreg.HKEY_LOCAL_MACHINE,
            BLUESTACKS_REG_PATH,
            "InstallDir",
        )
        if install_dir is not None:
            return f"{install_dir}{BLUESTACKS_EXE_NAME}"
        return None
