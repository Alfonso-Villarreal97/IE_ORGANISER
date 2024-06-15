from controller import extract_pdf_information, generate_prompt, process_response, request_anthropic

# Aquí se importaría Tkinter para construir la interfaz gráfica
# Ejemplo básico con Tkinter
import tkinter as tk
from tkinter import messagebox

def main():
    # Ruta del archivo PDF (en este caso 'Test1.pdf' está en el mismo directorio)
    pdf_path = 'Test1.pdf'
    
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
