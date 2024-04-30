#!/usr/bin/python3
""" fetch https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        form = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(form)))
        print("\t- content: {}".format(form))
        print("\t- utf8 content: {}".format(form.decode("utf-8")))
