def gcode_to_svg(input_file, output_file):
    with open(input_file, 'r') as gcode:
        lines = gcode.readlines()
    
    svg_content = []
    current_position = (0, 0)
    path_data = []

    for line in lines:
        line = line.strip()
        if not line or line.startswith(';'): 
            continue
        
        if line.startswith('G0') or line.startswith('G1'):
            try:
                parts = line.split()
                x = current_position[0]
                y = current_position[1]

                for part in parts:
                    if part.startswith('X'):
                        x = float(part[1:])
                    elif part.startswith('Y'):
                        y = float(part[1:])
                
                if line.startswith('G0'):
                    current_position = (x, y)
                elif line.startswith('G1'):
                    if not path_data:
                        path_data.append(f'M{x},{y} ')
                    else:
                        path_data.append(f'L{x},{y} ')
                    current_position = (x, y)
            except (IndexError, ValueError):
                print(f"Warning: Skipping malformed line: {line}")
                continue
    
    svg_content.append('<svg xmlns="http://www.w3.org/2000/svg" version="1.1">')
    svg_content.append('<path d="' + ''.join(path_data) + '" stroke="black" fill="none"/>')
    svg_content.append('</svg>')
    
    with open(output_file, 'w') as svg_file:
        svg_file.write(''.join(svg_content))


if __name__ == "__main__":
    input_file = r'C:\Users\janek\Downloads\input1\input1.gcode'   
    output_file = r'C:\Users\janek\Downloads\output\index.html'   

    gcode_to_svg(input_file, output_file)
    print(f'Conversion from {input_file} to {output_file} completed.')
