import unittest
from yan_api import create_folder, get_folder_info, delete_folder

FOLDER = 'test'


class Test_create_folder(unittest.TestCase):

    def test_createfolder201(self):
        res = create_folder(FOLDER)
        # if res == 201:
        #     res = f'Статус код {res} папка {FOLDER} создана'
        self.assertTrue(res == 201, res)

class Test_get_folder_info(unittest.TestCase):    

    def test_get_folder_info(self):
        res = get_folder_info(FOLDER)
        # if res == 409:
        #     res = f'Статус код {res} папка с именем {FOLDER} уже существует'
        self.assertTrue(res == 200, res) 

    def test_get_folder_info(self):
        res = get_folder_info(FOLDER)
        self.assertTrue(res == 404, res) 

class Test_delete_folder(unittest.TestCase):
    def test_delete_folder(self):
        res = delete_folder(FOLDER)

        self.assertTrue(res == 204, res)


if __name__ == '__main__':
    unittest.main()        