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
import webapp2
import logging

total = 0
hits = 0

class MainHandler(webapp2.RequestHandler):
	def get(self):
		global total
		global hits
		logging.info("Reporting...")
		self.response.write(float(hits)/total*4)


class PostHandler(webapp2.RequestHandler):
	def post(self):
		global total
		global hits
		logging.info("Adding...")
		total += int(self.request.get('total'))
		hits  += int(self.request.get('hits'))
		self.response.write(float(hits)/total*4)

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/totals', PostHandler)
], debug=True)
