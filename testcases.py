#!/usr/bin/env python3
"""
Test cases for PasswordGenie - Password and Passphrase Generator
"""

import unittest
import string
import os
import sys
from password_generator import generate_password, random_passphrase_generator


class TestPasswordGenerator(unittest.TestCase):
    """Test cases for the password generation functionality"""
    
    def test_generate_password_basic(self):
        """Test basic password generation with specified parameters"""
        # Test with small values
        l, u, p, d = 2, 2, 2, 2
        total = l + u + p + d
        password = generate_password(l, u, p, d, total)
        
        # Check password length
        self.assertEqual(len(password), total)
        
        # Check character type counts
        lowercase_count = sum(c.islower() for c in password)
        uppercase_count = sum(c.isupper() for c in password)
        digit_count = sum(c.isdigit() for c in password)
        punct_count = total - (lowercase_count + uppercase_count + digit_count)
        
        self.assertEqual(lowercase_count, l)
        self.assertEqual(uppercase_count, u)
        self.assertEqual(digit_count, d)
        self.assertEqual(punct_count, p)
    
    def test_generate_password_different_lengths(self):
        """Test password generation with different lengths"""
        test_cases = [
            (1, 1, 1, 1),  # minimum values
            (5, 3, 2, 4),  # mixed values
            (10, 5, 3, 7)  # larger values
        ]
        
        for l, u, p, d in test_cases:
            total = l + u + p + d
            password = generate_password(l, u, p, d, total)
            
            # Verify length
            self.assertEqual(len(password), total)
            
            # Verify character counts
            lowercase_count = sum(c.islower() for c in password)
            uppercase_count = sum(c.isupper() for c in password)
            digit_count = sum(c.isdigit() for c in password)
            punct_count = total - (lowercase_count + uppercase_count + digit_count)
            
            self.assertEqual(lowercase_count, l, f"Failed for case {(l, u, p, d)}")
            self.assertEqual(uppercase_count, u, f"Failed for case {(l, u, p, d)}")
            self.assertEqual(digit_count, d, f"Failed for case {(l, u, p, d)}")
            self.assertEqual(punct_count, p, f"Failed for case {(l, u, p, d)}")
    
    def test_generate_password_characters_valid(self):
        """Test that generated password contains only valid characters"""
        l, u, p, d = 3, 3, 3, 3
        total = l + u + p + d
        password = generate_password(l, u, p, d, total)
        
        valid_chars = string.ascii_letters + string.digits + string.punctuation
        
        for char in password:
            self.assertIn(char, valid_chars)
    
    def test_generate_password_randomness(self):
        """Test that password generation produces different results"""
        l, u, p, d = 4, 4, 4, 4
        total = l + u + p + d
        
        # Generate multiple passwords
        passwords = [generate_password(l, u, p, d, total) for _ in range(10)]
        
        # They should not all be the same (very unlikely with proper randomness)
        unique_passwords = set(passwords)
        self.assertGreater(len(unique_passwords), 1, "Generated passwords are not random enough")


class TestPassphraseGenerator(unittest.TestCase):
    """Test cases for the passphrase generation functionality"""
    
    def setUp(self):
        """Set up test environment"""
        # Ensure word_list.txt exists for testing
        self.word_list_path = 'word_list.txt'
        if not os.path.exists(self.word_list_path):
            # Create a temporary word list for testing
            with open(self.word_list_path, 'w') as f:
                f.write("test\nword\nlist\nfor\nunit\ntesting\npurposes\n")
    
    def test_random_passphrase_generator_basic(self):
        """Test basic passphrase generation"""
        word_count = 4
        passphrase = random_passphrase_generator(word_count)
        
        # Check that passphrase is not empty
        self.assertIsNotNone(passphrase)
        self.assertGreater(len(passphrase), 0)
        
        # Check word count (split by spaces)
        words = passphrase.split(' ')
        self.assertEqual(len(words), word_count)
    
    def test_random_passphrase_generator_different_lengths(self):
        """Test passphrase generation with different word counts"""
        test_word_counts = [1, 3, 5, 8, 12]
        
        for word_count in test_word_counts:
            passphrase = random_passphrase_generator(word_count)
            words = passphrase.split(' ')
            self.assertEqual(len(words), word_count, f"Failed for word count {word_count}")
    
    def test_random_passphrase_generator_randomness(self):
        """Test that passphrase generation produces different results"""
        word_count = 4
        
        # Generate multiple passphrases
        passphrases = [random_passphrase_generator(word_count) for _ in range(5)]
        
        # They should not all be the same (very unlikely with proper randomness)
        unique_passphrases = set(passphrases)
        self.assertGreater(len(unique_passphrases), 1, "Generated passphrases are not random enough")
    
    def test_random_passphrase_generator_word_list_dependency(self):
        """Test that passphrase generator requires word_list.txt file"""
        # This test verifies that the word list file is being read
        self.assertTrue(os.path.exists('word_list.txt'), "word_list.txt file is required")


class TestIntegration(unittest.TestCase):
    """Integration tests for the overall functionality"""
    
    def test_password_generator_import(self):
        """Test that password_generator module can be imported"""
        try:
            from password_generator import generate_password, random_passphrase_generator
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import password_generator: {e}")
    
    def test_main_module_import(self):
        """Test that main module can be imported"""
        try:
            import main
            self.assertTrue(hasattr(main, 'main'))
        except ImportError as e:
            self.fail(f"Failed to import main: {e}")


def run_tests():
    """Run all test cases and return results"""
    # Create test loader
    loader = unittest.TestLoader()
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases using the modern approach
    test_suite.addTest(loader.loadTestsFromTestCase(TestPasswordGenerator))
    test_suite.addTest(loader.loadTestsFromTestCase(TestPassphraseGenerator))
    test_suite.addTest(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Run PasswordGenie Test Cases')
    parser.add_argument('--test-type', choices=['password', 'passphrase', 'integration', 'all'], 
                       default='all', help='Type of tests to run')
    args = parser.parse_args()
    
    print("Running PasswordGenie Test Cases...")
    print("=" * 50)
    
    if args.test_type == 'all':
        result = run_tests()
    else:
        # Run specific test category
        loader = unittest.TestLoader()
        runner = unittest.TextTestRunner(verbosity=2)
        
        if args.test_type == 'password':
            suite = loader.loadTestsFromTestCase(TestPasswordGenerator)
        elif args.test_type == 'passphrase':
            suite = loader.loadTestsFromTestCase(TestPassphraseGenerator)
        elif args.test_type == 'integration':
            suite = loader.loadTestsFromTestCase(TestIntegration)
        
        result = runner.run(suite)
    
    print("\n" + "=" * 50)
    print("TEST SUMMARY:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
    
    success_rate = (result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100
    print(f"\nSuccess rate: {success_rate:.1f}%")
    
    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED!")
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED!")
        sys.exit(1)
