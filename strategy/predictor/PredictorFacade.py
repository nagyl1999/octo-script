#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Predictor Facade

Acts as a facade for strategy scores predictor.

@Author: nagyl
@Date:   2022.10.07.

"""

from strategy.IStrategy import IStrategy


class PredictorFacade(IStrategy):
    """ Facade for scores predictor """
    name = 'scores-predictor'

    def get_settings(self) -> dict:
        """ Returns settings """
        pass

    def get_sports(self) -> list[str]:
        """ Returns available sports """
        pass

    def get_name(self) -> str:
        """ Returns the name of the strategy """
        return PredictorFacade.name

    def execute(self) -> None:
        """ Execute strategy """
        pass
