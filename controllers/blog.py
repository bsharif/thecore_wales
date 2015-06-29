# -*- coding: utf-8 -*-
# try something like
import datetime
from gluon.tools import prettydate

def get_user_name(user_id):
    user_record = db(db.auth_user.id==user_id).select().first()
    first_name = user_record.first_name
    last_name = user_record.last_name
    full_name = str(first_name +" " + last_name)
    return full_name

def index():
    all_posts = db(db.blog_posts).select(db.blog_posts.ALL,orderby=~db.blog_posts.created_on)
    return locals()

def new_blog_post():
    form = SQLFORM(db.blog_posts)
    if form.process().accepted:
        response.flash = 'Blog Posted'
        redirect(URL('index'))
    return locals()

def get_blog_tags():
    all_posts = db(db.blog_posts).select()
    tags_list = []
    for post in all_posts:
        for tag in post.tags:
            tags_list.append(tag)
    return tags_list

def get_users_list():
    all_posts = db(db.blog_posts).select(db.blog_posts.ALL)
    user_list = []
    for post in all_posts:
        user_list.append(post.created_by)
    user_list = list(set(user_list))
    user_dict = {}
    for user in user_list:
        user_record = db(db.auth_user.id==user).select().first()
        user_name = user_record.first_name + " " + user_record.last_name
        user_dict[user] = user_name
    return user_dict

@auth.requires_membership('administrator')
def edit_blog_post():
    post_id = request.vars.post_id
    form=SQLFORM(db.blog_posts, post_id, showid=False)
    if form.process().accepted:
        response.flash = 'Post Updated'
        redirect(URL('view_blog_post',vars={'post_id':post_id}))
    return locals()


def view_blog_post():
    post_id = request.vars.post_id
    blog_post_record = db(db.blog_posts.id==post_id).select().first()
    user_name = get_user_name(blog_post_record.created_by)
    advanced_options=False
    if auth:
        user_id = auth.user_id
        if auth.has_membership('administrator'):
            advanced_options=True

    return locals()
    

def user_posts():
    user_id = request.vars.user_id
    user_record = db(db.auth_user.id==user_id).select().first()
    user_posts = db(db.blog_posts.created_by==user_id).select(db.blog_posts.ALL,orderby=~db.blog_posts.created_on)
    return locals()

def view_tag():
    tag_name = request.args(0)
#     user_record = db(db.auth_user.id==user_id).select().first()
    blog_posts = db(db.blog_posts.tags.contains(tag_name)).select(db.blog_posts.ALL,orderby=~db.blog_posts.created_on)
    return locals()

session.blog_tags = get_blog_tags()
session.user_dict = get_users_list()
