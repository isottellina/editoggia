# models.py --- 
# 
# Filename: models.py
# Author: Louise <louise>
# Created: Thu May 14 18:25:31 2020 (+0200)
# Last-Updated: Thu May 14 19:21:23 2020 (+0200)
#           By: Louise <louise>
#
"""
The models for the story blueprint.
"""
from flask_babel import gettext
from app.database import db

class FandomCategory(db.Model):
    """
    Represent a category of fandom, like “Books” and such.
    """
    __tablename__ = "fandomcategory"
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    fandoms = db.relationship('Fandom', back_populates='category')

class Fandom(db.Model):
    """
    Represent a fandom. 
    """
    __tablename__ = "fandom"
    
    id = db.Column(db.Integer(), primary_key=True)
    category_id = db.Column(db.Integer(), db.ForeignKey('fandomcategory.id'))
    category = db.relationship('FandomCategory', back_populates='fandoms')
    
    name = db.Column(db.String(255), index=True, unique=True, nullable=False)
    fictions = db.relationship('Fiction',
                               secondary='fiction_fandoms',
                               back_populates='fandom')

class FictionFandoms(db.Model):
    """
    An association table, allowing each fiction to have several fandoms.
    """
    __tablename__ = "fiction_fandoms"

    id = db.Column(db.Integer(), primary_key=True)
    fandom_id = db.Column(db.Integer(), db.ForeignKey('fandom.id'))
    fiction_id = db.Column(db.Integer(), db.ForeignKey('fiction.id'))
    
    
class Fiction(db.Model):
    """
    A fiction, written on the site.
    """
    __tablename__ = "fiction"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    hits = db.Column(db.Integer(), nullable=False, default=0, index=True)

    fandom = db.relationship('Fandom',
                             secondary='fiction_fandoms',
                             back_populates='fictions')
    
    author_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='fictions')

    tags = db.relationship('Tag', secondary='fictions_tags',
                           back_populates='fictions')
    
class FictionsTags(db.Model):
    """
    Association table between Fiction and Tags.
    """
    __tablename__ = "fictions_tags"

    id = db.Column(db.Integer(), primary_key=True)
    fiction_id = db.Column(db.Integer(), db.ForeignKey('fiction.id'))
    tag_id = db.Column(db.Integer(), db.ForeignKey('tag.id'))

class Tag(db.Model):
    """
    A tag. I really don't know how else to describe it.
    """
    __tablename__ = "tag"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    fictions = db.relationship('Fiction', secondary='fictions_tags',
                               back_populates='tags')