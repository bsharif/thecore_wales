# -*- coding: utf-8 -*-
# def index(): 
#     specialty_list = []
#     specialty_records = db(db.reg_questionnaire).select()
#     for specialty in specialty_records:
#         specialty_list.append = specialty.specialty
#     return locals()

def index():
    all_posts = db(db.blog_posts).select(db.blog_posts.ALL,orderby=~db.blog_posts.created_on)
    return locals()

def view():
    specialty = request.args(0)
    specialty_record = db(db.req_questionnaire.specialty==specialty).select().first()
    
    return locals()
    
def add_new():
    form = SQLFORM(db.reg_questionnaire)
    if form.process().accepted:
        response.flash = 'Record Added'
        redirect(URL('index'))
    return locals()
