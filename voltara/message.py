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
import subprocess

HEADER = "--= Voltara Speaks =--"
FOOTER = "https://kevsrobots.com/voltara"


class Message:

    def __init__(self):

        self.message = "Your wish is granted"

        # Setup the Printer
        self.printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
        
        # Set the printing speed
        self.printer.setTimes(35000, 2100)

    
    def print_header(self):
        """ Prints the header message """
        print(HEADER)
        self.printer.feed(5)

        self.printer.underlineOn()
        self.printer.setSize("M")
        self.printer.justify('C')
        self.printer.print(HEADER)

    def print_footer(self):
        """ Prints the footer message """

        print(FOOTER)
        self.printer.underlineOff()
        self.printer.setSize("S")
        self.printer.justify("L")
        self.printer.feed(2)
        self.printer.print(FOOTER)
        self.printer.feed(5)

    def format_message(self, message, line_length):
        words = message.split()
        formatted_lines = []
        current_line = ""
        
        for word in words:
            if len(current_line) + len(word) + 1 <= line_length:
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word
            else:
                formatted_lines.append(current_line)
                current_line = word
        
        if current_line:
            formatted_lines.append(current_line)
        
        return '\n'.join(formatted_lines)

    def print_fortune(self):
        """ Prints the fortune """

        result = subprocess.run(['/usr/games/fortune', '-a',  '-s'], capture_output=True, text=True)
        if result.returncode == 0:
            self.message = result.stdout.strip()
            

        else:
            print("failed to generate a fortune")
            self.message = "Your wish is granted"
            return

        self.printer.underlineOff()
        self.printer.setSize("S")
        self.printer.justify("L")
        self.printer.feed(2)
        
        self.message = self.format_message(self.message, 32)

        print(self.message)
        self.printer.print(self.message)

        self.printer.feed(2)