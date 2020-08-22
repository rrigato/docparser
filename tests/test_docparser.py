from datetime import datetime
from unittest.mock import MagicMock
from unittest.mock import patch

import json
import os
import unittest


class UnitTests(unittest.TestCase):

    
    @patch("logging.getLogger")
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
