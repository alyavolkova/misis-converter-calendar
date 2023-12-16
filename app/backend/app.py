from typing import Union

from fastapi import FastAPI, UploadFile

app = FastAPI()


def save_file(file: UploadFile):
    """

    :param file:
    """
    file_path = "./target_docs.docx"
    with open(file_path, "wb") as f:
        f.write(file.file.read())


@app.get("/")
def read_root():
    return {"Response": "Тут будет лицо сайта"}


@app.post("/processing_docs")
def read_item(file: UploadFile, setup: str):
    """
    Endpoint for save file in container
    :param file: target file
    :param setup: metadata
    :return:
    """
    save_file(file=file)
    return {"filename": file.filename, "Что-то": setup}
