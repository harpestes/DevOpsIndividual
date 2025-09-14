import unittest
import io
from contextlib import redirect_stdout
from ..string_operations import print_string, analyze_string, to_uppercase

class StringOperationsTests(unittest.TestCase):
    def test_print_string_valid_input(self):
        with io.StringIO() as buffer, redirect_stdout(buffer):
            print_string("hello")
            output = buffer.getvalue()
            self.assertEqual(output, "hello\n")

    def test_print_string_invalid_input(self):
        with self.assertRaises(TypeError):
            print_string(123)
        with self.assertRaises(TypeError):
            print_string(None)

    def test_analyze_string_uppercase(self):
        with io.StringIO() as buffer, redirect_stdout(buffer):
            analyze_string("HELLO")
            output = buffer.getvalue()
            self.assertIn("String HELLO in uppercase", output)

    def test_analyze_string_lowercase(self):
        with io.StringIO() as buffer, redirect_stdout(buffer):
            analyze_string("hello")
            output = buffer.getvalue()
            self.assertIn("String hello in lowercase", output)

    def test_analyze_string_mixedcase(self):
        with io.StringIO() as buffer, redirect_stdout(buffer):
            analyze_string("Hello World")
            output = buffer.getvalue()
            self.assertIn("String Hello World is mixed", output)

    def test_analyze_string_invalid_input(self):
        with self.assertRaises(TypeError):
            analyze_string(123)

    def test_to_uppercase_valid_input(self):
        self.assertEqual(to_uppercase("hello world"), "HELLO WORLD")
        self.assertEqual(to_uppercase("smogtether"), "SMOGTETHER")

    def test_to_uppercase_invalid_input(self):
        with self.assertRaises(TypeError):
            to_uppercase(123)
        with self.assertRaises(TypeError):
            to_uppercase(None)