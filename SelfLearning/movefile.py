import os, shutil

file_path_read = "C:\\Kalai\\Python\\Projects\\Billing\\Bills\\20220413204026.json"

file_path_processed = "C:\\Kalai\\Python\\Projects\\Billing\\Processed_bills\\20220413204026.json"

shutil.move(file_path_read,file_path_processed)
