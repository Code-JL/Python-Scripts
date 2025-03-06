def read_key_file(file_path):
    """Read the key file and create a dictionary mapping numbers to letters/words."""
    key_dict = {}
    try:
        # Explicitly specify encoding and handle both \t and spaces
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Split on whitespace and filter out empty strings
                parts = [part for part in line.split() if part]
                if len(parts) >= 2:
                    number = parts[0]
                    letter = parts[1]
                    key_dict[number] = letter
        print(f"Successfully loaded key dictionary: {key_dict}")
        return key_dict
    except Exception as e:
        print(f"Error reading key file: {e}")
        return {}

def process_file(input_file, output_file, key_dict):
    """Replace numbers in input file with corresponding values from key dictionary."""
    try:
        with open(input_file, 'r', encoding='utf-8') as fin, \
             open(output_file, 'w', encoding='utf-8') as fout:
            for line in fin:
                parts = line.strip().split()
                replaced_parts = []
                
                for part in parts:
                    part = part.strip()
                    if part in key_dict:
                        replaced_parts.append(key_dict[part])
                    else:
                        replaced_parts.append(part)
                
                output_line = '\t'.join(replaced_parts)
                fout.write(output_line + '\n')
    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    import os
    
    # Ensure Output directory exists
    os.makedirs('Output', exist_ok=True)
    
    # Read the key file
    key_dict = read_key_file('Input/Key.txt')
    
    if not key_dict:
        print("Error: Key dictionary is empty!")
        return
    
    # Process the NumReel file
    process_file('Input/NumReel.txt', 'Output/Reels.txt', key_dict)
    
    print("Replacement complete. Check Output/Reels.txt")

if __name__ == "__main__":
    main()