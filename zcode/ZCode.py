#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" ZCode API

This object will provide an API to the ZCode System.
Credentials are required within the .env file. Must
be singleton due to restricted number of logins.

@Author: nagyl
@Date:   2022.10.09.

"""

import os
import dotenv
import logging
import requests
import datetime

from requests import Response

dotenv.load_dotenv()


class Session(requests.Session):
    """ Singleton ZCode Session """
    headers: dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
    instance: 'Session' = None
    url_login: str = 'https://zcodesystem.com/vipclub/do_login.php'
    url_logout: str = 'https://zcodesystem.com/vipclub/logout.php'
    url_scorespredictor: str = 'https://zcodesystem.com/scorespredictor/score_games_list_n1.php'

    def __new__(cls) -> 'Session':
        """ Singleton pattern """
        if cls.instance is None:
            cls.instance = super(Session, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        """ Inicializing credentials """
        super().__init__()
        self.credentials = {
            'emailaddress': os.environ.get('ZCODE_USER'),
            'password': os.environ.get('ZCODE_PASS'),
            'json_result': 1
        }
        self.login()

    def load(self, url: str, data: dict = None) -> Response:
        """ Load ZCode API """
        if data is None:
            data = {}
        return self.post(url, data={**data, **self.credentials}, headers=Session.headers)

    def login(self) -> None:
        """ Log into ZCode """
        response = self.post(Session.url_login, data=self.credentials)
        try:
            if 'success' not in response.json():
                logging.critical('Critical error: cannot login!')
        except Exception as e:
            logging.critical(e)

    def logout(self) -> None:
        """ Logout from ZCode """
        self.load(Session.url_logout)

    def get_scores_predictor(self, sport: str, date: str = None) -> dict:
        """ Get data from scores predictor feature """
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        data = {
            'current_sport': sport.upper(),
            'current_sport2': '',
            'current_league': '',
            'current_date': date,
            'force_get_json': 1
        }
        return self.load(Session.url_scorespredictor, data).json()
