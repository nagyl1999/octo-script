#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Command Line UI

Provides a User Interface through the command line.

@Author: nagyl
@Date:   2022.10.07.

"""

from command import CommandProcessor


class Console:
    """ Command Line UI """
    welcome: str = 'Welcome to OctoScript!'
    message: str = 'Command: '

    def __init__(self) -> None:
        """ Initiating Command Processor """
        self.command_processor = CommandProcessor.CommandProcessor()

    def serve(self) -> None:
        """ Serving as Front-End """
        print(Console.welcome, end='\n\n')
        while True:
            full_command = input(Console.message).strip()
            command = full_command.lower().split(' ')[0]
            if command not in self.command_processor.commands:
                print(f'Error: command {command} not found!')
                continue
            self.command_processor.execute(self.command_processor.commands.get(command), full_command)
