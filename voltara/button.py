"""

.. module:: button
   :synopsis: Handles pressing of the button

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

from gpiozero import Button

# Uses GPIO 23
button = Button(23)

# button.wait_for_press()
# print("button pressed")
