#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" ICommand interface

All available commands must be realizing the ICommand
interface. Follows the Command Processor Pattern.

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
