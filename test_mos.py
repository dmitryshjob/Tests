import unittest

from mos import citis, dictionaries, list_requests

class TestCitis (unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_citis_01(self):
        res = citis()
        self.assertIsInstance(res, list)
      

class TestDictionaries(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_dictionaries01(self):
        res = dictionaries()
        self.assertIsInstance(res, list)

class TestList_requests(unittest.TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_list_requests01(self):
        res = list_requests()    
        self.assertIsInstance(res, float)      




if __name__ == '__main__':
    unittest.main()