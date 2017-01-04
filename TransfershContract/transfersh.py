#!/usr/bin/python
from gi.repository import Gtk, Gdk, Notify
import sys
import urllib2
import requests
import os


class TransfershUploader:
    def __init__ (self, args):

        files = []

        # Initialize the notification daemon
        Notify.init ("Transfer.sh")

        # Parse arguments
        if len (args) == 1:
            return
        else:
            for file in args:
                if file == args[0] or file == "":
                    continue
                files.append (file)

        self.paste_them_bad_boys (files)

    def notify (self, message_one, message_two, icon):
        try:
            notification = Notify.Notification.new (message_one, message_two, icon)
            notification.set_urgency (1)
            notification.show ()
            del notification
        except:
            pass

    def paste_them_bad_boys (self, files):
        urls = []

        for file in files:
		_, filename = os.path.split(file)
		upload_url = "http://transfer.sh/" + filename
		r = requests.put(upload_url, files={filename: open(file, 'rb')})
		urls.append(r.text)

        # Copy to clipboard
        url_list = ", ".join (urls)
        print url_list
        self.set_clipboard (url_list)
        if len (urls) > 1:
            self.notify (
                "Your files have been uploaded.", 
                "The links have been copied to your clipboard!", 
                "document-save"
            )
        else:
            self.notify (
                "Your file has been uploaded.", 
                "The link has been copied to your clipboard!", 
                "document-save"
            )

    def set_clipboard (self, url_list):
        display   = Gdk.Display.get_default()
        selection = Gdk.Atom.intern ("CLIPBOARD", False)
        clipboard = Gtk.Clipboard.get_for_display (display, selection)
        clipboard.set_text (url_list, -1)
        clipboard.store ()

if __name__ == '__main__':
    uploader = TransfershUploader (sys.argv)
