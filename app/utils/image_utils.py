import tempfile

def save_temp_image(upload_file):
    """Save uploaded image temporarily."""
    temp = tempfile.NamedTemporaryFile(delete=False)
    content = upload_file.file.read()
    temp.write(content)
    temp.close()
    return temp.name
