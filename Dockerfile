#Using the base image with python 3.7
FROM python:3.7

# Create directory
RUN mkdir /yelpapi

#Set our working directory as app
WORKDIR /yelpapi

# Copy yelpapi contents to new directory
COPY . .

#Installing requirements.txt from pip
RUN pip3 install -r requirements.txt

#Exposing the port 5000 from the container
EXPOSE 5000

#Starting the python application
CMD python3 run.py