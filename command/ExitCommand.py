#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Exit Command

Quits from the application.

@Author: nagyl
@Date:   2022.10.07.

"""

import sys

from command.ICommand import ICommand


class ExitCommand(ICommand):
    """ Exit Command """
    message: str = 'Bye!'
    help_message: str = 'Exits application'

    def execute(self, command: str) -> None:
        """ Closes the application with an exit message """
        print(ExitCommand.message)
        sys.exit(0)

    def unexecute(self) -> None:
        """ There is no unexecution from exiting """
        pass

    def help(self) -> None:
        """ Help message """
        print(ExitCommand.help_message)
