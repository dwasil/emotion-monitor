from src.source.console import Console as ConsoleSource
from src.source.base import Base as BaseSource

from src.processor.processor import Processor

from src.out.base import Base as BaseOut
from src.out.image import Image as ImageOut


class Application:

    def __init__(self, source: BaseSource, processor: Processor, out: BaseOut):
        self._source = source
        self._processor = processor
        self._out = out

    def run(self):
        frame = self._source.get_current_frame()
        result_data = self._processor.process(frame)
        self._out.show_result(result_data)


if __name__ == "__main__":

    app = Application(
        ConsoleSource('../sample_data/screenshot.png'),
        Processor(),
        ImageOut()
    )

    app.run()
