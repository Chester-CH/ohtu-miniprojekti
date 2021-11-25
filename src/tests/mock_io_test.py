import unittest
from mock_io import MockIO


class TestMockIO(unittest.TestCase):
    def setUp(self):
        self.io = MockIO()

    def test_writing_to_empty_mock_io_adds_to_output(self):
        self.io.write("test")
        self.assertEqual(self.io.output_list, ["test"])

    def test_writing_to_mock_io_adds_to_end_of_output(self):
        self.io.write("test1")
        self.io.write("test2")
        self.assertEqual(self.io.output_list, ["test1", "test2"])

    def test_read_returns_messages_from_input_list(self):
        new_io = MockIO(["hello", "world"])
        self.assertEqual(new_io.read(), "hello")
        self.assertEqual(new_io.read(), "world")

    def test_read_returns_empty_string_when_input_list_is_empty(self):
        self.assertEqual(self.io.read(), "")

    def test_read_empties_input_list(self):
        new_io = MockIO(["hello"])
        new_io.read()
        self.assertEqual(new_io.read(), "")
