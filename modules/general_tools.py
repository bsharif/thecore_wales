#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
from gluon import current
from gluon.dal import DAL, Field
from gluon.sqlhtml import SQLFORM
from gluon.validators import IS_NOT_EMPTY, IS_EMAIL, IS_LENGTH
db = DAL('sqlite://storage.sqlite')
current.db = db

def get_user_name(user_id):
    user_record = db(db.auth_user.id==user_id).select().first()
    first_name = user_record.first_name
    last_name = user_record.last_name
    full_name = str(first_name +" " + last_name)
    return full_name
