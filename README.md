AWS App2Container (A2C) workflow automation using ansible.
This is an example of using Ansible to automate the AWS App2Container workflow.

Summary
------------
This project demonstrates how to automate the AWS App2Container workflow by using ansible.
It automates the below steps :
  * Checks the pre-requisites needed to install AWS App2Container
  * Install AWS App2Container
  * Builds an inventory of applications and analyze the applications
  * Containerize the applications
  * Generate deployments
  * Generate pipeline
  * Deploy the deployments and the pipeline


Disclaimer
------------
This project is an example of an automation and meant to be used for testing and learning purposes only.
Be aware that the automation is not covered by the AWS free tier.
Please use the AWS pricing calculator for estimation beforehand.
This playbook is tested on Amazon Linux 2.

Prerequisites
------------

* An AWS account.
* An IAM user. Please refer to the link for more information. (https://docs.aws.amazon.com/app2container/latest/UserGuide/iam-a2c.html)
* AWS profile configured on the application servers or worker machine.
* An Amazon S3 bucket.
* A running java application.

Role Variables
--------------
user:          Sudo user

workspace_dir: Workspace directory where all the work will be saved.

awsProfile:    AWS profile configured on the application or the worker server.

s3Bucket:      The S3 bucket for application artifacts.

deployTarget: The target environment. Possible option ECS or EKS. Default is ECS.

deployEnv:    The pipeline environment. Possible option beta or prod. Default is beta.

deploy:       Flag to deploy the generated artifacts. Possible option true or false. Default is true.

worker_mode:  Flag to use the worker mode or not. Possible option true or false. Default is true.

containerParameters_containerBaseImage: The base image to use for the container.

containerParameters_appExcludedFiles:  A list of paths to exclude while containerizing.

containerParameters_appSpecificFiles:  A list of paths to include while containerizing.

containerParameters_applicationMode:  Application mode flag. Possible option true or false.

containerParameters_logLocations: List of path where the logs are located.


Tags Support
--------------
prerequisite: Run task necessary to check the prerequisites needed for AWS App2Container

install:      Run task necessary to install AWS App2Container

init:         Run task necessary to initialize AWS App2Container

inventory:    Run task necessary to discover the applications on the applications servers

analyze:      Run task necessary to analyse the applications on the applications servers

extract:      Run task necessary to extract the applications

containerize: Run task necessary to containerise the applications

gen_deploy:   Run task necessary to generate the deployment artifacts

gen_pipeline: Run task necessary to generate the pipeline artifacts


Inventory
------------
onPremisesApplicationServer: The list of unique server running unique applications.
If there is one application running on 5 servers, mention one of the server.

onPremisesWorkerServer: Server where all the containerizing step will be performed. This server is needed only
if the flag worker_mode is set to true. If the same is false this section has no impact on the run.


Example Playbook
----------------
To run the playbook

ansible-playbook -i inventory.ini main.yml -e s3Bucket=<S3 Bucket> -e awsProfile=<awsProfile to use>

To discover all Java applications

ansible-playbook -i inventory.ini main.yml -e s3Bucket=<S3 Bucket> -e awsProfile=<awsProfile to use> --tags inventory

To Containerize a specific application id from the list of applications discovered

ansible-playbook -i inventory.ini main.yml -e s3Bucket=<S3 Bucket> -e awsProfile=<awsProfile to use> --appid <>

## Security

 See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

 This library is licensed under the MIT-0 License. See the LICENSE file.
