def find_val(a_list, val_to_find):
    '''
    :return: the index of the first occurence of val_to_find in a_list, or -1 if not found
    '''
    for i in range(len(a_list)):
        if a_list[i] == val_to_find:
            return i
    return -1

def find_val_test():
    print("------find_val_test-------")
    test_list = [2, 5, 4, 6, 1]
    for i in range(len(test_list)):
        result = find_val(test_list, test_list[i])
        print("should be", i, ":", result)
    # How does the test above work?
    
    result = find_val(test_list, 7)
    print("should be -1:", result)
    result = find_val([4], 4)
    print("should be 0:", result)
    result = find_val([], 4)
    print("should be -1:", result)
    result = find_val([2, 3, 8, 6, 3, 6, 5, 4, 6], 3)
    print("should be 1:", result)
    result = find_val([2, 3, 8, 6, 3, 6, 5, 4, 6], 6)
    print("should be 3:", result)

def count_val(a_list, val_to_count):
    '''
    :return: the number of occurences of val_to_count in a_list
    '''
    counter = 0
    for i in a_list:
        if i == val_to_count:
            counter += 1
    return counter
        

def count_val_test():
    print("------count_val_test-------")
    result = count_val([2, 3, 8, 6, 3, 6, 5, 3], 8)
    print("should be 1:", result)
    result = count_val([2, 3, 8, 6, 3, 6, 5, 3], 10)
    print("should be 0:", result)
    result = count_val([2, 3, 8, 6, 3, 6, 5, 3], 3)
    print("should be 3:", result)
    result = count_val([2, 3, 8, 6, 3, 6, 5, 4], 6)
    print("should be 2:", result)
    result = count_val([2, 2, 2], 2)
    print("should be 3:", result)
    result = count_val([4], 4)
    print("should be 1:", result)
    result = count_val([], 4)
    print("should be 0:", result)

def max_val(a_list):
    '''
    :return: the maximum value in a_list, or None if a_list is empty
    '''
    value = 0
    
    if len(a_list) == 0:
        return "None"
    
    for i in a_list:
        if i > value:
            value = i
    return value

def max_val_test():
    print("------max_val_test-------")
    result = max_val([2, 3, 8, 6, 3, 6, 5, 4, 6])
    print("should be 8:", result)
    result = max_val([10, 3, 8, 6, 3, 6, 5, 4, 6])
    print("should be 10:", result)
    result = max_val([10, 3, 8, 6, 3, 6, 5, 4, 6, 1000])
    print("should be 1000:", result)
    result = max_val([-5, -3, -8, -6, -3])
    print("should be -3:", result)
    result = max_val([2])
    print("should be 2:", result)
    result = max_val([])
    print("should be None:", result)

def max_index(a_list):
    '''
    :return: the index of the first occurence of the maximum value in a_list, or None if a_list is empty
    '''
    
    if len(a_list) == 0:
        return "None"

    val = a_list[0]
    index = 0
    
    for i in range(len(a_list)):
        if a_list[i] > val:
            val = a_list[i]
            index = i
    return index
    


def max_index_test():
    print("------max_index_test-------")
    result = max_index([2, 3, 8, 6, 3, 6, 5, 4, 6])
    print("should be 2:", result)
    result = max_index([10, 3, 8, 6, 3, 6, 5, 4, 6])
    print("should be 0:", result)
    result = max_index([10, 3, 8, 6, 3, 6, 5, 4, 6, 1000])
    print("should be 9:", result)
    result = max_index([-5, -3, -8, -6, -3])
    print("should be 1:", result)
    result = max_index([2])
    print("should be 0:", result)
    result = max_index([])
    print("should be None:", result)

def all_values_below(a_list, threshold):
    '''
    :return: a new list of all the values from a_list that are below threshold
    '''
    below_threshold = []
    for i in a_list:
        if i < threshold:
            below_threshold.append(i)
    return below_threshold
        

def all_values_below_test():
    print("------all_values_below_test-------")
    result = all_values_below([2, 3, 8, 6, 3, 6, 5, 4, 6], 5)
    print("should be [2, 3, 3, 4]:", result)
    result = all_values_below([10, 3, 8, 6, 3, 6, 5, 4, 6], 11)
    print("should be [10, 3, 8, 6, 3, 6, 5, 4, 6]:", result)
    result = all_values_below([2, 3, 8, 6, 3, 6, 5, 4, 6], 0)
    print("should be []:", result)
    result = all_values_below([10, 3, 8, 6, 3, 6, 5, 4, 6, -1000], 3)
    print("should be [-1000]:", result)
    result = all_values_below([-5, -3, -8, -6, -3], -5)
    print("should be [-8, -6]:", result)
    result = all_values_below([2], 5)
    print("should be [2]:", result)
    result = all_values_below([], 5)
    print("should be []:", result)

def ask_user_for_grades(number_of_grades):
    '''
    asks the user to enter some specific number of grades, keeps them all in a list
    :return:   a list with number_of_grades numbers in it
    '''
    
    student_names = []
    student_grades = []
    for i in range(number_of_grades):
        name_input = input("Enter student name :: ")
        student_names.append(name_input)
        grade_input = int(input("Enter score for student (0-10) :: "))
        student_grades.append(grade_input)
        
    return student_names, student_grades

def add_to_each_value(a_list, amount_to_add):
    '''
    :side effect: all values in a_list are increased by amount_to_add
    '''
    for i in range(len(a_list)):
        a_list[i] += amount_to_add

def add_to_each_value_test():
    print("------add_to_each_value_test-------")
    
    # What is different about these tests?
    list_to_change = [2, 3, 8, 6, 3, 6, 5, 4, 6]
    add_to_each_value(list_to_change, 2)
    print("should be [4, 5, 10, 8, 5, 8, 7, 6, 8]:", list_to_change)
    
    list_to_change = [-5, -3, -8, 16, 4]
    add_to_each_value(list_to_change, 5)
    print("should be [0, 2, -3, 21, 9]:", list_to_change)

    list_to_change = []
    add_to_each_value(list_to_change, 10)
    print("should be []:", list_to_change)
 

def test():
    find_val_test()
    count_val_test()
    max_val_test()
    max_index_test()
    all_values_below_test()
    add_to_each_value_test()
    
def find_failing_names(names, grades, fgrades):
    
    student_names = names.copy()
    student_grades = grades.copy()
    fail_grades = fgrades.copy()
    fail_names = []
    #num_fail_grades = len(fail_grades)
    while(len(fail_grades) >= 1):
        fail_names.append(student_names[find_val(student_grades, fail_grades[0])])
        student_grades.remove(fail_grades[0])
        student_names.remove(fail_names[-1])
        fail_grades.pop(0)
        
    return fail_names

def find_max_grade_names(grades, names, max_grade):
    student_grades = grades.copy()
    student_names = names.copy()
    num_max_grades = count_val(student_grades, max_grade)
    top_student_names = []
    
    for i in range(num_max_grades):
        top_student_names.append(student_names[find_val(student_grades, max_grade)])
        student_grades.remove(max_grade)
        student_names.remove(top_student_names[i])
        
    return top_student_names

def main():
    #test()
    num_grades = int(input("Enter number of grades to process :: "))
    
    student_names, student_grades = ask_user_for_grades(num_grades)
    
    max_grade = max_val(student_grades)
    max_students = find_max_grade_names(student_grades, student_names, max_grade)
    fail_names = find_failing_names(student_names, student_grades, all_values_below(student_grades, 6))
    
    print("\nThe maximum grade was ", max_grade, ", earned by ", ", ".join(max_students), ". The students who failed were ", ", ".join(fail_names), sep="")
    
    grade_bump_check = input("Would you like to increase grades? y/n :: ")
    
    if(grade_bump_check == "y"):
        grade_increase = 10 - max_grade
        add_to_each_value(student_grades, grade_increase)
        
        max_grade = max_val(student_grades)
        max_students = find_max_grade_names(student_grades, student_names, max_grade)
        fail_names = find_failing_names(student_names, student_grades, all_values_below(student_grades, 6))
        
        print("\nThe maximum grade was ", max_grade, ", earned by ", ", ".join(max_students), ". The students who failed were ", ", ".join(fail_names), sep="")
        
        print("\nThe new grades are:")
        for i in range(len(student_names)):
            print(student_names[i], student_grades[i])
              
main()
