import json


def count_lines_in_ipynb(filename):
    with open(filename, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    total_lines = 0
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            total_lines += sum(1 for line in cell["source"] if line.strip() != "")

    return total_lines


filename = "/home/voy/space/cud/thes/as2.ipynb"
print(count_lines_in_ipynb(filename))
