from .base import Base


class Console(Base):

    def show_result(self, result_data):
        print(str(result_data))
