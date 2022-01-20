from mock_server.application import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define

define("address", default="localhost", help="run on the given address")
define("port", default=8888, help="run on the given port", type=int)
define("dir", help="dir with api definitions")
define("debug", help="", default=False, type=bool)
define("application_data", help="Application data file",
       default="application.json")
define("num_processes", help="Number of child processes", default=1, type=int)
define("custom_provider", help="Custom response provider")


def main():
    app = Application(6780, "0.0.0.0", "/api", True, "")
    print("Serving on %s:%s.." % (options.address, options.port))

    server = HTTPServer(app)
    server.bind(options.port, options.address)
    server.start(options.num_processes)
    IOLoop.instance().start()
