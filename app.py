from dotenv import load_dotenv

load_dotenv() #Loads All the Environment Variables
import base64
import streamlit as st
import os
import io
from PIL import Image 
from  PyPDF2 import PdfReader 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
  # Gemini pro response 
def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    # Get the file path from the uploaded_file object
    file_path = uploaded_file  # Assuming the name attribute contains the file path
    reader = PdfReader(open(file_path, 'rb'))
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text
        
input_prompt = """
Hey Act Like A skilled Or very experience ATS(Application Tracking System )
With a deep learning underastand of tech field ,software engineering, Datascience, Data Analyst and big engineer. your task is to evalute the resume based on the given job description you must consider the jod market is very competitive and you should provide best assistance for improving the Resumes. Assign the percentage matching based on jd and the misssing keywords with high accuracy resume{text}description{jd} i want the response in one single string having structure {{"jd Match:"%","MissingKeywords:[]","Profile Summary":""}}  """   

## Streamlit App

st.title("sriram ATS Resume EXpert")
st.text("improve your resume ATS Tracking System")
Jd=st.text_area("Paste your Job Discription")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type="pdf",help="Please Upload Your resume")


submit=st.button("Submit")

if submit:
    if uploaded_file is not None:
         text=input_pdf_text(str(uploaded_file))
         response=get_gemini_response(input_prompt)
         st.subheader(response)
       
