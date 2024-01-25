import PyPDF2
from docx import Document
def pdf_to_word_converter(input_pdf_path,output_doc_path):
    pdf = PyPDF2.PdfReader(input_pdf_path)
    doc = Document()
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        text = page.extract_text()
        doc.add_paragraph(text)
    doc.save(output_doc_path)
    print(f"PDF successfully converted to the word document. Output.doc save at:{output_doc_path}")

input_pdf_path = r"C:\Users\ACER\Downloads\Lab Problems on ARRAY.pdf"
output_doc_path = r"C:\Users\ACER\Downloads\output.doc"
pdf_to_word_converter(input_pdf_path,output_doc_path) 