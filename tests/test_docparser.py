from datetime import datetime
from unittest.mock import MagicMock
from unittest.mock import patch

import json
import os
import unittest


class UnitTests(unittest.TestCase):
    
    @patch("builtins.open")
    @patch("os.listdir")
    def test_get_matching_doc(self, listdir_mock, open_patch):
        """Validates matching logic between task folder and documentation
            markdown name

            Parameters
            ----------
            listdir_mock : unittest.mock.MagicMock
                Mock object to get list of markdown name

            open_patch : unittest.mock.MagicMock
                Mock object for open reading of markdown file

            Returns
            -------

            Raises
            ------
        """
        from docparser.docparser import get_matching_doc
        '''
            Use an example of markdown files to validate the correct file is selected
        '''
        listdir_mock.return_value = ["cloudformation-execute-changeset.md", "welcome.md", "task-reference.md", "ecr-pushimage.md", "security.md", "setting-up.md", "disaster-recovery-resiliency.md", "index.md", "send-message.md", "security-iam.md", "getting-started.md", "elastic-beanstalk-createversion.md", "awspowershell-module-script.md", "cloudformation-create-update.md", "secretsmanager-create-update.md", "tutorial-s3.md", "lambda-netcore-deploy.md", "systemsmanager-setparameter.md", "document-history.md", "codedeploy-deployment.md", "data-protection.md", "secretsmanager-getsecret.md", "compliance-validation.md", "elastic-beanstalk-deploy.md", "awsshell.md", "systemsmanager-runcommand.md", "lambda-deploy.md", "tutorial-eb.md", "s3-download.md", "s3-upload.md", "aws-cli.md", "lambda-invoke.md", "cloudformation-delete-stack.md", "systemsmanager-getparameter.md", "tutorials.md", "infrastructure-security.md"]
        
        mock_path = "fakepath"
        markdown_file_name, markdown_body = get_matching_doc(
            aws_toolkit_docs=mock_path, 
            task_folder_name="LambdaInvokeFunction"
        )
        listdir_mock.assertCalledOnceWith(
            mock_path
        )

        self.assertEqual(markdown_file_name, "lambda-invoke.md")


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