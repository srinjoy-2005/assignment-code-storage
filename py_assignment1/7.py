import os

def findfiles(directory_path):
    file_paths = []
    for root, dir, files in os.walk(directory_path):
        for file in files:
            if os.path.isfile(f'{root}\\{file}'):
                file_paths.append(f'{root}\\{file}')

    return file_paths
if __name__ == "__main__":
    file_paths = findfiles(r"D:\10501019\AdvancedOOPS")
    for file_path in file_paths:
        print(file_path)