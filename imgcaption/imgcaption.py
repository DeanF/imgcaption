import json
import mimetypes
import os

import requests
from six.moves.urllib.parse import urljoin

CAPTIONBOT_API = 'https://www.captionbot.ai/api/'


class API(object):
    def __init__(self):
        self.session = requests.Session()
        self.watermark = ''
        self.conversation_id = self._make_api_request('init')

    def _make_api_request(self, endpoint, method='GET', **kwargs):
        res = self.session.request(method,
                                   urljoin(CAPTIONBOT_API, endpoint),
                                   **kwargs)
        print(res.json())
        return res.json()

    def _send_message(self, message):
        res = self._make_api_request(
            'message', method='POST',
            headers={'Content-Type': 'application/json'},
            json={
                'userMessage': message,
                'conversationId': self.conversation_id,
                'waterMark': self.watermark
            }
        )
        res = json.loads(res)
        self.watermark = res.get('WaterMark', self.watermark)
        return res

    def get_url_caption(self, url):
        res = self._send_message(url)
        return res.get('UserMessage')

    def get_file_caption(self, fp, filename):
        mime_type, _ = mimetypes.guess_type(filename)
        files = {'file': (os.path.basename(filename), fp, mime_type)}
        img_url = self._make_api_request('upload', method='POST', files=files)
        return self.get_url_caption(img_url)

    def get_filepath_caption(self, filepath):
        with open(filepath, mode='rb') as fp:
            return self.get_file_caption(fp, filepath)

    def send_score(self, score):
        return self._send_message(score)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
