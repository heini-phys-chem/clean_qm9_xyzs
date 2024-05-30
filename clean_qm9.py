import os
import re

from tqdm import tqdm


def convert_scientific_notation(number_str):
    """Convert a scientific notation string with '*' to a float."""
    return float(number_str.replace('*^', 'e'))

def process_xyz_file(filepath):
    """Read, process, and rewrite the XYZ file to correct the scientific notation."""
    with open(filepath, 'r') as file:
        lines = file.readlines()

    corrected_lines = []
    for line in lines:
        corrected_line = re.sub(r'(\d+\.\d+)\*\^(-?\d+)',
                                lambda match: str(convert_scientific_notation(match.group(0))),
                                line)
        corrected_lines.append(corrected_line)

    with open(filepath, 'w') as file:
        file.writelines(corrected_lines)

def process_all_xyz_files(directory):
    """Process all XYZ files in the given directory."""
    for filename in tqdm(os.listdir(directory), desc="Clean QM9"):
        if filename.endswith(".xyz"):
            filepath = os.path.join(directory, filename)
            process_xyz_file(filepath)

def main():
    directory = 'xyzs'
    process_all_xyz_files(directory)


if __name__ == '__main__':
    main()
