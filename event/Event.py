#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Event Model

Models an Event. ID, Date, Teams, must be present.
The attribute other can be used to store non-trivial
data.

@Author: nagyl
@Date:   2022.11.14.

"""

import datetime

from event.Team import Team


class Event:
    """ Event Model """

    def __init__(self, id: str, date: datetime.datetime, teams: list[Team]):
        """ Take over date and teams """
        self.id = id
        self.date = date
        self.teams = teams
        self.other = dict()
