import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"

import numpy as np
from handwriting_synthesis import Hand
import random
from textwrap import wrap
from PyPDF4 import PdfFileMerger
from cairosvg import svg2pdf
from handwriting_synthesis import drawing

styles = []
biases = []
lines = []

# stbi = {
#     0: [.9, .7, 1.0],
#     1: [.4, 1.05],
#     3: [.65, .9],
#     4: [.9],
#     7: [.9],
#     8: [.9],
#     9: [.75, .8, .9, 1.0, 1.05],
#     12: [.75, .9, 1],
# }
# stbi = {
#     0: [random.choice([.9, .7, 1.0])],
#     1: [random.choice([.4, 1.05])],
#     3: [random.choice([.65, .9])],
#     4: [random.choice([.9])],
#     7: [random.choice([.9])],
#     8: [random.choice([.9])],
#     9: [random.choice([.75, .8, .9, 1.0, 1.05])],
#     12: [random.choice([.75, .9, 1])],
# }
# stbi = {0: [0.7]}  # Chetali
stbi = {1: [0.9]}  # Me


def hasInvalidCharacters(lines):
    char_set = set(drawing.alphabet).union(set(drawing.EXTRA_CHAR_MAP))
    flag = False
    for line_num, line in enumerate(lines):
        for char in line:
            if char not in char_set:
                print((
                    f"Invalid character \"{char}\" detected in line {line_num}.\n"
                    f"Valid character set is {char_set}.\n"
                    f"Line content: \"{line}\""
                ))
                flag = True
    return flag



def splitter(text, max_length=69):
    lines = []
    line = ""
    for line in text.split("\n"):
        wr = wrap(line, max_length)
        if wr == []:
            lines.append("")
        else:
            lines.extend(wr)
    return lines


def pdfConverter(filenames):
    pdfFiles = []
    for file in filenames:
        pdfFiles.append(f"img/dist/{file}.pdf")
        svg2pdf(url=(svg:=f"img/dist/{file}.svg"), write_to=pdfFiles[-1])
        os.remove(svg)

    merger = PdfFileMerger(strict=False)
    for pdf in pdfFiles:
        merger.append(fileobj=open(pdf, 'rb'))
        os.remove(pdf)
    merger.write(f"img/{filenames[0].split('-pg')[0]}.pdf")
    merger.close()


arr_splitter = lambda arr, size: [arr[x:x+size] for x in range(0, len(arr), size)]

linesPerPage = 28

if __name__ == '__main__':
    hand = Hand()
    try:
        lines = splitter(open('towrite.txt').read())
    except FileNotFoundError:
        raise FileNotFoundError("File 'towrite.txt' not found. Please create the file and type the text to be handwritten.")
    if hasInvalidCharacters(lines):
        print("Invalid characters detected. Exiting...")
        exit(1)
    # usage demo
    # stroke_widths = [random.choice([1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5])] * len(lines)

    for i in stbi:
        for j in stbi[i]:
            print(f"=" * 90)
            print(f"{f'Style: {i}, Bias: {j}':^90}")
            print(f"=" * 90)
            stroke_width = random.choice(
                [1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5])
            lines_sp = arr_splitter(lines, linesPerPage)
            filenames = []
            for k, line_pg in enumerate(lines_sp):
                filenames.append(f'st{i}_bias{j}-pg{k}')
                print(f"\rPage {k}/{len(lines_sp)} done", end="")
                hand.write(
                    filename=f"img/dist/{filenames[-1]}.svg",
                    lines=line_pg,
                    biases=[j] * len(line_pg),
                    styles=[i] * len(line_pg),
                    stroke_widths=[
                        stroke_width + random.choice([-0.1, -0.05, 0, 0.05, 0.1]) for _ in range(len(lines))],
                    alignCenter=False
                )
                print(f"\rPage {k+1}/{len(lines_sp)} done", end="")
            print()
            pdfConverter(filenames)
