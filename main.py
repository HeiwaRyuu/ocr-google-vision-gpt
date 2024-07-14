from gpt_open_ai_ocr_correction import correct_text
from ocr_google_cloud_vision import detect_text

import os

def main():
    for i in range(3):
        # Extraí o texto usando o Google Vision
        file_path = os.getcwd() + f"/images/joao-teixeira-alves-neto-prontuario_page-000{i+1}.jpg"
        ocr_text = detect_text(file_path)

        # Corrige o texto usando o ChatGPT
        texto_final = correct_text(ocr_text)

        # Read the text recognition output from the processor
        filename = file_path.split('/')[-1].split('.')[0] + '.txt'
        output_file_path = rf'{os.getcwd()}\results\{filename}'
        with open(output_file_path, 'w+') as f:
            f.write(texto_final)

        print(f"The document has been processed and its contents saved to {output_file_path}")

if __name__ == "__main__":
    main()