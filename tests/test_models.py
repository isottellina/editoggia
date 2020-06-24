# test_models.py --- 
# 
# Filename: test_models.py
# Author: Louise <louise>
# Created: Mon Jun 22 21:35:44 2020 (+0200)
# Last-Updated: Mon Jun 22 22:05:07 2020 (+0200)
#           By: Louise <louise>
#
from helpers import EditoggiaTestCase

from editoggia.database import db
from editoggia.models import Story, Fandom, Tag

class TestModel(EditoggiaTestCase):
    """
    Tests functions overloaded in models.
    """
    def test_story_setattr(self):
        """
        Test the setattr overloading of the Story
        model. We're supposed to be able to set
        fandoms and tags that don't exist and have
        them created.
        """
        story = self.create_stories(1)[0]

        story.fandom = ["Original Work", "Fandom2"]
        story.tags = ["Tag1", "Tag2"]

        fandoms = db.session.query(Fandom).all()
        tags = db.session.query(Tag).all()

        self.assertEqual(story.fandom, fandoms)
        self.assertEqual(story.tags, tags)

    def test_crudmixin_get_by_id(self):
        """
        Tries to get an object by its ID.
        """
        fandom = Fandom.get_by_id(1)

        self.assertNotEqual(fandom, None)

    def test_crudmixin_get_by_id_invalid(self):
        """
        Tries to get an object that doesn't exist.
        """
        fandom = Fandom.get_by_id("not working")

        self.assertEqual(fandom, None)

    def test_crudmixin_create(self):
        """
        Tries to create a Fandom.
        """
        fandom = Fandom.create(name = "Fandom1")

        db.session.query(Fandom).filter(Fandom.name == "Fandom1").first()

        self.assertNotEqual(fandom, None)

    def test_crudmixin_delete(self):
        """
        Tries to delete a fandom.
        """
        self.assertNotEqual(Fandom.get_by_id(1), None)
        
        fandom = Fandom.get_by_id(1)
        fandom.delete()

        self.assertEqual(Fandom.get_by_id(1), None)