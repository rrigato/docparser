from datetime import datetime
from unittest.mock import MagicMock
from unittest.mock import patch

import json
import logging
import os

import unittest


def get_logger():
    """Returns a logger
        Parameters
        ----------


        Returns
        -------

        Raises
        ------
    """
    '''
        Adds the file name to the logs/ directory without
        the extension
    '''
    logging.basicConfig(
        filename=os.path.join("logs/",
        os.path.basename(__file__).split(".")[0] + ".log"),
        format="%(asctime)s %(message)s",
         datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG
         )
    logging.info("\n")

def main(aws_toolkit_source="../awstoolkitsource", aws_toolkit_docs="../awstoolkitdocs"):
    """Main entry point into script

        Parameters
        ----------
        aws_toolkit_source : str
            path to aws toolkit source code. Defaults ../awstoolkitsource
            https://github.com/aws/aws-toolkit-azure-devops

        aws_toolkit_docs : str
            path to aws toolkit docs code. Defaults ../awstoolkitdocs
            https://github.com/awsdocs/aws-tools-ado-vsts-user-guide

        Returns
        -------

        Raises
        ------
    """
    get_logger()
    for devops_task in os.listdir(os.path.join(aws_toolkit_source, "Tasks")):
        logging.info(devops_task)

        try:
            with open(os.path.join(aws_toolkit_source,"Tasks", devops_task, 
                "task.json"), "r") as devops_task:            
                devops_task_definition = json.load(devops_task)
                print(devops_task_definition["name"]) 

        except FileNotFoundError:
            logging.exception("main - task.json not found")
            
    

if __name__ == "__main__":
    main()