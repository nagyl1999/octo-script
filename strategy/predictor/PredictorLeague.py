#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Predictor League

Collects data from scores predictor in
specific leagues.

@Author: nagyl
@Date:   2022.10.12.

"""

from zcode.ZCode import Session
from bs4 import BeautifulSoup


class PredictorLeague:
    """ Collects League events """
    available_sports = ['NFL', 'NBA', 'NCAAB', 'NCAAF', 'MLB', 'KHL', 'AHL', 'NHL']

    def __init__(self) -> None:
        """ Inicializing ZCode API """
        self.zcode: Session = Session()
        self.events = list()
        self.signals: dict[str, dict] = {}

    def execute(self, settings: dict) -> dict:
        """ Execute strategy """
        self.signals.clear()
        for sport in settings.get('sports'):
            if sport not in PredictorLeague.available_sports:
                continue
            html = self.zcode.get_scores_predictor(sport)['html']
            self.process_html(html)
            self.add_kelly(html)
        return self.signals

    def process_html(self, html: str) -> None:
        """ Process html for signals """
        events = BeautifulSoup(html, 'html.parser').find('table', {'id': 'master'})
        if events is None:
            return
        events = events.find('tbody').find_all('tr', {'class': 'game'})
        for event in events:
            self.signals[event['data-gid']] = {
                'date': event['data-date'],
                'teams': [],
                'confidence': event.find('td', {'class': 'confidence'}).text.strip().replace('%', ''),
                'prediction': event.find('td', {'class': 'pscore'}).text.strip().split(' ')[0].split('(')[0].split(':')
            }
            try:
                for team in event.find_all('td', {'class': 'team_name'}):
                    hot = team.find('span', {'class': 'hot'})
                    odds = team.find('span', {'class': 'odd'}).text
                    name = team.find('div', {'class': 'team'}).text.replace(odds, '')
                    if hot is not None:
                        name = name.replace(hot.text, '')
                    self.signals[event['data-gid']].get('teams').append({
                        'hot': hot,
                        'odds': odds,
                        'name': name
                    })
            except Exception as ignore:
                continue

    def add_kelly(self, html: str) -> None:
        """ Add kelly values for events """
        events = BeautifulSoup(html, 'html.parser').find('table', {'data-pclass': 'p2'})
        if events is None:
            return
        events = events.find('tbody').find_all('tr', {'class': 'game'})
        for event in events:
            self.signals.get(event['data-gid'])['kelly'] = {
                'wage': event.find('td', {'class': 'wagepart'}).text,
                'winner': event.find('td', {'class': 'kellybet'}).text
            }
