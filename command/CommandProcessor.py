#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Command Processor

All initiated commands must be run through this
object. Ensures that all commands can be unexecuted.
Single source of truth for available commands.

@Author: nagyl
@Date:   2022.10.07.

"""

from queue import LifoQueue
from command import HelpCommand
from command import ExitCommand
from command.ICommand import ICommand


class CommandProcessor:
    """ Command Processor, executes, unexecutes commands """
    MAX_SIZE = 0  # No limit

    def __init__(self) -> None:
        """ Inicializing stack for commands """
        self.stack = LifoQueue(maxsize=CommandProcessor.MAX_SIZE)
        self.commands: dict[str, ICommand] = {
            'help': HelpCommand.HelpCommand(self),
            'exit': ExitCommand.ExitCommand()
        }

    def execute(self, command: ICommand, cmd: str) -> None:
        """ Executes command through the ICommand interface's execute method """
        command.execute(cmd)
        self.stack.put(command)

    def unexecute(self) -> None:
        """ Unexecutes last command through the ICommand interface's unexecute method """
        command = self.stack.get()
        command.unexecute()
