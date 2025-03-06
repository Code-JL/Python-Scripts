import os

def load_replacement_pairs(key_file):
    """Load replacement pairs from Key.txt"""
    replacements = {}
    with open(key_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                old, new = line.split(None, 1)  # Split on first whitespace
                replacements[old] = new
    return replacements

def apply_replacements(content, replacements):
    """Apply all replacements to the content"""
    for old, new in replacements.items():
        content = content.replace(old, new)
    return content

def process_file(input_file, replacements):
    """Process a single file and return its new content and new filename"""
    # Read the file content
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Apply replacements to content
    new_content = apply_replacements(content, replacements)
    
    # Apply replacements to filename
    new_filename = os.path.basename(input_file)
    new_filename = apply_replacements(new_filename, replacements)
    
    return new_content, new_filename

def main():
    # Create Output directory if it doesn't exist
    if not os.path.exists('Output'):
        os.makedirs('Output')
    
    # Load replacement pairs
    replacements = load_replacement_pairs('Input/Key.txt')
    
    # Read files list
    with open('Input/Files.txt', 'r') as f:
        files = [line.strip() for line in f if line.strip()]
    
    # Process each file
    for input_file in files:
        try:
            new_content, new_filename = process_file(input_file, replacements)
            
            # Write the new content to the output file
            output_path = os.path.join('Output', new_filename)
            with open(output_path, 'w') as f:
                f.write(new_content)
                
            print(f"Processed {input_file} -> Output/{new_filename}")
            
        except Exception as e:
            print(f"Error processing {input_file}: {str(e)}")

if __name__ == "__main__":
    main()
