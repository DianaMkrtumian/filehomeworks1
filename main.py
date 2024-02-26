
def compile_files(path):
    files = {}
    for file_ in path:
        if file_.endswith(".txt"):
            files = file_
            with open('files', encoding='utf-8') as f:
                file_.files = f.readlines()
                files[len(file_.files)] = (file_, ' '.join(file_.files))

    files = dict(sorted(files.items()))

    with open('result_files.txt', "w", encoding='utf-8') as new_file:
        for key, value in files.items():
            new_file.write(f"{value[0]}\n")
            new_file.write(f"{key}\n")
            new_file.write(f"{value[1]}\n\n")
    print(new_file)
    