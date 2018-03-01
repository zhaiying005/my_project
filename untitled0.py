#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 10:05:33 2018

@author: yingzhai
"""

import pandas as pd
dat = pd.read_csv('data/gapminder_gdp_europe.csv')
dat = pd.read_csv('data/gapminder_gdp_oceania.csv')
<<<<<<< HEAD
oceania = pd.read_csv('data/gapminder_gdp_oceania.csv')
=======
oceania =pd. read_csv('data/gapminder_gdp_oceania.csv'), index_col = 'country')
>>>>>>> c76690dc758fdcf719b590e455397c361a2fa750
