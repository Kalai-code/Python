import os,sys, glob
import zipfile
import shutil

file_path_processed = "Bills_Copy\\"

def main(output_filename):
  l_json_files_list = glob.glob(file_path_processed + '*.json')
  zip_file = zipfile.ZipFile(output_filename, 'w',zipfile.ZIP_DEFLATED)
  with zip_file:
    for file in l_json_files_list:
      zip_file.write(filename=file, arcname=os.path.basename(file))
      os.remove(file)

main("Bills_Copy\\my_python_files.zip")
