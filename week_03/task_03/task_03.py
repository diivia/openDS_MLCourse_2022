class Task03:
    def __init__(self, path_for_text_input_file, path_for_numbers_input_file, path_for_output_file):
        self.path_for_text_input_file = path_for_text_input_file
        self.path_for_numbers_input_file = path_for_numbers_input_file
        self.path_for_output_file = path_for_output_file

    def read_from_file_to_list(self, path_to_file):
        lines_list = list()
        with open(path_to_file, "r") as input_file:
            for line in input_file:
                lines_list.append(line)
        return lines_list

    def find_substring(self, line, number1, number2):
        return str(line[int(number1): int(number2) + 1])

    def create_list_of_substrings(self, input_list, substring_indexes_list):
        results_list = list()
        for i in range(len(input_list)):
            line = input_list[i]
            first_index, second_index = substring_indexes_list[i].split()
            results_list.append(self.find_substring(line, int(first_index), int(second_index)))
        return results_list

    def write_results_to_file(self, list, path_to_file):
        with open(path_to_file, "w") as output_file:
            output_file.write(" ".join(list))

    def read_input_file_and_write_calculation_results_to_file(self):
        text_list = self.read_from_file_to_list(self.path_for_text_input_file)
        numbers_list = self.read_from_file_to_list(self.path_for_numbers_input_file)
        results_list = self.create_list_of_substrings(text_list, numbers_list)
        self.write_results_to_file(results_list, self.path_for_output_file)


# PATH_INP_1 = "./test_import_file_2_1.txt"
# PATH_INP_2 = "./test_import_file_2_2.txt"
# PATH_OUT = "./test_output_file_my2.txt"

PATH_INP_1 = "./import_file_2_1.txt"
PATH_INP_2 = "./import_file_2_2.txt"
PATH_OUT = "./output_file_my3.txt"

task_03 = Task03(PATH_INP_1, PATH_INP_2, PATH_OUT)
task_03.read_input_file_and_write_calculation_results_to_file()