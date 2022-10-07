#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Help Command

Displays help messages.

@Author: nagyl
@Date:   2022.10.07.

"""

from command.ICommand import ICommand


class HelpCommand(ICommand):
    """ Help Command """
    message: str = 'All available command:'
    help_message: str = 'Displays help informations'

    def __init__(self, processor):
        """ Dependency Injection """
        self.processor = processor

    def execute(self, cmd: str) -> None:
        """ Closes the application with an exit message """
        if len(cmd.split(' ')) > 1:
            self.processor.commands.get(cmd.split(' ')[1]).help()
            return None
        print(HelpCommand.message)
        for cmd in self.processor.commands.keys():
            print(f'\t- {cmd}')

    def unexecute(self) -> None:
        """ There is no unexecution from displaying help message """
        pass

    def help(self) -> None:
        """ Help message """
        print(HelpCommand.help_message)
