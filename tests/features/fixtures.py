import logging
import threading

import flask
from behave import fixture
from flask import jsonify
from werkzeug.serving import make_server

_PORT = 58179


class MockServer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        app = flask.Flask(__name__)

        def started():
            logging.info("Ping start detected!")
            self.started = True
            return jsonify(success=True)

        app.add_url_rule("/abc123/start", methods=["POST"], view_func=started)
        app.add_url_rule("/abc123", methods=["POST"], view_func=lambda: jsonify(success=True))
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
    logging.info("Starting mock server!")
    mock_server = MockServer()
    mock_server.start()

    context.mock_server = mock_server

    yield

    stop_mock_server(mock_server)


def stop_mock_server(mock_server: MockServer):
    logging.info("Stopping mock server!")
    mock_server.shutdown()
    mock_server.join(timeout=5)


if __name__ == '__main__':
    start_mock_server({})

