import os
import random
import shutil
from pathlib import Path
from faker import Faker
from docx import Document
from PIL import Image
from fpdf import FPDF

# Initialize Faker for generating random data
faker = Faker()

# Define the base directory
base_directory = "test"
folders = ["folder_1", "folder_2", "folder_3", "folder_4"]
file_types = ['pdf', 'png', 'docx']

# Function to create a sample PDF
def create_pdf(file_path, content):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    pdf.output(file_path)

# Function to create a sample PNG
def create_png(file_path):
    img = Image.new('RGB', (200, 200), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    img.save(file_path)

# Function to create a sample DOCX
def create_docx(file_path, content):
    doc = Document()
    doc.add_paragraph(content)
    doc.save(file_path)

def create(dir):
    base_directory = dir
    # Ensure the base directory is clean
    if os.path.exists(base_directory):
        shutil.rmtree(base_directory)
    os.makedirs(base_directory)
    # Create folders and populate with files
    for folder in folders:
        folder_path = os.path.join(base_directory, folder)
        os.makedirs(folder_path, exist_ok=True)

        for i in range(3):  # Create 3 random files per folder
            file_name = f"{faker.word()}_{i}"
            file_extension = random.choice(file_types)
            file_path = os.path.join(folder_path, f"{file_name}.{file_extension}")
            
            # Generate different types of files
            if file_extension == "pdf":
                create_pdf(file_path, faker.text())
            elif file_extension == "png":
                create_png(file_path)
            elif file_extension == "docx":
                create_docx(file_path, faker.text())

    print(f"Folders and files created successfully in '{base_directory}'")