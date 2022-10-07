#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Workspace Object

This singleton object will contain all
relevant information about our workspace.
E.g.: Selected strategy, its settings, etc.
Acts as a single source of truth for available
strategies.

@Author: nagyl
@Date:   2022.10.07.

"""

from strategy.predictor import PredictorFacade
from strategy.IStrategy import IStrategy


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
        self.strategy: IStrategy | None = None
        self.strategies: dict[str, IStrategy] = {
            'scores-predictor': PredictorFacade.PredictorFacade()
        }
