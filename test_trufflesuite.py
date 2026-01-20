# test_trufflesuite.py
"""
Tests for TruffleSuite module.
"""

import unittest
from trufflesuite import TruffleSuite

class TestTruffleSuite(unittest.TestCase):
    """Test cases for TruffleSuite class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TruffleSuite()
        self.assertIsInstance(instance, TruffleSuite)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TruffleSuite()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
