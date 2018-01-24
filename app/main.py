import alive_detector
import tplink
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Miner Waker - Server Working')


class Check(webapp2.RequestHandler):
    def get(self):
        """Check and reset down miners."""

        print 'Check started...'

        rigs = alive_detector.miners_alive()

        for rig in rigs:
            if rig['alive'] is False:
                print 'Rig ' + rig['name'] + ' is down. Starting reset...'
                tplink.reset(rig['name'])

        print 'Check finished'

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Done')


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=False)

check = webapp2.WSGIApplication([
    ('/check', Check)
], debug=False)
