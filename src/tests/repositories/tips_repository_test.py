import unittest
from database_connection import create_database_connection, TEST_DATABASE_NAME
from initialize_database import initialize_database
from repositories.tips_repository import TipsRepository
from services.reading_tip_factory import ReadingTipFactory
from entities.tip_types import TipTypes


class TestTipsRepository(unittest.TestCase):
    def setUp(self):
        self.connection = create_database_connection(TEST_DATABASE_NAME)
        initialize_database(self.connection)
        self.tips_repository = TipsRepository(self.connection)

    def test_store_reading_tip_gives_boolean_true(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BOOK)
        tip['title'] = "Snowcrash"
        boolean = self.tips_repository.store_reading_tip(tip)
        self.assertTrue(boolean)

    def test_store_reading_tip_stores_the_right_title(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BOOK)
        tip['title'] = "Snowcrash"
        self.tips_repository.store_reading_tip(tip)

        sql = "SELECT title FROM Tips;"
        cursor = self.connection.cursor()
        answer = cursor.execute(sql).fetchone()
        self.assertEqual(answer[0], tip["title"])

    def test_store_reading_tips_stores_the_right_type(self):
        tip_type = TipTypes.BOOK
        tip = ReadingTipFactory.get_new_reading_tip(tip_type)
        tip['title'] = "Snowcrash"
        self.tips_repository.store_reading_tip(tip)

        sql = "SELECT type FROM Tips;"
        cursor = self.connection.cursor()
        answer = cursor.execute(sql).fetchone()
        self.assertEqual(answer[0], tip_type)

    def test_store_reading_tips_stores_new_title_correctly(self):
        new_title = "Story about ham"
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BOOK)
        tip['title'] = "Snowcrash"
        self.tips_repository.store_reading_tip(tip)
        tip['title'] = new_title
        self.assertTrue(self.tips_repository.store_reading_tip(tip))

        cursor = self.connection.cursor()
        sql = "SELECT title FROM Tips;"
        answer = cursor.execute(sql).fetchone()
        self.assertEqual(answer[0], new_title)

    def test_get_tips_gives_an_object_with_the_right_title(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BOOK)
        tip['title'] = "Snowcrash"
        self.tips_repository.store_reading_tip(tip)

        tip_list = self.tips_repository.get_tips()
        self.assertEqual(tip_list[0]["title"], tip["title"])

    def test_remove_tip_changes_tips_visible_value_from_true_to_false(self):
        input_title = "Pipsa Possu ja yksisarvinen"
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BOOK)
        tip['title'] = input_title
        self.tips_repository.store_reading_tip(tip)

        sql = "SELECT id, visible FROM Tips WHERE title=?;"
        cursor = self.connection.cursor()
        answer = cursor.execute(sql, [input_title]).fetchone()
        self.assertEqual(answer[1], True)

        self.tips_repository.remove_tip(answer[0])
        cursor = self.connection.cursor()
        answer2 = cursor.execute(sql, [input_title]).fetchone()
        self.assertEqual(answer2[1], False)

    def test_get_tips_doesnt_give_removed_tip(self):
        input_title = "Glamorama"
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BOOK)
        tip['title'] = input_title
        self.tips_repository.store_reading_tip(tip)

        sql = "SELECT id FROM Tips WHERE title=?;"
        cursor = self.connection.cursor()
        tip_id = cursor.execute(sql, [input_title]).fetchone()

        self.tips_repository.remove_tip(tip_id[0])
        tips = self.tips_repository.get_tips()
        self.assertEqual(len(tips), 0)

    def test_storing_book_type_tip_with_its_parameters(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BOOK)
        tip["title"] = title = "Taivaallinen vastaanotto"
        tip["author"] = author = "Jukka Viikilä"
        tip["isbn"] = isbn = "978-951-1-37793-1"
        tip["description"] = description = "Finlandia 2021"
        self.tips_repository.store_reading_tip(tip)
        tip = self.tips_repository.get_tips()[0]
        self.assertEqual(
            (tip["title"], tip["author"], tip["isbn"], tip["description"]),
            (title, author, isbn, description)
        )

    def test_storing_video_type_tip_with_its_parameters(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.VIDEO)
        tip["title"] = title = "Joulusydän"
        tip["url"] = url = "https://www.youtube.com/watch?v=rf-s3PuSkvs"
        tip["description"] = description = "a cool christmas song"
        self.tips_repository.store_reading_tip(tip)
        tip = self.tips_repository.get_tips()[0]
        self.assertEqual(
            (tip["title"], tip["url"], tip["description"]),
            (title, url, description)
        )

    def test_storing_blogpost_type_tip_with_its_parameters(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BLOGPOST)
        tip["title"] = title = "How Secure Is The Flask User Session?"
        tip["author"] = author = "Miguel Grinberg"
        tip["url"] = url = "https://blog.miguelgrinberg.com/post/\
                            how-secure-is-the-flask-user-session"
        tip["description"] = description = "material for tsoha"
        self.tips_repository.store_reading_tip(tip)
        tip = self.tips_repository.get_tips()[0]
        self.assertEqual(
            (tip["title"], tip["author"], tip["url"], tip["description"]),
            (title, author, url, description)
        )

    def test_storing_podcast_type_tip_with_its_parameters(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.PODCAST)
        tip["title"] = title = "Avaruusteleskooppi Hubblen \
                                seuraaja saattaa nähdä \
                                maailmankaikkeuden alkuun"
        tip["url"] = url = "https://areena.yle.fi/audio/1-50990157"
        tip["name"] = name = "Tiedeykkönen"
        tip["description"] = description = "space nad universe"
        self.tips_repository.store_reading_tip(tip)
        tip = self.tips_repository.get_tips()[0]
        self.assertEqual(
            (tip["title"], tip["url"], tip["name"], tip["description"]),
            (title, url, name, description)
        )
