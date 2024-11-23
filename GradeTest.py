# *****************************************************************************
# Program: GradeTest.py
# Language: Python 3.10.6
#
# Description: This program will read a text file grades and display how many questions where
# right and wrong and if you passed.
#
# College: Husson University
# Course: IT 262 - Spring 2023
# Author: Michael Desjardins
#
# Change Log:
# Date          Description of Change
# -----------------------------------
# 02-6-2023    intitial Draft
# 02-7-2023    finished
# *****************************************************************************

correctAnswers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

# Open external text file
studentScoresFile = open('StudentResponses.txt', 'r')

# Process contents of the file
studentScoreRecord = studentScoresFile.readline()
while studentScoreRecord != '':
    studentScoreRecord = studentScoreRecord.rstrip('\n')
    studentScoreList = studentScoreRecord.split(',')
    totalCorrect = 0
    totalIncorrect = 0
    incorrectAnswers = []
    for i in range(len(correctAnswers)):
        if studentScoreList[i+1] == correctAnswers[i]:
            totalCorrect += 1
        else:
            totalIncorrect += 1
            incorrectAnswers.append(i+1)

    print('Student Name: ', studentScoreList[0])
    print("\tTotal correct: " + str(totalCorrect))
    print("\tTotal incorrect: " + str(totalIncorrect))

    if totalIncorrect >= 0:
        print("\tThe following questions where answered incorrectly:", incorrectAnswers)
    if totalCorrect >= 15:
        print("\tResult of exam = PASS\n")
    else:
        print("\tResult of exam = FAIL\n")
    studentScoreRecord = studentScoresFile.readline()

# Close external file
studentScoresFile.close()
