from datetime import datetime
from unittest.mock import MagicMock
from unittest.mock import patch

import json
import os
import unittest


class UnitTests(unittest.TestCase):

    @patch("os.listdir")
    def test_get_matching_doc(self, listdir_mock):
        """Validates matching logic between task folder and documentation
            markdown name

            Parameters
            ----------
            listdir_mock : unittest.mock.MagicMock
                Mock object to get list of markdown name
            Returns
            -------

            Raises
            ------
        """

    @unittest.skip("Skip until patch system io")
    @patch("docparser.docparser.get_logger")
    def test_main(self, getLogger_mock):
        """Test for main function

            Parameters
            ----------
            getLogger_mock : unittest.mock.MagicMock
                Mock object used to patch get_logger for lambda handler

            Returns
            -------

            Raises
            ------
        """
        from docparser.docparser import main
        main()
        get_logger_mock.assertCalledOnceWith()