* **Docker is a powerful platform that has revolutionized the development and distribution of applications by utilizing containerization, a lightweight alternative to full machine virtualization. Containerization involves encapsulating an application and its environment—dependencies, libraries, and configuration files—into a container, which is a portable and consistent unit of software.**

* Unlike traditional virtual machines that replicate an entire operating system, Docker containers share the host system's kernel, making them much more efficient, fast to start, and less resource-intensive. 

* Creating a Simple Machine Learning Application
For this tutorial, let's create a simple Python application that uses the Scikit-learn library to train a model on the Iris dataset.

## Basic ML Steps

1. Create a Project Directory and create a virtual env
Open your terminal or command prompt and run the following:

        mkdir ml-docker-app  
        cd ml-docker-app

2. Create a requirements.txt File
List the Python packages that your application requires. For our simple ML application:

        scikit-learn==1.0.2   
        pandas==1.3.5   
        joblib==1.1.0

3. Create the Machine Learning Application Script

4. Install the Dependencies
Run the following command to install the dependencies listed in requirements.txt:  
`pip install -r requirements.txt`

5. Run Your Application
Run your application to make sure it works:
`python3 app.py`

## Containerize the Application with Docker
Create a file named `Dockerfile` 

1. Build the Docker Image   
Run the following command in your terminal to build the Docker image:   
`docker build -t ml-docker-app`

2. Run the Docker Container  
Once the image is built, run your application in a Docker container:   
`docker run ml-docker-app`

- If everything is set up correctly, Docker will run your Python script inside a container, and you should see the accuracy of the model outputted to your terminal, just like when you ran the script natively.

- Tag & Push the Container to DockerHub    
Log in to Docker Hub from the Command Line
Once you have a Docker Hub account, you need to log in through the command line on your local machine. Open your terminal and run:   
`docker login`

- Tag Your Docker Image   
Before you can push an image to Docker Hub, it must be tagged with your Docker Hub username. If you don’t tag it correctly, Docker will not know where to push the image.
Assuming your Docker ID is username and you want to name your Docker image ml-docker-app, run:  
`docker tag ml-docker-app username/ml-docker-app`
- Push the Image to Docker Hub   
To push the image to Docker Hub, use the docker push command followed by the name of the image you want to push:   
`docker push username/ml-docker-app`


