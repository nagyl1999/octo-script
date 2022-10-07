#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" ICommand interface

All available commands must be realizing the ICommand
interface. Follows the Command Processor Pattern. Adds
an extra help function that must contain all help info
about the given command.

@Author: nagyl
@Date:   2022.10.06.

"""


class ICommand:
    """ Command interface, follows Command Processor Pattern """

    def execute(self, command: str) -> None:
        """ Execution must be defined in derived objects """
        pass

    def unexecute(self) -> None:
        """ Unexecution must be defined in derived objects """
        pass

    def help(self) -> None:
        """ Displays help message for command """
        pass
