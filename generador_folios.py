import hashlib
#Generador de Código para Curso El Diario Oficial - INC | ¿Cómo publicar a tiempo?
#El Certificado de Finalización del curso de sensibilización es la relación de las y los aliados institucionales de Gobierno con quienes la INC mantendrá contacto
#Estas serán las personas que motivarán el cambio cultural desde la planeación de la publicación de los documentos que enviarán a la INC para publicarlos en el Diario Oficial
def generar_folio_inc(cedula, curso="GC"):
    # Parámetros institucionales
    prefijo = f"INC-EICE-2026-{curso}"
    
    # Creación del Hash seguro (SHA-256) basado en la cédula
    # Esto garantiza que el código sea único para cada persona
    hash_objeto = hashlib.sha256(cedula.encode())
    hash_hex = hash_objeto.hexdigest()[:7].upper() # Tomamos 7 caracteres
    
    # Dígito de verificación simple (puede ser el último caracter del hash)
    dv = hash_hex[-1]
    
    return f"{prefijo}-{hash_hex}-{dv}"

# Ejemplo de uso:
estudiante_id = "1010203040"
nuevo_folio = generar_folio_inc(estudiante_id)
print(f"Folio generado para el Diario Oficial: {nuevo_folio}")
