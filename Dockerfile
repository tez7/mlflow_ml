# # Base image
FROM python:3.8-slim-buster

#Installs the AWS Command Line Interface (CLI). It first updates the package lists (apt update -y) and then installs the awscli package, allowing the container to interact with Amazon Web Services (S3, ECR, etc.)
RUN apt update -y && apt install awscli -y

#Sets the working directory inside the container to /app. All subsequent commands (COPY, RUN, CMD) will be executed relative to this directory unless an absolute path is provided
WORKDIR /app

#Copies files from the host. It takes all files and folders from the current directory on your local machine (.) and copies them into the working directory (/app) inside the container. This includes your app.py, requirements.txt, and source code
COPY . /app

#Installs the Python packages listed in requirements.txt. It uses pip, the Python package installer, to read the requirements.txt file and install all specified dependencies into the container's Python environment
RUN pip install -r requirements.txt

#Specifies the command to run when the container starts. In this case, it runs the app.py script using Python. This is typically where your application logic would be executed when the container is launched
#Defines the command to run when the container starts. When a container is launched from this image, it will execute the command python app.py, which starts your main Flask application
CMD ["python", "app.py"]