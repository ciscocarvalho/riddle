import argparse

parser = argparse.ArgumentParser(description="Remove immediate duplicate lines from file")
parser.add_argument("-i", "--input-file", help="Input file to be used", required=True)
parser.add_argument("-o", "--output-file", help="Output file to be used", required=True)
args = vars(parser.parse_args())
input_file, output_file = args["input_file"], args["output_file"]

with open(input_file) as f:
    lines = f.readlines()
    lines_new_file = []
    previous_line = None

    for line in lines:
        if previous_line is None or line != previous_line:
            lines_new_file.append(line)

        previous_line = line

    with open(output_file, "w") as f2:
        f2.writelines(lines_new_file)
