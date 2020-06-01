from src.source.image import Image as ImageSource
from src.source.video import Video as VideoSource
from src.source.application_window import ApplicationWindow as ApplicationWindowSource
from src.source.base import Base as BaseSource

from src.processor.processor import Processor

from src.out.base import Base as BaseOut
from src.out.image import Image as ImageOut
from src.out.video import Video as VideoOut
from src.out.application_window import ApplicationWindow as ApplicationWindowOut
from src.out.application_twindow import ApplicationTWindow as ApplicationTWindowOut

import cv2
from src.sys.windows_enumerator import WindowsEnumerator
from src.gui.target_choose_dialog import TargetChooseDialog


class Application:

    def __init__(self, source: BaseSource, processor: Processor, out: BaseOut):
        self._source = source
        self._processor = processor
        self._out = out
        self._out2 = ImageOut()

    def run(self):

        frame = self._source.get_current_frame()

        if frame is None:
            return

        result_data = self._processor.process(frame)

        self._out.show_result(result_data)

    def destroy(self):
        self._source.destroy()
        self._out.destroy()


def run_application(window):

    app = Application(
        # ImageSource('../sample_data/screenshot.png'),
        # VideoSource('../sample_data/sample2.mp4'),
        # VideoSource('/dev/video0')
        ApplicationWindowSource(window),
        Processor(),
        # ImageOut()
        ApplicationTWindowOut(window)
    )

    while True:
        app.run()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    app.destroy()


if __name__ == "__main__":

    target = TargetChooseDialog(
        run_application
    )

    target.show()
