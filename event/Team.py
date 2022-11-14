#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Team Model

Models a Team. Name, Odds must be filled.
The attribute other can be used to store non-trivial
data.

@Author: nagyl
@Date:   2022.11.14.

"""


class Team:
    """ Team Model """

    def __init__(self, name: str, odds: float) -> None:
        """ Take over name and odds """
        self.name = name
        self.odds = odds
        self.other = dict()
