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
import caesar
import cgi

def page_builder(message):
    
    header = """
    <h2> Web Caesar </h2>
    """

    form = """
    <form method = "post">
        <p> What message would you like to encrypt? </p>
        <textarea name = "message">%s</textarea>
        <br>
        <p> By how many units do you wish to rotate the message? </p>
        <input type = "text" name = "rotations">
        <br>
        <input type = "submit">
    </form>
    """
    return header + form % message

class MainHandler(webapp2.RequestHandler):
    def get(self):
        blank_page = page_builder("")
        self.response.write(blank_page)

    def post(self):
        message = self.request.get("message")
        
        rotations = int(self.request.get("rotations"))
        encrypted_message = caesar.encrypt(message, rotations)
        
        escaped_encrypted_message = cgi.escape(encrypted_message)
        results_page = page_builder(escaped_encrypted_message)
        
        self.response.write(results_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
