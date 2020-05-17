import unittest
import sys
sys.path.insert(0, '..')
from cpu_builds import *

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

def get_default_resource(name="test_resource", manufacturer="test_manfacturer", total=100, allocated=0):
    return Resource(name, manufacturer, total, allocated)


class TestResource(unittest.TestCase):
    """Test the resource class in cpu_builds"""

    def test_create_resource(self):
        """Test creation of resource object"""
        resource = Resource('test name', 'test manufacturer', 100, 1)
        self.assertEqual(resource.name, 'test name')
        self.assertEqual(resource.manufacturer, 'test manufacturer')
        self.assertEqual(resource.total, 100)
        self.assertEqual(resource.allocated, 1)

    def test_create_resource_invalid_args(self):
        """Test creating resource with invalid arguments fails"""
        self.assertRaises(TypeError, Resource, 123, 'test manufacturer', 100, 1)
        self.assertRaises(TypeError, Resource, 'test name', 1234, 100, 1)
        self.assertRaises(TypeError, Resource, 'test name', 'test manufacturer', '100', 1)
        self.assertRaises(TypeError, Resource, 'test name', 'test manufacturer', 100, '1')
        self.assertRaises(ValueError, Resource, 'test name', 'test manufacturer', -1, 1)
        self.assertRaises(ValueError, Resource, 'test name', 'test manufacturer', 100, -1)

    def test_claim_success(self):
        """test claiming a valid number of resources"""
        resource = get_default_resource()
        total = resource.total
        allocated = resource.allocated
        claim_amount = 25
        resource.claim(claim_amount)
        self.assertEqual(resource.total, total - claim_amount)
        self.assertEqual(resource.allocated, allocated + claim_amount)

    def test_claim_fail(self):
        """Test that trying to claim too many of the resource fails"""
        resource = get_default_resource()
        self.assertRaises(TypeError, resource.claim, 'invalid_input')
        #addmore tests

    def test_freeup_success(self):
        pass

    def test_freeup_fail(self):
        pass

    def test_died_success(self):
        pass

    def test_died_success(self):
        pass

    def test_purchased_success(self):
        pass

    def test_purchased_success(self):
        pass

    
if __name__ == "__main__":
    run_tests(TestResource)