from typing import Union
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


file_path = "./target_docs.docx"
processed_file_path = "target_file.docx"


def change_font(doc, font_name, font_size):
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.font.name = font_name
            run.font.size = Pt(font_size)
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT


def process_word_file(input_file, output_file):
    doc = Document(input_file)
    font_name = 'Times New Roman'
    font_size = 12
    change_font(doc, font_name, font_size)
    doc.save(output_file)


def save_file(file: UploadFile):
    """

    :param file:
    """
    with open(file_path, "wb") as f:
        f.write(file.file.read())


@app.get("/")
def read_root():
    return {"Response": "Тут будет лицо сайта"}


@app.post("/processing_docs")
def read_item(file: UploadFile):
    """
    Endpoint for save file in container
    :param file: target file
    :return:
    """
    save_file(file=file)
    process_word_file(file_path, processed_file_path)

    return {"filename": file.filename}


@app.get("/download_processed_file")
def download_processed_file():
    return FileResponse(path=processed_file_path, filename="processed_file.docx", media_type="application/octet-stream")
