import PyPDF2

def extract_pdf_information(pdf_path):
    """
    Extrae información de un documento PDF.
    
    Args:
    - pdf_path (str): Ruta al archivo PDF.
    
    Returns:
    - str: Texto extraído del PDF.
    """
    pdf_file_obj = open(pdf_path, 'rb')
    reader = PyPDF2.PdfReader(pdf_file_obj)
    
    pre_process_info = ""
    for num_page in range(len(reader.pages)):
        info_page = reader.pages[num_page]
        extract_info = info_page.extract_text()
        pre_process_info += extract_info.strip() + " "  # Data extraída
        
    pdf_file_obj.close()
    return pre_process_info
