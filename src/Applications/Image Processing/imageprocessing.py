import time

from PIL import Image, ImageDraw
from collections import Counter
import heapq
import sys
from time import sleep
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QIcon, QPixmap

MODE_RECTANGLE = 1
MODE_ELLIPSE = 2
MODE_ROUNDED_RECTANGLE = 3

MODE = MODE_RECTANGLE
ITERATIONS = 5024
LEAF_SIZE = 4
PADDING = 1
FILL_COLOR = (0, 0, 0)
SAVE_FRAMES = False
ERROR_RATE = 0.5
AREA_POWER = 0.25
OUTPUT_SCALE = 1


def weighted_average(hist):
    total = sum(hist)
    value = sum(i * x for i, x in enumerate(hist)) / total
    error = sum(x * (value - i) ** 2 for i, x in enumerate(hist)) / total
    error = error ** 0.5
    return value, error


def color_from_histogram(hist):
    r, re = weighted_average(hist[:256])
    g, ge = weighted_average(hist[256:512])
    b, be = weighted_average(hist[512:768])
    e = re * 0.2989 + ge * 0.5870 + be * 0.1140
    return (r, g, b), e


def rounded_rectangle(draw, box, radius, color):
    l, t, r, b = box
    d = radius * 2
    draw.ellipse((l, t, l + d, t + d), color)
    draw.ellipse((r - d, t, r, t + d), color)
    draw.ellipse((l, b - d, l + d, b), color)
    draw.ellipse((r - d, b - d, r, b), color)
    d = radius
    draw.rectangle((l, t + d, r, b - d), color)
    draw.rectangle((l + d, t, r - d, b), color)


class Quad(object):
    def __init__(self, model, box, depth):
        self.model = model
        self.box = box
        self.depth = depth
        hist = self.model.im.crop(self.box).histogram()
        self.color, self.error = color_from_histogram(hist)
        self.leaf = self.is_leaf()
        self.area = self.compute_area()
        self.children = []

    def is_leaf(self):
        l, t, r, b = self.box
        return int(r - l <= LEAF_SIZE or b - t <= LEAF_SIZE)

    def compute_area(self):
        l, t, r, b = self.box
        return (r - l) * (b - t)

    def split(self):
        l, t, r, b = self.box
        lr = l + (r - l) / 2
        tb = t + (b - t) / 2
        depth = self.depth + 1
        tl = Quad(self.model, (l, t, lr, tb), depth)
        tr = Quad(self.model, (lr, t, r, tb), depth)
        bl = Quad(self.model, (l, tb, lr, b), depth)
        br = Quad(self.model, (lr, tb, r, b), depth)
        self.children = (tl, tr, bl, br)
        return self.children

    def get_leaf_nodes(self, max_depth=None):
        if not self.children:
            return [self]
        if max_depth is not None and self.depth >= max_depth:
            return [self]
        result = []
        for child in self.children:
            result.extend(child.get_leaf_nodes(max_depth))
        return result


class Model(object):
    def __init__(self, path):
        self.im = Image.open(path).convert('RGB')
        self.width, self.height = self.im.size
        self.heap = []
        self.root = Quad(self, (0, 0, self.width, self.height), 0)
        self.error_sum = self.root.error * self.root.area
        self.push(self.root)

    @property
    def quads(self):
        return [x[-1] for x in self.heap]

    def average_error(self):
        return self.error_sum / (self.width * self.height)

    def push(self, quad):
        score = -quad.error * (quad.area ** AREA_POWER)
        heapq.heappush(self.heap, (quad.leaf, score, quad))

    def pop(self):
        return heapq.heappop(self.heap)[-1]

    def split(self):
        quad = self.pop()
        self.error_sum -= quad.error * quad.area
        children = quad.split()
        for child in children:
            self.push(child)
            self.error_sum += child.error * child.area

    def render(self, path, max_depth=None):
        m = OUTPUT_SCALE
        dx, dy = (PADDING, PADDING)
        im = Image.new('RGB', (self.width * m + dx, self.height * m + dy))
        draw = ImageDraw.Draw(im)
        draw.rectangle((0, 0, self.width * m, self.height * m), FILL_COLOR)
        for quad in self.root.get_leaf_nodes(max_depth):
            l, t, r, b = quad.box
            box = (l * m + dx, t * m + dy, r * m - 1, b * m - 1)

            # Convert box and color to ints. Python2 did this automatically
            box = tuple(int(v) for v in box)
            quad.color = tuple(int(v) for v in quad.color)

            if MODE == MODE_ELLIPSE:
                draw.ellipse(box, quad.color)
            elif MODE == MODE_ROUNDED_RECTANGLE:
                # Compute radius and convert to ints
                radius = int(m * min((r - l), (b - t)) / 4)
                rounded_rectangle(draw, box, radius, quad.color)
            else:
                draw.rectangle(box, quad.color)
        del draw
        im.save(path, 'PNG')


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Image Processing"
        self.setWindowTitle(self.title)
        self.setGeometry(10, 10, 1280, 960)

        vbox = QVBoxLayout(self)

        # Create widget
        self.label = QLabel(self)
        self.pixmap = QPixmap('maudy.jpg')
        self.label.setPixmap(self.pixmap)
        self.resize(self.pixmap.width(), self.pixmap.height())

        self.lineedit1 = QLineEdit(self)

        self.btn1 = QPushButton("Process Image", self)
        self.btn1.clicked.connect(self.calculate_image)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.lineedit1)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def calculate_image(self):
        model = Model("maudy.jpg")
        previous = None
        for i in range(int(self.lineedit1.text())):
            error = model.average_error()
            if previous is None or previous - error > ERROR_RATE:
                # print(i, error)
                if SAVE_FRAMES:
                    model.render('frames/%06d.png' % i)
                previous = error
            model.split()
            # time.sleep(3)
            # model.render(f'output{i}.png')
            self.label.setPixmap(QPixmap(model.render(f'output{i}.png')))
            self.resize(self.pixmap.width(), self.pixmap.height())
        model.render('output.png')
        self.label.setPixmap(QPixmap('output.png'))
        self.resize(self.pixmap.width(), self.pixmap.height())
        # print('-' * 32)
        # depth = Counter(x.depth for x in model.quads)
        # for key in sorted(depth):
        #     value = depth[key]
        #     n = 4 ** key
        #     pct = 100.0 * value / n
            # print('%3d %8d %8d %8.2f%%' % (key, n, value, pct))
        # print('-' * 32)
        # print('             %8d %8.2f%%' % (len(model.quads), 100))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication([])
    ex = Window()
    ex.show()
    # Start the event loop.
    sys.exit(app.exec())  # Zero is considered “successful termination”
