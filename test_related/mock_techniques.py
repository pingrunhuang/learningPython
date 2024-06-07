from unittest.mock import patch, Mock
from unittest import TestCase
import pandas as pd
from io import BytesIO
from requests.exceptions import Timeout
from functions import http_get_data, get_df1, get_df2
import os

'''
Mock testing dataframe value 
'''

class TestDFUtils(TestCase):
    @patch('pandas.read_sql')
    def test_one(self, mock: Mock):
        mock.return_value = pd.DataFrame({'foo_id':[1,2,3]}) # make the return result predictable by setting the component inside the object you want to test as the value you expect
        results = get_df1(None)
        mock.assert_called_once()

        pd.testing.assert_frame_equal(results, pd.DataFrame({'bar_id':[1,2,3]}))

    
    def test_two(self):
        """
        test open file using patch context manager
        """
        df = pd.DataFrame({'foo_id': [1,2,3]})
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='sheet1', index=False)
        writer.close()
        output.seek(0)

        with patch('builtins.open', autospec=True) as mock:  # autosepc to make sure mispell error
            mock.return_value = output
            df = get_df2('')
            mock.assert_called_once_with('')
        pd.testing.assert_frame_equal(df, pd.DataFrame({'bar_id':[1,2,3]}))


'''
mocking datetime library: freezegun
'''



'''
set Mock().side_effect to mock the cases that only happen under some unpredictable situation like exception raising

we can also specify the mock here explicitly, but this require the mocked object is within the same file with the to test function
'''
# mock_request = Mock()
class TestRequest(TestCase):
    @patch('functions.requests')
    def test_get_data(self, mock_request):
        mock_request.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            http_get_data()

'''
Mocking instance method: 
In the sense of mocking multiple methods within an instance, stacked decorated patch is applied  
'''

class RemovalService:
    # in this case, path.isfile and remove should be mocked
    def rm(self, path):
        res = os.path.isfile(path)
        if res:
            os.remove(path)

class RemovalServiceTestCase(TestCase):
    def setUp(self):
        self.service = RemovalService() # must separate target object from the test cases

    @patch('functions.os.path')
    @patch('functions.os')
    def test_rm(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        self.service.rm("test")
        self.assertFalse(mock_os.remove.called, "remove not called since file does not exists")

    # note here how we patch the object that reside in the same module of the testing method
    @patch('__main__.os.path')
    @patch('__main__.os')
    def test_local_rm(self, mock_os, mock_path):
        mock_path.isfile.return_value = True
        self.service.rm('.')
        mock_os.remove.assert_called_with('.')

'''
How to avoid mispelling in mock object
'''
import functions
funcs = Mock(spec=functions)
class RemovalServiceTestCase2(TestCase):
    @patch('functions.os.path')
    @patch('functions.os')
    def test_local_rm(self, mock_os, mock_path):
        service = functions.RemovalService()
        mock_path.isfile.return_value = True
        service.rm('.')  # if we provide other method that does not belong to RemovalService, an AttributeError will arise where the previous mock object will treat it as a newly create method
        mock_os.remove.assert_called_with('.')


if __name__ == "__main__":
    import unittest
    unittest.main()

