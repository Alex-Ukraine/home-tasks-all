def sort_names(input_file_path: str, output_file_path: str) -> None:
    with open(input_file_path) as file1:
        list_names = file1.readlines()
    list_names[-1]=list_names[-1].join([list_names[-1], '\n'])
    list_names.sort()
    with open(output_file_path, 'w') as file2:
        file2.writelines(list_names)