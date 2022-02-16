from ppadb.client import Client as AdbClient
import subprocess
from src.data.constants import LIB_DIR_WIN
from PIL import Image
import io
from src.data.constants import APP_WIDTH, APP_HEIGHT


class Adb:
    def __init__(self, emulator_port: int):
        self.adb_server_path = rf"{LIB_DIR_WIN}\adb\adb"
        self.init_adb_server(emulator_port)
        self.adb_client = AdbClient()
        self.emulator = self.adb_client.devices()[0]

    def init_adb_server(self, emulator_port: int):
        self.adb_server_command("kill-server")
        self.adb_server_command("start-server")

    def adb_server_command(self, command: str):
        subprocess.check_call(
            [self.adb_server_path, command],
            shell=True,
        )

    def take_screenshot(self):
        return Image.open(io.BytesIO(self.emulator.screencap()))


if __name__ == "__main__":
    adb = Adb(5555)
    jpeg = adb.take_screenshot()
    jpeg.save("screen.png")
