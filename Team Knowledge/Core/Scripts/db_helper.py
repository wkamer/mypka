"""
Database paden voor alle SQLite databases in myPKA.
Gebruik: from db_helper import personal_db, team_db, ke_db, gr_db
"""

import os

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

personal_db    = os.path.join(BASE, 'PKM', 'personal.db')
team_db        = os.path.join(BASE, 'Team Knowledge', 'team-knowledge.db')
ke_db          = os.path.join(BASE, 'Team Knowledge', 'Kamer E-commerce', 'kamer e-commerce.db')
gr_db          = os.path.join(BASE, 'Team Knowledge', 'Geldstroom Regie', 'geldstroom-regie.db')
