import os
import anthropic
from dotenv import load_dotenv
from model.model import extract_pdf_information  # Asegúrate de importar desde el módulo correcto

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def generate_prompt(pre_process_info):
    """
    Genera el prompt para enviar a Anthropic.
    
    Args:
    - pre_process_info (str): Texto extraído del PDF.
    
    Returns:
    - str: Prompt formateado para Anthropic.
    """
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
                "Nota importante: Necesito que formatees lo que encuentres de la siguiente manera"
                "Nombre Persona: "
                "RFC Persona: "
                "Nombre Empresa: "
                "RFC Empresa: "
                "Si no hayas alguna información, rellena los formatos como 'No encontrado'"
                )
    
    prompt = f'{system_prompt}\n\nHuman: {question}\n\nAssistant:'
    return prompt

def process_response(response_text):
    """
    Procesa la respuesta obtenida de Anthropic y devuelve los datos relevantes.
    
    Args:
    - response_text (str): Texto generado por Anthropic.
    
    Returns:
    - tuple: Tupla con los valores de RFC Persona, Nombre Persona, RFC Empresa, Nombre Empresa.
    """
    # Definimos las variables donde almacenaremos la información
    rfc_persona = "No encontrado"
    nombre_persona = "No encontrado"
    rfc_empresa = "No encontrado"
    nombre_empresa = "No encontrado"

    # Buscamos y extraemos la información necesaria del texto
    lines = response_text.splitlines()

    for line in lines:
        if line.startswith("RFC Persona:"):
            rfc_persona = line.split(":")[1].strip()
        elif line.startswith("Nombre Persona:"):
            nombre_persona = line.split(":")[1].strip()
        elif line.startswith("RFC Empresa:"):
            rfc_empresa = line.split(":")[1].strip()
        elif line.startswith("Nombre Empresa:"):
            nombre_empresa = line.split(":")[1].strip()

    return rfc_persona, nombre_persona, rfc_empresa, nombre_empresa

def request_anthropic(prompt):
    """
    Realiza la solicitud a Anthropic con el prompt especificado.
    
    Args:
    - prompt (str): Prompt formateado para enviar a Anthropic.
    
    Returns:
    - str: Texto generado por Anthropic en respuesta al prompt.
    """
    # Obtener la clave API desde las variables de entorno
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    # Inicializar cliente de Anthropic
    client = anthropic.Client(api_key=api_key)
    
    # Hacer solicitud a Anthropic
    response = client.completions.create(
        model="claude-2",
        prompt=prompt,
        max_tokens_to_sample=300,
    )
    
    return response.completion

def run_pdf_processing(pdf_path):
    """
    Función para ejecutar el procesamiento del PDF.
    
    Args:
    - pdf_path (str): Ruta al archivo PDF.
    
    Returns:
    - str: Texto extraído del PDF.
    """
    return extract_pdf_information(pdf_path)
