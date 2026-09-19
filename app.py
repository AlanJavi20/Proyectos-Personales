import os
import easyocr
import tkinter as tk
from tkinter import filedialog

def seleccionar_imagen():
    """Abre una ventana para que escojas la imagen en tu PC."""
    root = tk.Tk()
    root.withdraw() # Oculta la ventana principal de Tkinter para que solo se vea el explorador
    
    # Abre el explorador de archivos filtrando por imágenes comunes
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona una imagen con texto",
        filetypes=[
            ("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.webp"),
            ("Todos los archivos", "*.*")
        ]
    )
    return ruta_archivo

def leer_texto_con_easyocr(ruta_imagen):
    if not ruta_imagen or not os.path.exists(ruta_imagen):
        return "No se seleccionó ninguna imagen o la ruta no es válida."

    try:
        print("\nCargando el modelo de EasyOCR (la primera vez puede demorar un momento)...")
        # Inicializamos el lector para español e inglés
        lector = easyocr.Reader(['es', 'en'])
        
        print("Procesando imagen seleccionada...")
        resultados = lector.readtext(ruta_imagen, detail=0)
        
        texto_completo = "\n".join(resultados)
        return texto_completo
    except Exception as e:
        return f"Ocurrió un error al procesar la imagen: {e}"

if __name__ == "__main__":
    print("=== PROTOTIPO DE OCR CON SELECTOR DE ARCHIVOS ===")
    input("Presiona Enter para abrir el explorador de archivos y elegir tu imagen...")
    
    # Llama a la función que abre la ventana flotante
    ruta_imagen = seleccionar_imagen()
    
    if ruta_imagen:
        print(f"\nArchivo seleccionado: {ruta_imagen}")
        resultado = leer_texto_con_easyocr(ruta_imagen)
        
        print("\n--- TEXTO TRANSCRITO ---")
        print(resultado)
        print("------------------------")
    else:
        print("\nOperación cancelada. No se seleccionó ningún archivo.")