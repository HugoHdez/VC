import os
import random
import shutil
import xml.etree.ElementTree as ET

def split_dataset(image_dir, output_dir, labels_dir, train_ratio=0.72, val_ratio=0.08, test_ratio=0.2):
    # Crear carpetas de destino
    train_dir = os.path.join(output_dir, 'train')
    val_dir = os.path.join(output_dir, 'val')
    test_dir = os.path.join(output_dir, 'test')

    # Borra los subdirectorios si existen
    remove_files(train_dir)
    remove_files(val_dir)
    remove_files(test_dir)

    # Crea los directorios de las imagenes
    os.makedirs(train_dir + r'\images', exist_ok=True)
    os.makedirs(val_dir + r'\images', exist_ok=True)
    os.makedirs(test_dir + r'\images', exist_ok=True)
     
    # Crea los directorios de los labels
    os.makedirs(train_dir + r'\labels', exist_ok=True)
    os.makedirs(val_dir + r'\labels', exist_ok=True)
    os.makedirs(test_dir + r'\labels', exist_ok=True)


    # Obtener lista de imágenes
    images = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    random.shuffle(images)  # Mezclar las imágenes

    labels = [f for f in os.listdir(labels_dir) if os.path.isfile(os.path.join(labels_dir, f))]

    # Calcular tamaños de cada subconjunto
    total_images = len(images)
    train_size = int(total_images * train_ratio)
    val_size = int(total_images * val_ratio)

    # Asignar imágenes a cada subconjunto
    train_images = images[:train_size]
    val_images = images[train_size:train_size + val_size]
    test_images = images[train_size + val_size:]

    # Mover las imágenes a las carpetas correspondientes
    for img in train_images:
        shutil.copy(os.path.join(image_dir, img), os.path.join(train_dir + r'\images', img))
        move_labels(img, train_dir)
    for img in val_images:
        shutil.copy(os.path.join(image_dir, img), os.path.join(val_dir + r'\images', img))
        move_labels(img, val_dir)
    for img in test_images:
        shutil.copy(os.path.join(image_dir, img), os.path.join(test_dir + r'\images', img))
        move_labels(img, test_dir)
        
        

    print(f"Total de imágenes: {total_images}")
    print(f"Imágenes de entrenamiento: {len(train_images)}")
    print(f"Imágenes de validación: {len(val_images)}")
    print(f"Imágenes de prueba: {len(test_images)}")

def move_labels(img, folder_dir):
    image_name, _ = os.path.splitext(img)  # Obtener el nombre sin extensión
    xml_file = f"{image_name}.xml"  # Archivo XML correspondiente
    xml_path = os.path.join(labels_dir, xml_file)
    if os.path.exists(xml_path):
        # Si el archivo XML existe, convertirlo a txt y moverlo a la carpeta labels
        xml_to_txt(xml_path, folder_dir + r'\labels')
    else:
        print(f"No se encontró {xml_file}.")
    

# Función para eliminar todos los archivos de un directorio si tiene contenido
def remove_files(path):
    if len(os.listdir(path)) == 0:
        return False
    shutil.rmtree(f'{path}')
    return True

import os
import xml.etree.ElementTree as ET

def xml_to_txt(xml_file, output_dir, class_id=0):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    size = root.find("size")
    img_width = int(size.find("width").text)
    img_height = int(size.find("height").text)

    yolo_annotations = []
    
    for obj in root.iter("object"):
        bndbox = obj.find("bndbox")
        xmin = int(bndbox.find("xmin").text)
        ymin = int(bndbox.find("ymin").text)
        xmax = int(bndbox.find("xmax").text)
        ymax = int(bndbox.find("ymax").text)

        # Convert to YOLO format
        x_center = (xmin + xmax) / 2.0 / img_width
        y_center = (ymin + ymax) / 2.0 / img_height
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}\n")

    # Save YOLO format to txt file
    txt_file = os.path.join(output_dir, os.path.basename(xml_file).replace(".xml", ".txt"))
    with open(txt_file, "w") as f:
        f.writelines(yolo_annotations)




# Uso del script
image_dir = r'F:\Universidad\Curso 2024-25\Primer Semestre\VC\Practicas\VC\Practica 4\plates\images'  # Ruta a la carpeta que contiene las imágenes
labels_dir = r'F:\Universidad\Curso 2024-25\Primer Semestre\VC\Practicas\VC\Practica 4\plates\annotations'  # Ruta a la carpeta que contiene los labels
output_dir = r'F:\Universidad\Curso 2024-25\Primer Semestre\VC\Practicas\VC\Practica 4\TGC_RBNW'  # Ruta de la carpeta para los conjuntos de salida
split_dataset(image_dir, output_dir, labels_dir)
