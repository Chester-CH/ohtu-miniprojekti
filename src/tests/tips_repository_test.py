from database_connection import create_database_connection, TEST_DATABASE_NAME
from initialize_database import initialize_database
from repositories.tips_repository import TipsRepository
import unittest

class TestTipsRepository(unittest.TestCase):
    def setUp(self):
        self.connection = create_database_connection(TEST_DATABASE_NAME)
        initialize_database(self.connection)
        self.tips_repository = TipsRepository(self.connection)

    def test_create_tip_gives_boolean_true(self):
        boolean = self.tips_repository.create_tip("Some_Title")
        self.assertEqual(boolean, True)
    
    def test_create_tip_makes_the_right_title(self):
        title = "Some_Title"
        self.tips_repository.create_tip(title)

        sql = "SELECT title FROM Tips;"
        cursor = self.connection.cursor()
        answer = cursor.execute(sql).fetchone()
        self.assertEqual(answer[0], title)

    def test_get_tips_gives_an_object_with_the_right_title(self):
        input_title = "Crash"
        self.tips_repository.create_tip(input_title)
        tip_list = self.tips_repository.get_tips()
        self.assertEqual(tip_list[0].title, input_title)

    def test_remove_tip_changes_tips_visible_value_from_true_to_false(self):
        input_title = "Pipsa Possu ja yksisarvinen"
        self.tips_repository.create_tip(input_title)

        sql = "SELECT id, visible FROM Tips WHERE title=?;"
        cursor = self.connection.cursor()
        answer = cursor.execute(sql, [input_title]).fetchone()
        self.assertEqual(answer[1], True)

        self.tips_repository.remove_tip(answer[0])
        cursor = self.connection.cursor()
        answer2 = cursor.execute(sql, [input_title]).fetchone()
        self.assertEqual(answer2[1], False)

    def test_get_tips_doesnt_give_removed_tip(self):
        input_title = "Bret Easton Ellis: Glamorama"
        self.tips_repository.create_tip(input_title)

        sql = "SELECT id FROM Tips WHERE title=?;"
        cursor = self.connection.cursor()
        tip_id = cursor.execute(sql, [input_title]).fetchone()

        self.tips_repository.remove_tip(tip_id[0])
        tips = self.tips_repository.get_tips()
        self.assertEqual(len(tips), 0)
