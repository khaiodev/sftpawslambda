# sftpawslambda

Usei o "pysftp", para isso é necessário adicionar uma camada(layer) para que o Python consigo dar o import.

1.    In the AWS Cloud9 console, create an Amazon Elastic Compute Cloud (Amazon EC2) instance with Amazon Linux 2 AMI. For instructions, see Creating an EC2 environment in the AWS Cloud9 User Guide.

2.    Create an AWS Identity and Access Management (IAM) policy that grants permissions to call the PublishLayerVersion API operation.

Example IAM policy statement that grants permissions to call the PublishLayerVersion API operation

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "lambda:PublishLayerVersion",
            "Resource": "*"
        }
    ]
}
3.    Create an IAM role and attach the IAM policy to the role. Then, attach the IAM role to the Amazon EC2 instance.

Note: Your EC2 instance now has permissions to upload Lambda layers for the PublishLayerVersion API call.

4.    Open your AWS Cloud9 Amazon EC2 environment. Then, install Python 3.8 and pip3 by running the following commands:

$ sudo amazon-linux-extras install python3.8
$ curl -O https://bootstrap.pypa.io/get-pip.py
$ python3.8 get-pip.py --user
5.    Create a python folder by running the following command:

$ mkdir python
6.    Install the Pandas library files into the python folder by running the following command:

Important: Replace Pandas with the name of the Python library that you want to import.

$ python3.8 -m pip install pandas -t python/
7.    Zip the contents of the python folder into a layer.zip file by running the following command:

$ zip -r layer.zip python
8.    Publish the Lambda layer by running the following command:

Important: Replace us-east-1 with the AWS Region that your Lambda function is in.

$ aws lambda publish-layer-version --layer-name pandas-layer --zip-file fileb://layer.zip --compatible-runtimes python3.8 --region us-east-1
9.    Add the layer to your Lambda function.
