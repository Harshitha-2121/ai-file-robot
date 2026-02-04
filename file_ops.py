import os
import shutil

FOUND_PDFS = []

def find_all_pdfs(start_path="C:\\"):
    global FOUND_PDFS
    FOUND_PDFS = []

    for root, _, files in os.walk(start_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                FOUND_PDFS.append(os.path.join(root, file))

    return FOUND_PDFS


def move_pdfs(folder_name="All_PDFs"):
    if not FOUND_PDFS:
        return "No PDFs found. Run find command first."

    destination = os.path.join("C:\\", folder_name)
    os.makedirs(destination, exist_ok=True)

    moved = 0
    for pdf in FOUND_PDFS:
        try:
            shutil.move(pdf, destination)
            moved += 1
        except:
            pass

    return f"Moved {moved} PDFs to {destination}"
