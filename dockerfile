#Uses Python 3.11
FROM python:3.11

#Establish work directory
WORKDIR /usr/src/app

#Copy current dir contents into container
COPY . .


#Install needed packages
RUN pip install --no-cache-dir -r requirements.txt


#Run app when container launches
CMD ["python3", "./imageManipulation.py"]
