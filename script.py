import os
import subprocess

def print_ascii_art():
    art = """
  _____       ______ _ _                       
 |  __ \     |  ____| (_)                      
 | |__) |   _| |__  | |_ _ __  _ __   ___ _ __ 
 |  ___/ | | |  __| | | | '_ \| '_ \ / _ \ '__|
 | |   | |_| | |    | | | |_) | |_) |  __/ |   
 |_|    \__, |_|    |_|_| .__/| .__/ \___|_|   
         __/ |          | |   | |              
        |___/           |_|   |_|     - by @rudy
    """
    print(art)

def list_folders():
    folders = [f for f in os.listdir('.') if os.path.isdir(f) and not f.startswith('.')]
    for idx, folder in enumerate(folders, start=1):
        print(f"{idx}. {folder}")
    return folders

def list_python_files(folder):
    python_files = [f for f in os.listdir(folder) if f.endswith('.py')]
    for idx, file in enumerate(python_files, start=1):
        print(f"{idx}. {file}")
    return python_files

def run_python_file(folder, file):
    file_path = os.path.join(folder, file)
    subprocess.run(['python', file_path])

def main():
    print_ascii_art()
    folders = list_folders()
    if not folders:
        print("No folders found.")
        return


    folder_choice = int(input("Choose a tool: ")) - 1
    if folder_choice < 0 or folder_choice >= len(folders):
        print("Invalid choice.")
        return

    selected_folder = folders[folder_choice]
    python_files = list_python_files(selected_folder)
    if not python_files:
        print("No Python files found in the selected folder.")
        return

    file_choice = int(input("Choose a Python script number to run: ")) - 1
    if file_choice < 0 or file_choice >= len(python_files):
        print("Invalid choice.")
        return

    selected_file = python_files[file_choice]
    run_python_file(selected_folder, selected_file)

if __name__ == "__main__":
    main()