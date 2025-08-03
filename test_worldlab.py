# test_worldlab.py
"""
Tests for WorldLab module.
"""

import unittest
from worldlab import WorldLab

class TestWorldLab(unittest.TestCase):
    """Test cases for WorldLab class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WorldLab()
        self.assertIsInstance(instance, WorldLab)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WorldLab()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
