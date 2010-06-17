"""
This is a manual script to run the django server.

You can use it in your programs to fire up the plotting server. Just call it
like this:

>>> from plotserver.runserver import main
>>> main()

"""

def main():
    import os
    import sys

    sys.path.insert(0, "..")
    os.environ['DJANGO_SETTINGS_MODULE'] = "plotserver.settings"

    from django.core.servers.basehttp import run, AdminMediaHandler, WSGIServerException
    from django.core.handlers.wsgi import WSGIHandler

    addr = '127.0.0.1'
    port = '8000'
    admin_media_path = ''
    try:
        handler = AdminMediaHandler(WSGIHandler(), admin_media_path)
        print "Server is running at http://%s:%s/" % (addr, port)
        print "Quit the server with CONTROL-C."

        run(addr, int(port), handler)
    except WSGIServerException, e:
        # Use helpful error messages instead of ugly tracebacks.
        ERRORS = {
            13: "You don't have permission to access that port.",
            98: "That port is already in use.",
            99: "That IP address can't be assigned-to.",
        }
        try:
            error_text = ERRORS[e.args[0].args[0]]
        except (AttributeError, KeyError):
            error_text = str(e)
        sys.stderr.write(self.style.ERROR("Error: %s" % error_text) + '\n')
        # Need to use an OS exit because sys.exit doesn't work in a thread
        os._exit(1)
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
