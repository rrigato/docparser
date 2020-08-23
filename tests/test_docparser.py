from datetime import datetime
from unittest.mock import MagicMock
from unittest.mock import mock_open
from unittest.mock import patch

import json
import os
import unittest


class UnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.markdown_files_list = ["cloudformation-execute-changeset.md", "welcome.md", "task-reference.md", "ecr-pushimage.md", "security.md", "setting-up.md", "disaster-recovery-resiliency.md", "index.md", "send-message.md", "security-iam.md", "getting-started.md", "elastic-beanstalk-createversion.md", "awspowershell-module-script.md", "cloudformation-create-update.md", "secretsmanager-create-update.md", "tutorial-s3.md", "lambda-netcore-deploy.md", "systemsmanager-setparameter.md", "document-history.md", "codedeploy-deployment.md", "data-protection.md", "secretsmanager-getsecret.md", "compliance-validation.md", "elastic-beanstalk-deploy.md", "awsshell.md", "systemsmanager-runcommand.md", "lambda-deploy.md", "tutorial-eb.md", "s3-download.md", "s3-upload.md", "aws-cli.md", "lambda-invoke.md", "cloudformation-delete-stack.md", "systemsmanager-getparameter.md", "tutorials.md", "infrastructure-security.md"]
        cls.devops_task_list = ["Common", "CloudFormationExecuteChangeSet", "SystemsManagerRunCommand", "AWSCLI", "BeanstalkCreateApplicationVersion", "AWSPowerShellModuleScript", "SecretsManagerGetSecret", "ECRPushImage", "S3Download", "SystemsManagerSetParameter", "S3Upload", "CodeDeployDeployApplication", "CloudFormationCreateOrUpdateStack", "ECRPullImage", "BeanstalkDeployApplication", "SystemsManagerGetParameter", "AWSShellScript", "CloudFormationDeleteStack", "LambdaDeployFunction", "LambdaInvokeFunction", "SecretsManagerCreateOrUpdateSecret", "SendMessage", "LambdaNETCoreDeploy"]

        with open("tests/tasks/s3upload.json") as s3_upload_task:
            cls.mock_s3_task_definition = json.load(s3_upload_task)

    @patch("builtins.open")
    @patch("os.listdir")
    def test_get_matching_doc(self, listdir_mock, open_mock):
        """Validates matching logic between task folder and documentation
            markdown name

            Parameters
            ----------
            listdir_mock : unittest.mock.MagicMock
                Mock object to get list of markdown name

            open_mock : unittest.mock.MagicMock
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
        listdir_mock.return_value = self.markdown_files_list
        
        mock_path = "fakepath"
        markdown_file_name, markdown_body = get_matching_doc(
            aws_toolkit_docs=mock_path, 
            task_folder_name="LambdaInvokeFunction"
        )
        listdir_mock.assert_called_once_with(
            mock_path
        )

        self.assertEqual(markdown_file_name, "lambda-invoke.md")

        open_mock.assert_called_once_with(
            os.path.join(mock_path, "lambda-invoke.md"), "r"
        )


    @patch("docparser.docparser.get_matching_doc")
    @patch("builtins.open")
    @patch("os.listdir")
    @patch("docparser.docparser.get_logger")
    def test_main(self, get_logger_mock, listdir_mock, open_mock,
        get_matching_doc_mock):
        """Test for main function

            Parameters
            ----------
            get_logger_mock : unittest.mock.MagicMock
                Mock object used to patch get_logger for lambda handler

            listdir_mock : unittest.mock.MagicMock
                Mock object to get list of markdown name

            open_mock : unittest.mock.MagicMock
                Mock object for open reading of markdown file

            get_matching_dock_mock : unittest.mock.MagicMock
                Mock object for open reading of markdown file

            Returns
            -------

            Raises
            ------
        """
        from docparser.docparser import main
        mock_source_code_location = "../mock_source"
        mock_docs_location = "../mock_docs"


        listdir_mock.return_value = self.devops_task_list

        open_mock.return_value = self.mock_s3_task_definition

        main(aws_toolkit_source=mock_source_code_location, aws_toolkit_docs=mock_docs_location)
        get_logger_mock.assert_called_once_with()

        self.assertEqual(open_mock.call_count, len(self.devops_task_list))