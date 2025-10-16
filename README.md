# mlflow_ml

## Workflows

1. Update config.yaml
2. Update schema.yaml #(columns you have in you data)
3. Update params.yaml #(parameters - provide value here instead of run time)
4. Update the config.entity #()
5. Update the configuration manager(i.e configuration.py ) in src config #()
6. Update the components #(update data ingestion, validation)
7. Update the pipeline #(all component will be implemented via pipeline)
8. Update the main.py #()
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)
pip3 install mlflow


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)


MLFLOW_TRACKING_URI=https://dagshub.com/tez7/mlflow_ml.mlflow \
MLFLOW_TRACKING_USERNAME=tez7 \
MLFLOW_TRACKING_PASSWORD=be4cff9191bdcbbe7ccd24845978958de0c5553b \
python script.py


Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/tez7/mlflow_ml.mlflow

export MLFLOW_TRACKING_USERNAME=tez7 

export MLFLOW_TRACKING_PASSWORD=6b89a6bd0668b9beb9b3ba3484190e94c10ff4fb

```
### """Experiment Tracking and Management: DagsHub integrates with MLflow to provide a remote server for logging, tracking, and comparing machine learning experiments. Users can view and manage experiment results, hyperparameters, and trained models through a built-in UI, facilitating analysis and reproducibility"""


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model