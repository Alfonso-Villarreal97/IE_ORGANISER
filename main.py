from controller.controller import generate_prompt, request_anthropic, process_response
from model.model import extract_pdf_information
import tkinter as tk
from tkinter import messagebox

def main():
    # Ruta del archivo PDF (en este caso 'Test1.pdf' está en la carpeta resources)
    pdf_path = 'resources/Test1.pdf'
    
    # Extraer información del PDF
    pre_process_info = extract_pdf_information(pdf_path)
    
    # Generar prompt para Anthropic
    prompt = generate_prompt(pre_process_info)
    
    # Hacer solicitud a Anthropic
    response_text = request_anthropic(prompt)
    
    # Procesar la respuesta de Anthropic
    rfc_persona, nombre_persona, rfc_empresa, nombre_empresa = process_response(response_text)
    
    # Mostrar los resultados (ejemplo con messagebox de Tkinter)
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    
    messagebox.showinfo("Resultados",
                        f"RFC Persona: {rfc_persona}\n"
                        f"Nombre Persona: {nombre_persona}\n"
                        f"RFC Empresa: {rfc_empresa}\n"
                        f"Nombre Empresa: {nombre_empresa}")
    
    root.destroy()  # Cerrar la ventana al cerrar el messagebox

if __name__ == "__main__":
    main()
"""
TODO:   Fase I: Extracción de datos [Completa]
        Fase II: Settear valor obtenidos en variables [Completa]
        Fase III: A partir de las variables, estructurar las carpetas [*]
            Fase a): Establecer y diseñar como funcionaría eso con una interfaz gráfica,
            Cómo se elegirían los parámetros (Diseñar la interfaz) [*]
        Fase IV: Aplicar lo anterior a 'N' Archivos [*]
        
"""