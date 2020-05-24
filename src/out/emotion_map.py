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

    map2 = [
        ['angry', [1, 0, 0, 1]],
        ['disgust', [0.6, 0.3, 0, 1]],
        ['fear', [0.1, 0.2, 0, 1]],
        ['happy', [1, 1, 0, 1]],
        ['sad', [0.3, 0, 0.6, 1]],
        ['surprise', [0.2, 0.6, 1, 1]],
        ['neutral', [0.5, 0.5, 0.5, 1]],
        ['unknown', [0, 0, 0, 1]]
    ]