import unittest
from entities.content import Content


class MockValidator:
    called = False

    def mock_validator(self, value):
        self.called = True
        if value != 10:
            return True
        return False


class TestContent(unittest.TestCase):
    def test_default_validator_works(self):
        content = Content(10)
        content.value = None
        self.assertEqual(content.value, 10)

    def test_injected_validator_is_called(self):
        mock_validator = MockValidator()
        self.assertFalse(mock_validator.called)
        content = Content(0, mock_validator.mock_validator)
        content.value = 10
        self.assertTrue(mock_validator.called)

    def test_injected_validator_works(self):
        mock_validator = MockValidator()
        content = Content(0, mock_validator.mock_validator)
        content.value = 10
        self.assertEqual(content.value, 0)
