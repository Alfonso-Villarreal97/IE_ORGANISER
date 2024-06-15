import os
import PyPDF2
import anthropic
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API desde las variables de entorno
api_key = os.getenv("ANTHROPIC_API_KEY")

# -- Extraer información de un documento -- #
pdf_file_obj = open('Test1.pdf', 'rb')  # Documento en hardcode
reader = PyPDF2.PdfReader(pdf_file_obj)

pre_process_info = ""

for num_page in range(len(reader.pages)):
    info_page = reader.pages[num_page]
    extract_info = info_page.extract_text()
    pre_process_info += extract_info.strip() + " "  # Data extraída

# -- Inicio de consumo -- #
system_prompt = "Eres un asistente muy útil"
question = (f"Con base a la siguiente información: {pre_process_info}"
            "\n\nExtrae unicamente el RFC de la persona," 
            "el RFC de la empresa, el nombre de la persona y el nombre de la empresa:"
            "\nTe doy ejemplos de las características que deben tener estos datos:"
            "\n1.- Nombre de persona, receptor o cliente: DIEGO ALFONSO TREJO VILLARREAL"
            "\n2.- Nombre de persona, receptor o cliente: : JOSE GABRIEL NARO RODRIGUEZ"
            "\n3.- Nombre de empresa, emisor o establecimiento: DISTRIBUIDORA LIVERPOOL"
            "\n4.- Nombre de empresa, emisor o establecimiento: HOME DEPOT MEXICO"
            "\n5.- RFC de la empresa: HDM001017AS1"
            "\n6.- RFC de la empresa: GDM002018AS2"
            "\n7.- RFC de la persona: TEVD971127RU1"
            "\n8.- RFC de la persona: SUGG510625ER7"
            )

prompt = f'{system_prompt}\n\nHuman: {question}\n\nAssistant:'

client = anthropic.Client(api_key=api_key)

response = client.completions.create(
    model="claude-2",
    prompt=prompt,
    max_tokens_to_sample=300,
)

print(response.completion)
