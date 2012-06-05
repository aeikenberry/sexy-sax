#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from twilio.rest import TwilioRestClient
import os
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')

        template_values = {
		            # Nothing to pass here
		        }
            
        self.response.out.write(template.render(path, template_values))

    def post(self):
          thenumber = self.request.get("number")
          ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
          AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
          client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
          call = client.calls.create(thenumber, from_="YOUR_TWILIO_PHONE_NUMBER", url="http://url.to/your.xml")

          template_values = {
		            # Nothing to pass here
		        }
		
          path = os.path.join(os.path.dirname(__file__), 'called.html')
          self.response.out.write(template.render(path, template_values))

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
