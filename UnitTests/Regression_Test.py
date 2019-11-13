import unittest
from Main import Main
from ObjectClasses.RomanBaseList import RomanBaseList
from SemanticAnalysis.NumberConvert import NumberConvert

TEST_FILE_PATH = "UnitTests/TestInput/"


class UnitTest(unittest.TestCase):
    def test_galaxy_project_positive_result(self):
        main = Main()
        result = main.translate("".join([TEST_FILE_PATH, 'project_positive_test.txt']))
        correct_result = ['pish tegj glob glob is 42',
                          'glob prok Silver is 68 Credits',
                          'glob prok Gold is 57800 Credits',
                          'glob prok Iron is 782 Credits']
        self.assertEqual(result, correct_result)

    def test_galaxy_project_negative_result(self):
        main = Main()
        result = main.translate("".join([TEST_FILE_PATH, 'project_negative_test.txt']))
        negative_result = ['pish tegj glob glob is 42',
                          'glob prok Silver is 68 Credits',
                          'I have no idea what you are talking about']
        self.assertEqual(result, negative_result)


if __name__ == '__main__':
    unittest.main()
