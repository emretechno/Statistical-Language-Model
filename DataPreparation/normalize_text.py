import re

# This function replaces Turkish characters with English equivalent characters
def normalize_turkish_to_english(text):
    # Define mapping from Turkish characters to English characters
    mapping_turkish = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    
    return text.translate(mapping_turkish).lower()  # Translate the text to English characters and convert it to lowercase

def normalize_the_file(file_path):
    try:
        # First, read the file content in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Filter out lines containing unnecessary symbols like </doc> or <doc ...>
        cleaned_lines = [line for line in lines if not re.match(r"</?doc\b.*?>", line)]
        
        # Normalize the text
        normalized_text = normalize_turkish_to_english("".join(cleaned_lines))
        
        # Open the file in write mode and write the normalized text
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(normalized_text)
        
        print(f"File {file_path} is normalized from Turkish to English successfully.\n")
    except Exception as e:
        print(f"The file wasn't found. Check the path and filename: {e}")

