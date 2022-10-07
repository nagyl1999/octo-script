#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Select Strategy Command

Select one strategy from the available list.

@Author: nagyl
@Date:   2022.10.07.

"""

from command.ICommand import ICommand
from workspace.Workspace import Workspace


class SelectStrategyCommand(ICommand):
    """ List Strategy Command"""
    help_message = 'Select a strategy. Example:\nselect-strategy example-strategy'

    def __init__(self):
        """ Initiating workspace """
        self.workspace = Workspace()

    def execute(self, command: str) -> None:
        """ List all available strategies """
        if len(command.split(' ')) <= 1:
            print('Too few arguments!')
            return None
        strategy = command.lower().split(' ')[1]
        if strategy not in self.workspace.strategies:
            print(f'Error: there is no such strategy!')
            return None
        self.workspace.strategy = self.workspace.strategies.get(strategy)
        print(f'{strategy} selected.')

    def unexecute(self) -> None:
        """ There is no unexecution of listing """
        pass

    def help(self) -> None:
        """ Help message """
        print(SelectStrategyCommand.help_message)
