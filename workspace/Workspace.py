#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Workspace Object

This singleton object will contain all
relevant information about our workspace.
E.g.: Selected strategy, its settings, etc.

@Author: nagyl
@Date:   2022.10.07.

"""


class Workspace(object):
    """ Singleton Workspace object """
    instance: 'Workspace' = None

    def __new__(cls) -> 'Workspace':
        """ Singleton pattern """
        if cls.instance is None:
            cls.instance = super(Workspace, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        """ Workspace data """
        self.strategy = None
