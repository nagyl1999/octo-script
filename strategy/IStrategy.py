#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" IStrategy interface

All available strategies must be realizing the
IStrategy interface. There is a way to get settings,
available sports to personalize execution. All strategies
should save its result into some file.

@Author: nagyl
@Date:   2022.10.07.

"""


class IStrategy:
    """ IStrategy Interface """

    def get_settings(self):
        """ Returns the realizing strategy's settings """
        pass

    def get_sports(self):
        """ Returns the realizing strategy's available sports """
        pass

    def execute(self):
        """ Execute strategy """
        pass
