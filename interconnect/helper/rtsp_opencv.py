import cv2

from interconnect.helper.yolo_image_detection import yolo_img


def gen(source):
    while True:
        frame = source.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


class DataFeed(object):
    def __init__(self):
        self.url = cv2.VideoCapture("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov")

    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):
        success, imgNp = self.url.read()
        resize = cv2.resize(imgNp, (420, 240), interpolation=cv2.INTER_LINEAR)
        # ret, jpeg = cv2.imencode('.jpg', yolo_img(resize))
        ret, jpeg = cv2.imencode('.jpg', resize)
        return jpeg.tobytes()
