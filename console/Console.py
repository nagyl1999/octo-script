#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Command Line UI

Provides a User Interface through the command line.

@Author: nagyl
@Date:   2022.10.07.

"""

from command import HelpCommand
from command import ExitCommand
from command import CommandProcessor


class Console:
    """ Command Line UI """
    welcome = 'Welcome to OctoScript!'
    message = 'Command: '
    commands = {
        'exit': ExitCommand.ExitCommand(),
        'help': HelpCommand.HelpCommand()
    }

    def __init__(self):
        """ Initiating Command Processor """
        self.command_processor = CommandProcessor.CommandProcessor()

    def serve(self):
        """ Serving as Front-End """
        print(Console.welcome, end='\n\n')
        while True:
            full_command = input(Console.message).strip()
            command = full_command.lower().split(' ')[0]
            if command not in Console.commands:
                continue  # TODO error handling
            self.command_processor.execute(Console.commands.get(command), full_command)
