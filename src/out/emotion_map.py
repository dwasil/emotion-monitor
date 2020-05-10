def _RGB(r: int, g: int, b: int):
    return b + (g << 8) + (r << 16)

class EmotionMap:

    map = [
        ['angry', _RGB(255, 0, 0)],
        ['disgust', _RGB(153, 76, 0)],
        ['fear', _RGB(25, 51, 0)],
        ['happy', _RGB(255, 255, 0)],
        ['sad', _RGB(76, 0, 153)],
        ['surprise', _RGB(51, 153, 255)],
        ['neutral', _RGB(128, 128, 128)],
        ['unknown', _RGB(0, 0, 0)]
    ]