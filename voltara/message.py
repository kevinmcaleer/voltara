"""

.. module:: message
   :synopsis: Handles all the messages

======================================
module_name - Brief Module Description
======================================

.. moduleauthor:: Kevin McAleer <kevinmcaleer@email.com>

Introduction
------------

A brief introduction to the module and its purpose. Describe what the module does and why it's useful.

Usage
-----

Provide examples of how to import and use the module. Include simple code snippets if possible.

Contents
--------

List the main contents or functionalities of the module, including classes, functions, and any other important components.

References
----------

List any external references or resources related to the module, such as documentation, tutorials, or related projects.

Notes
-----

Include any additional notes or remarks about the module, such as known issues, future development plans, or important considerations for users.
"""

from Adafruit_Thermal import *

HEADER = "--= Voltara Speakers =--"
FOOTER = "https://www.kevsrobots.com/voltara"


class Message:

    def __init__(self):

        self.message = "Your wish is granted"

        # Setup the Printer
        self.printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
        
        # Set the printing speed
        self.printer.setTimes(35000, 2100)

    
    def print_header(self):
        """ Prints the header message """
        self.printer.feed(2)

        self.printer.underlineOn()
        self.printer.setSize("M")
        self.printer.justify('C')
        self.printer.print(HEADER)

    def print_footer(self):
        """ Prints the footer message """

        self.printer.underlineOff()
        self.printer.setSize("S")
        self.printer.justify("L")
        self.printer.feed(2)
        self.printer.print(FOOTER)

    def print_fortune(self):
        """ Prints the fortune """

        # TODO: Insert code here for fortune
        self.printer.underlineOff()
        self.printer.setSize("S")
        self.printer.justify("L")
        self.printer.feed(2)
        
        print(self.message)
        # self.printer.print(self.message)

        self.printer.feed(2)