## Made by Gekko

import os
import PyPDF2
from collections import Counter
import re

def merge_pdfs(pdf_list, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

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
    pdf_list = ['files/file1.pdf', 'files/file2.pdf', 'files/file3.pdf']  # Replace with your PDF files
    output_pdf = 'merged.pdf'
    merge_pdfs(pdf_list, output_pdf)

    # Example usage for text file analysis
    text_file = 'files/example.txt'  # Replace with your text file
    analyze_text_file(text_file)

if __name__ == "__main__":
    main()