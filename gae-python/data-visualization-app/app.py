import webapp2

class ShowHome(webapp2.RequestHandler):
    def get(self):
        ## Code to render home page

## Here is the WSGI application instance that routes requests

application = webapp2.WSGIApplication([
    ('/', ShowHome),
], debug=True)
