from datetime import datetime
from unittest.mock import MagicMock
from unittest.mock import patch

import json
import os
import unittest


def main(aws_toolkit_source="../awstoolkitsource", aws_toolkit_source="../awstoolkitdocs"):
    """Main entry point into script

        Parameters
        ----------
        aws_toolkit_source : str
            path to aws toolkit source code. Defaults ../awstoolkitsource
            https://github.com/aws/aws-toolkit-azure-devops

        aws_toolkit_source : str
            path to aws toolkit source code. Defaults ../awstoolkitdocs
            https://github.com/awsdocs/aws-tools-ado-vsts-user-guide

        Returns
        -------

        Raises
        ------
    """
    logging.getLogger("logs/docparser.logs")
    for devops_task in os.listdir(aws_toolkit_source + "/Tasks"):
        print(devops_task)
        # with open 
    

if __name__ == "__main__":
    main()