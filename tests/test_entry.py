"""Tests for the One-Liner Marathon entry.

Run:  python3 -m pytest tests/ -q     (or python3 -m unittest discover -s tests)
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main


class TestEntry(unittest.TestCase):
    def test_joke_is_one_line_within_gate(self):
        self.assertTrue(main.JOKE.strip())
        self.assertNotIn("\n", main.JOKE)
        self.assertGreaterEqual(len(main.JOKE), main.MIN_CHARS)
        self.assertLessEqual(len(main.JOKE), main.MAX_CHARS)
        main.JOKE.encode("utf-8")

    def test_validate_rejects_bad_inputs(self):
        for bad in ("", "   ", "a" * 281, "two\nlines"):
            with self.assertRaises(ValueError, msg=repr(bad)):
                main.validate_joke(bad)

    def test_write_entry_round_trip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "entry.txt")
            main.write_entry(main.JOKE, path)
            with open(path, "rb") as handle:
                raw = handle.read()
            self.assertEqual(raw, main.JOKE.encode("utf-8"))
            self.assertEqual(len(raw.decode("utf-8")), len(main.JOKE))

    def test_two_runs_are_byte_identical(self):
        """The grader runs the program twice; both runs must match."""
        with tempfile.TemporaryDirectory() as tmp:
            first = os.path.join(tmp, "first.txt")
            second = os.path.join(tmp, "second.txt")
            main.write_entry(main.JOKE, first)
            main.write_entry(main.JOKE, second)
            with open(first, "rb") as a, open(second, "rb") as b:
                self.assertEqual(a.read(), b.read())

    def test_main_py_runs_as_script(self):
        env = dict(os.environ)
        result = subprocess.run(
            [sys.executable, "main.py"],
            cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            capture_output=True,
            text=True,
            env=env,
            timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(main.JOKE, result.stdout)


if __name__ == "__main__":
    unittest.main()
