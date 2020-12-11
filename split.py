
# split.py
#
# Demonstrates the use of the string 'split' method
# and parallel lists.

# CSC 110
# W'12


def main():
    # Introduction
    print('Enter a series of student records.')
    print('Each record should consist of the student name')
    print('followed by a list of quiz scores separated by spaces.')
    print('For this demonstration, the student name should be one word.')
    print('Press <Enter> with no input after the last record.\n')


    # Get user input
    student_names = []  # initialize list of student names
    average_scores = [] # initialize list of average scores
    overall_highest_score = 0  # assumes no score can be less than zero
    user_input = input('Enter the first record: ')
    while user_input != '':
        record = user_input.split()
        student_names.append(record[0])
        sum = 0
        for i in range(1, len(record)):  # why start with 1?
            score = float(record[i])
            sum += score
            if score > overall_highest_score:
                overall_highest_score = score
        if len(record) > 1:
            average_scores.append(sum/(len(record)-1))  # why -1?
        else:
            average_scores.append(0)
        user_input = input('Enter the next record (empty if finished): ')
        

    # Show report
    print()
    for i in range(len(student_names)):
        print('The average score for ' + student_names[i] + ' is ' \
              + format(average_scores[i], '.1f') + '.')
    print('The highest grade earned by any student was ' \
          + str(overall_highest_score))

main()

# Here are two test cases:

##Enter a series of student records.
##Each record should consist of the student name
##followed by a list of quiz scores separated by spaces.
##For this demonstration, the student name should be one word.
##Press <Enter> with no input after the last record.
##
##Enter the first record: sally 82 93 89
##Enter the next record (empty if finished): eric 79 83 90
##Enter the next record (empty if finished): minh 92 87 84
##Enter the next record (empty if finished): 
##
##The average score for sally is 88.0.
##The average score for eric is 84.0.
##The average score for minh is 87.7.
##The highest grade earned by any student was 93.0

# In this second test case, notice that each student may
# have a different number of test:

##Enter a series of student records.
##Each record should consist of the student name
##followed by a list of quiz scores separated by spaces.
##For this demonstration, the student name should be one word.
##Press <Enter> with no input after the last record.
##
##Enter the first record: victor 88 84 89
##Enter the next record (empty if finished): mary 83 79 88 92 95
##Enter the next record (empty if finished): jung 92 83
##Enter the next record (empty if finished): peter 81 83 84
##Enter the next record (empty if finished): 
##
##The average score for victor is 87.0.
##The average score for mary is 87.4.
##The average score for jung is 87.5.
##The average score for peter is 82.7.
##The highest grade earned by any student was 95.0
