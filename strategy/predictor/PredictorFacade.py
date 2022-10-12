#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Predictor Facade

Acts as a facade for strategy scores predictor.

@Author: nagyl
@Date:   2022.10.07.

"""

import datetime
from pprint import pprint

from strategy.IStrategy import IStrategy
from strategy.predictor.PredictorLeague import PredictorLeague


class PredictorFacade(IStrategy):
    """ Facade for scores predictor """
    name = 'scores-predictor'
    settings: dict = {
        'date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'sports': ['NCAAF']
    }

    def __init__(self):
        """ Inicializing strategies """
        self.league = PredictorLeague()

    def get_settings(self) -> dict:
        """ Returns settings """
        return PredictorLeague.settings

    def get_sports(self) -> list[str]:
        """ Returns available sports """
        return PredictorLeague.available_sports

    def get_name(self) -> str:
        """ Returns the name of the strategy """
        return PredictorFacade.name

    def add_sport(self, sport: str) -> None:
        """ Sport > Settings """
        PredictorFacade.settings.get('sports').append(sport)

    def remove_sport(self, sport: str) -> None:
        """ Removes sport from settings """
        PredictorFacade.settings.get('sport').remove(sport)

    def execute(self) -> None:
        """ Execute strategy """
        events = self.league.execute(PredictorFacade.settings)
