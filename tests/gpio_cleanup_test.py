"""
Test de l'import du module exit_handler (l'import au milieu du code est donc normal!)
"""
import unittest

class CleanupTest(unittest.TestCase):
    def test_atexit_register(self):
        import atexit

        before_import_count = atexit._ncallbacks()

        from src.lib import exit_handler

        after_import_count = atexit._ncallbacks()

        self.assertEqual(before_import_count + 1, after_import_count)

        exit_handler()

        self.assertEqual(before_import_count + 1, after_import_count)


if __name__ == "__main__":
    unittest.main()
