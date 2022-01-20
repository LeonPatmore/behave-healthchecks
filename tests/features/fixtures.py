import threading
from time import sleep

import flask
from behave import fixture
from flask import jsonify
from werkzeug.serving import make_server

_PORT = 58179
APP = None  # type: MockServer or None


class MockServer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        app = flask.Flask(__name__)

        def started():
            self.started = True
            return jsonify(success=True)

        app.add_url_rule("/abc123/start", methods=["POST"], view_func=started)
        self.server = make_server('127.0.0.1', _PORT, app)
        self.ctx = app.app_context()
        self.ctx.push()

        self.started = False

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

    def ping_started(self) -> bool:
        print (self.started)
        return self.started


@fixture
def start_mock_server(context, **kwargs):
    global APP
    APP = MockServer()
    APP.start()

    yield

    stop_mock_server()


def stop_mock_server():
    if APP is None:
        return
    APP.shutdown()
    APP.join(timeout=5)


if __name__ == '__main__':
    start_mock_server({})

