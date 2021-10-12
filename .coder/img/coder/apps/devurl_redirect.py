#!/usr/bin/env python3

# put this in /coder/apps/devurl_redirect.py

import os, sys, re, requests, argparse

from http.server import HTTPServer, BaseHTTPRequestHandler

# arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--listen-port", dest = "listen_port", default=8888, type=int)
parser.add_argument("-r", "--redirect-port", dest = "redirect_port", default=8888, type=int)
# TODO: impliment parser.add_argument("-n", "--devurl_name", dest = "devurl_name")
parser.add_argument("-s", "--start-command", dest = "start_command", default="false")

args = parser.parse_args()

# get Dev URL host
response = requests.get(
    os.environ.get('CODER_URL') + '/api/private/devurls/host',
    headers={'Session-Token': os.environ.get('CODER_AGENT_TOKEN')},
)

# start the application, if passed through
if args.start_command != "false":
    import subprocess
    subprocess.Popen(args.start_command.split ( ), close_fds=False)

class Redirect(BaseHTTPRequestHandler):

    def do_HEAD(self):
        # for Coder health checks
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        # redirect to proper dev URL :)

        # also for health check
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes("All OK", "utf8"))
            return
        
        try:
            devurl_host = response.json()['devurl_host']
        except:
            # will fail if non 200 status code
            # or if dev url host is empty

            # dev URL not found
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            self.wfile.write(bytes("Error: Could not get Dev URL host. After fixing, you may need to rebuild this workspace", "utf8"))
            return

        # check if the access URL is http or https :)
        if os.environ.get('CODER_URL').find("https") != -1:
            schema="https"
        else:
            schema="http"
        
        # Redirect to the proper dev URL
        url = ("% s://% s-% s-% s.% s" % (schema, args.redirect_port, os.environ.get('CODER_ENVIRONMENT_NAME'), os.environ.get('CODER_USERNAME'), devurl_host))
        print ("Redirecting to " + url)
        self.send_response(302)
        self.send_header('Location', url)
        self.end_headers()


print("Starting redirect server on port", args.listen_port)
HTTPServer(("", int(args.listen_port)), Redirect).serve_forever()