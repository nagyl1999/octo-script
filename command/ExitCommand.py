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
    message = 'Bye!'

    def execute(self, command: str) -> None:
        """ Closes the application with an exit message """
        print(ExitCommand.message)
        sys.exit(0)

    def unexecute(self) -> None:
        """ There is no unexecution from exiting """
        pass
