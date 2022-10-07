#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Help Command

Displays help message.

@Author: nagyl
@Date:   2022.10.07.

"""

from command.ICommand import ICommand


class HelpCommand(ICommand):
    """ Help Command """
    commands = ['exit', 'help']

    def execute(self, command: str) -> None:
        """ Closes the application with an exit message """
        print('Available Commands:')
        print('\n'.join([f"\t - {cmd}" for cmd in sorted(HelpCommand.commands)]))

    def unexecute(self) -> None:
        """ There is no unexecution from displaying help message """
        pass
