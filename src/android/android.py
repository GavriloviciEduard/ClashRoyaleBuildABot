from src.android.adb import Adb
from src.android.bluestacks import Bluestacks

class Android:
    def __init__ (self):
        self.bluestacks = Bluestacks()
