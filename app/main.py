import alive_detector
import tplink
import webapp2
from requests_toolbelt.adapters import appengine
appengine.monkeypatch()


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Miner Waker - Server Working')


class Check(webapp2.RequestHandler):
    def get(self):
        """Check and reset down miners."""

        print 'Check started...'

        rigs = alive_detector.miners_alive()

        response = ''

        for rig in rigs:
            if rig['alive'] is False:
                output = 'Rig ' + rig['name'] + ' is down. Starting reset...'
                response += output + '\n'
                print output
                tplink.reset(rig['name'])

        print 'Check finished'

        if response == '':
            response = 'Miners OK'

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/check', Check)
], debug=False)
