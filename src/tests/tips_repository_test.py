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
