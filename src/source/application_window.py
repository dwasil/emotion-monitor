from .base import Base
from ..gui.target_choose_dialog import TargetChooseDialog


class ApplicationWindow(Base):

    def __init__(self):
        self._choose_dialog = TargetChooseDialog()
        self._choose_dialog.show(('window1', 'window2'))

    def get_current_frame(self):
        return None
