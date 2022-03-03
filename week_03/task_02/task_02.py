class Task02:

    def __init__(self, path_for_input_file, path_for_output_file):
        self.path_for_input_file = path_for_input_file
        self.path_for_output_file = path_for_output_file


    def calculate(self, action, number1, number2):
        return str(eval(f'{number1} {action} {number2}'))


    def create_results_list(self, path_to_file):
        results_list = list()
        with open(path_to_file, "r") as input_file:
            for line in input_file:
                action, number1, number2 = line.split()
                results_list.append(self.calculate(action, number1, number2))
        return results_list


    def write_results_to_file(self, list, path_to_file):
        with open(path_to_file, "w") as output_file:
            output_file.write(",".join(list))

    def read_input_file_and_write_calculation_results_to_file(self, input_file, output_file):
        results_list = self.create_results_list(input_file)
        self.write_results_to_file(results_list, output_file)

# PATH_INP = "./test_input_file_1.txt"
# PATH_OUT = "./test_output_file_1.txt"

PATH_INP = "./input_file.txt"
PATH_OUT = "./output_file.txt"

task02 = Task02(PATH_INP, PATH_OUT)
task02.read_input_file_and_write_calculation_results_to_file(PATH_INP, PATH_OUT)