from src.source.image import Image as ImageSource
from src.source.video import Video as VideoSource
from src.source.application_window import ApplicationWindow as ApplicationWindowSource
from src.source.base import Base as BaseSource

from src.processor.processor import Processor

from src.out.base import Base as BaseOut
from src.out.image import Image as ImageOut
from src.out.video import Video as VideoOut
import cv2


class Application:

    def __init__(self, source: BaseSource, processor: Processor, out: BaseOut):
        self._source = source
        self._processor = processor
        self._out = out

    def run(self):
        frame = self._source.get_current_frame()
        result_data = self._processor.process(frame)
        self._out.show_result(result_data)

    def destroy(self):
        self._source.destroy()
        self._out.destroy()


if __name__ == "__main__":

    app = Application(

        # ImageSource('../sample_data/screenshot.png'),
        # VideoSource('../sample_data/sample2.mp4'),
        # VideoSource('/dev/video0')
        ApplicationWindowSource(),
        Processor(),
        # ImageOut()
        VideoOut()
    )

    while True:
        app.run()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    app.destroy()