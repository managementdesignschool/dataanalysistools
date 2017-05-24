#!/usr/bin/env python

# Data Anabkysus

import pygtk
pygtk.require('2.0')
import gtk

class DataAnalysis:

    def dataanalysis(self, widget, data=None):
        print "Data Analysis"

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    
        self.window.connect("delete_event", self.delete_event)
    
        self.window.connect("destroy", self.destroy)
    
        self.window.set_border_width(10)
    
        self.button = gtk.Button("Data Analysis Tool")
    
        self.button.connect("clicked", self.dataanalysis, None)
    
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
    
        self.window.add(self.button)
    
        self.button.show()
    
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    da = DataAnalysis()
    da.main()

