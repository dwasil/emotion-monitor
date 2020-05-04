from .base import Base
from ..gui.target_choose_dialog import TargetChooseDialog


class ApplicationWindow(Base):

    def __init__(self, choose_dialog: TargetChooseDialog):
        self._choose_dialog = choose_dialog
        self._choose_dialog.show()

    def get_current_frame(self):
        return None
