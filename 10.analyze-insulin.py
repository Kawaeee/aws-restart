# https://www.ncbi.nlm.nih.gov/protein/AAA59172.1

# In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as lsinsulin-seq-clean.txt.
# In lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.

# In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as binsulin-seq-clean.txt.
# In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters.

# In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as cinsulin-seq-clean.txt.
# In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.

# In the AWS Cloud9 IDE, on the navigation pane, choose File > New File and save the file as ainsulin-seq-clean.txt.
# In ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.

import re

file_path = "10.preproinsulin-seq.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

clean_lines = []

for line in lines:
    line = re.sub(r"ORIGIN|\/\/|\d+", "",line).strip()
    if line:
        clean_lines.append(line)

clean_preproinsulin = " ".join(clean_lines).replace(" ", "").strip()
print(clean_preproinsulin)

lsinsulin = clean_preproinsulin[0:24]  # Amino acids 1-24
binsulin = clean_preproinsulin[24:54]  # Amino acids 25-54
cinsulin = clean_preproinsulin[54:89]  # Amino acids 55-89
ainsulin = clean_preproinsulin[89:110] # Amino acids 90-110

# Verify the lengths and print the sequences
print("L segment (lsinsulin):")
print(lsinsulin)
print("Length:", len(lsinsulin))

print("B segment (binsulin):")
print(binsulin)
print("Length:", len(binsulin))

print("C segment (cinsulin):")
print(cinsulin)
print("Length:", len(cinsulin))

print("A segment (ainsulin):")
print(ainsulin)
print("Length:", len(ainsulin))
