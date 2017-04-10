from wsgiref import simple_server
import cgi
import fnmatch
import static_files
import templating


def not_found(environ, start_response):
    start_response('404 Not Found', [('content-type', 'text/html')])
    return [
        """<html><h1>Page not Found</h1><p>That page is unknown. Return to the <a href="/">home page</a></p></html>""", ]


def one(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    return [templating.load_page({'content': 'The Content Of Page One'}, "one.html").encode('utf-8'), ]


def two(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    return [templating.load_page({'content': 'The Content Of Page Two'}, "two.html"), ]


def index(environ, start_response):
    start_response('200 OK', [('content-type', 'text/html')])
    return ["""<html>Index</html>""".encode('utf-8'), ]


routes = [('/static/*', static_files.make_static_application('/static/', 'static', not_found)),
          ('/one', one),
          ('/two', two),
          ('/', index),
          ]


def application(environ, start_response):
    for path, app in routes:
        if fnmatch.fnmatch(environ['PATH_INFO'], path):
            return app(environ, start_response)
    return not_found(environ, start_response)


if __name__ == '__main__':
    server = simple_server.make_server('localhost', 8080, application)
    print("Listening for requests on http://localhost:8080/")
    server.serve_forever()
