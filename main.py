from gpt_open_ai_ocr_correction import correct_text
from ocr_google_cloud_vision import detect_text

import os

def save_text(file_path, file_extension, data):
    filename = file_path.split('/')[-1].split('.')[0] + file_extension
    output_file_path = rf'{os.getcwd()}\results\{filename}'
    with open(output_file_path, 'w+', encoding='utf-8') as f:
        f.write(data)
    return output_file_path

def main():
    base_path = os.getcwd() + "/images/images"
    for file_path in os.listdir(base_path):
        file_path = base_path+"/"+file_path
        # Extract text via OCR using Google Vision
        ocr_text = detect_text(file_path)

        # Correct OCR mistakes using ChatGPT
        final_text = correct_text(ocr_text)

        # Save the raw output in '.txt' and a json version of it
        save_text(file_path, "_raw.txt", ocr_text)

        output_file_path = save_text(file_path, ".json", final_text)
        
        print(f"The document has been processed and its contents saved to:\n {output_file_path}")

if __name__ == "__main__":
    main()