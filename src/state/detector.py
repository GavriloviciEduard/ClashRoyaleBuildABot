import os

from PIL import ImageDraw, ImageFont

from src.state.card_detector import CardDetector
from src.state.number_detector import NumberDetector
from src.state.unit_detector import UnitDetector
from src.state.screen_detector import ScreenDetector
from src.data.constants import DATA_DIR, SCREENSHOTS_DIR


class Detector:
    def __init__(self, card_names, debug=False):
        if len(card_names) != 8:
            raise ValueError('You must specify all 8 of your cards')

        self.card_names = card_names
        self.debug = debug

        self.font = None
        if self.debug:
            os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
            self.font = ImageFont.load_default()

        self.card_detector = CardDetector(self.card_names)
        self.number_detector = NumberDetector(f'{DATA_DIR}/number.onnx')
        self.unit_detector = UnitDetector(f'{DATA_DIR}/unit.onnx')
        self.screen_detector = ScreenDetector()

    def _draw_text(self, d, bbox, text):
        text_width, text_height = self.font.getsize(text)
        x = (bbox[0] + bbox[2] - text_width) / 2
        y = bbox[3] + 2
        for xy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            d.text(xy, text=text, fill='black')
        d.text((x, y), text=text)

    def run(self, image):
        state = {'units': self.unit_detector.run(image),
                 'numbers': self.number_detector.run(image),
                 'cards': self.card_detector.run(image),
                 'screen': self.screen_detector.run(image)}

        if self.debug:
            d = ImageDraw.Draw(image)

            for k, v in state['numbers'].items():
                d.rectangle(tuple(v['bounding_box']))
                self._draw_text(d, v['bounding_box'], str(v['number']))

            for k, v in state['units'].items():
                for i in v:
                    d.rectangle(tuple(i['bounding_box']))
                    self._draw_text(d, i['bounding_box'], k)

            save_path = os.path.join(SCREENSHOTS_DIR, f"{len(os.listdir(SCREENSHOTS_DIR)) + 1}.jpg")
            image.save(save_path)

        return state
