# extensions.py --- 
# 
# Filename: extensions.py
# Author: Louise <louise>
# Created: Sat May  2 06:11:47 2020 (+0200)
# Last-Updated: Fri May 29 14:25:26 2020 (+0200)
#           By: Louise <louise>
# 
"""
Create all extension objects. They are then initialized
with the app in the app factory.
"""
from flask_babel import Babel
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

babel = Babel()
lm = LoginManager()
bcrypt = Bcrypt()
csrf = CSRFProtect()
