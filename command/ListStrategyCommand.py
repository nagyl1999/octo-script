#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" List Strategy Command

Lists all available strategies.

@Author: nagyl
@Date:   2022.10.07.

"""

from command.ICommand import ICommand
from workspace.Workspace import Workspace


class ListStrategyCommand(ICommand):
    """ List Strategy Command"""
    message = 'Available strategies:'
    help_message = 'Lists all available strategies'

    def __init__(self):
        """ Initiating workspace """
        self.workspace = Workspace()

    def execute(self, command: str) -> None:
        """ List all available strategies """
        print(ListStrategyCommand.message)
        for name in self.workspace.strategies.keys():
            print(f'\t- {name}')

    def unexecute(self) -> None:
        """ There is no unexecution of listing """
        pass

    def help(self) -> None:
        """ Help message """
        print(ListStrategyCommand.help_message)
