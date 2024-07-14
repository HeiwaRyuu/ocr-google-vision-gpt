import os

credential_path = r"C:\Users\clib_\AppData\Roaming\gcloud\application_default_credentials.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    
    full_ocr_text = texts[0]
    return full_ocr_text.description

def main():
    for i in range(3):
        path = os.getcwd() + f"/images/joao-teixeira-alves-neto-prontuario_page-000{i+1}.jpg"
        detect_text(path)

if __name__ == "__main__":
    main()