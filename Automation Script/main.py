## Made by Gekko

import os
import PyPDF2
from collections import Counter
import re

def merge_pdfs(pdf_list, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"Merged {len(pdf_list)} PDFs into {output_path}")

def analyze_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Remove punctuation and make lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()

    # Count characters
    char_count = len(text)

    # Count words
    words = text.split()
    word_count = len(words)

    # Count word frequency
    word_freq = Counter(words)

    print(f"Analysis of {file_path}:")
    print(f"Character count: {char_count}")
    print(f"Word count: {word_count}")
    print("Word frequency:")
    for word, freq in word_freq.most_common(10):
        print(f"{word}: {freq}")

def main():
    # Example usage for PDF merging
    pdf_list = ['Automation Script/files/file1.pdf', 'Automation Script/files/file2.pdf', 'Automation Script/files/file3.pdf']  # Replace with your PDF files
    output_pdf = 'Automation Script/merged.pdf'
    merge_pdfs(pdf_list, output_pdf)

    # Example usage for text file analysis
    text_file = 'Automation Script/files/example.txt'  # Replace with your text file (if you don't have one, you can use the example.txt file in the files folder)
    # text_file = 'Automation Script/files/RomeoAndJuliet.txt' # Uncomment this line to analyze Romeo and Juliet
    analyze_text_file(text_file)

if __name__ == "__main__":
    main()