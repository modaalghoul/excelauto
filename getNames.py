

import os
import pandas

def getNamesFromExcelFiles():
    filename = __file__.split("\\")[-1]
    current_dir = __file__[:-(len(filename)+1)]


    excel_files = []
    for item in os.listdir(current_dir):
        fullpath = os.path.join(current_dir, item)
        if item.endswith('.xlsx') and os.path.isfile(fullpath):
            excel_files.append(item)

    names = []
    for filename in excel_files:
        names.extend(pandas.read_excel(filename).Names.tolist())

    return names
