import PyPDF2
import docx

def extract_text(file_path):
    """Extracts text from a PDF or DOCX file.

    Args:
        file_path (str): Path to the PDF or DOCX file.

    Returns:
        str: The extracted text, or None if an error occurs.
    """

    try:
        if file_path.endswith(".pdf"):
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
                return text

        elif file_path.endswith(".docx"):
            doc = docx.Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text

        else:
            print("Unsupported file format.")
            return None

    except Exception as e:
        print(f"Error extracting text: {e}")
        return None