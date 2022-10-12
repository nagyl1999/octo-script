#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Show Strategy Command

Prints the selected strategy. Gives another
input in case there is none.

@Author: nagyl
@Date:   2022.10.12.

"""

from command.ICommand import ICommand
from workspace.Workspace import Workspace


class ShowStrategyCommand(ICommand):
    """ Show Selected Strategy """
    help_message = 'Displays currently selected strategy'
    error_message = 'There is no selected strategy!'

    def __init__(self):
        """ Inicializing workspace """
        self.workspace = Workspace()

    def execute(self, command: str) -> None:
        """ Output selected strategy """
        if self.workspace.strategy is None:
            print(ShowStrategyCommand.error_message)
            return None
        print(f'Selected strategy: {self.workspace.strategy.get_name()}')
        self.workspace.strategy.execute()

    def unexecute(self) -> None:
        """ There is no unexecution from printing """
        pass

    def help(self) -> None:
        """ Display help message """
        print(ShowStrategyCommand.help_message)
