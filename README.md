# Project for sharpening skills using the Streamlit module.

## What can it do?
There are three pages: the first contains information about the state of Apple's transactions in charts; the second contains a personal study of tips based on DataFrame with the drawing of charts of the dependencies of some features on others; the third allows you to independently upload your own csv file to build charts online.

## How to download and use it in your work?
Fork the repository. There are two options - launch via Docker and via a local virtual environment.
### Dockerfile (install it first)
sudo docker build -t streamlit-pet  
sudo docker images *(take image_ID)*  
sudo docker run -p 8501:8501 *image_ID*  
### Venv
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  

After you do one of the methods, a link to the local server will appear in the terminal.

# Link to my version: https://renathedv-streamlit-pet-main-ktx1kg.streamlit.app/tips
