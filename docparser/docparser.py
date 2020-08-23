from datetime import datetime
from fuzzywuzzy import process

import json
import logging
import os

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



def get_matching_doc(aws_toolkit_docs, task_folder_name):
    """Returns the matching documentation file

        Parameters
        ----------
        aws_toolkit_docs : str
            path to aws toolkit docs code. Defaults ../awstoolkitdocs
            https://github.com/awsdocs/aws-tools-ado-vsts-user-guide
        
        task_folder_name : str
            name of the aws toolkit task folder

        Returns
        -------
        markdown_file_name : str
            name of markdown file selected
        
        markdown_content : str
            content of the markdown file

        Raises
        ------
    """
    all_markdown_files = os.listdir(aws_toolkit_docs)

    '''
        tuple with ("lambda-invoke.md", 65)
    '''
    markdown_file_name = process.extractOne(task_folder_name, all_markdown_files)
    logging.info(
        "get_matching_doc - match " + task_folder_name + " to " +
         str(markdown_file_name)
    )
    
    with open(os.path.join(aws_toolkit_docs, markdown_file_name[0]), "r") as md_file:
        markdown_content = md_file.read()
    
    logging.info("get_matching_doc - read markdown content")

    return(markdown_file_name[0], markdown_content)


def get_doc_line_locations(markdown_content):
    """Gets the doc string line locations for inserting new documentation

        Parameters
        ----------
        markdown_content : str
            content of the markdown file

        Returns
        -------
        yaml_start_line : str
            Where to begin inserting data type information for the
            azure pipelines yaml
        
        parameters_start_line : str
            where the parameters section begins in the markdown task definition

        Raises
        ------
    """
    line_counter = 0
    yaml_start_line = None
    parameters_start_line = None

    for markdown_file_line in markdown_content.splitlines():

        '''
            want to start before this Description markdown section        
            ## Description<a name="description"></a>

        '''
        if markdown_file_line.lower().startswith("## description<a"):
            yaml_start_line = line_counter - 1

        '''
            parameters section begins after this markdown header
            ## Parameters<a name="parameters"></a>
        '''
        if markdown_file_line.lower().startswith("## parameters<a"):
            parameters_start_line = line_counter + 1

        line_counter += 1

    return(yaml_start_line, parameters_start_line)

def main(aws_toolkit_source="../awstoolkitsource/Tasks", 
    aws_toolkit_docs="../awstoolkitdocs/doc_source"):
    """Main entry point into script

        Parameters
        ----------
        aws_toolkit_source : str
            path to aws toolkit source code. Defaults ../awstoolkitsource/Tasks
            https://github.com/aws/aws-toolkit-azure-devops

        aws_toolkit_docs : str
            path to aws toolkit docs code. Defaults ../awstoolkitdocs/doc_source
            https://github.com/awsdocs/aws-tools-ado-vsts-user-guide

        Returns
        -------

        Raises
        ------
    """
    get_logger()
    
    for devops_task_folder in os.listdir(aws_toolkit_source):
        logging.info("main - devops_task" + devops_task_folder)
        try:
            with open(os.path.join(aws_toolkit_source, devops_task_folder, 
                "task.json"), "r") as devops_task:            
                devops_task_definition = json.load(devops_task)
                markdown_file_name, markdown_content = get_matching_doc(
                    aws_toolkit_docs=aws_toolkit_docs,
                    task_folder_name=devops_task_folder
                )

        except FileNotFoundError:
            logging.exception("main - task.json not found")
            
    

if __name__ == "__main__":
    main()