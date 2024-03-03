
#include <stdio.h>

int main() {
    printf("|------------------------------------------------|\n");
    printf("|                                                |\n");
    printf("|              WELCOME TO THE GK QUIZ            |\n");
    printf("|                                                |\n");
    printf("|------------------------------------------------|\n");
    
    printf("HEY THERE !!!!!\n\n\n");
    printf("THINGS TO REMEMBER......\n\n\n");
    printf("THERE ARE 10  QUESTIONS RELATED TO YEAR 2023..\n");
    printf("THERE WIL BE 4 OPTIONS ALRIGHT (A/B/C/D)..\n");
    printf("THERE CANBE ONLY A SINGLE INPUT FOR A SOECIFIC QUESTION\n");
    printf("-----------------------------------------------------\n");
    printf("ALRIGHTY !!! LEST GETS THIS STARTED ......\n");

    int total_credits = 0;

    //SO I MADE USE OF SIMPLE STRINGS WITH ARRAYS WITHOUT SUBSCRIPT
    char question1[] = "1. What is the capital of France?";
    char question2[] = "2. Which planet is known as the Red Planet?";
    char question3[] = "3. Who wrote the play 'Romeo and Juliet'?";
    char question4[] = "4. Which gas do plants absorb from the atmosphere?";
    char question5[] = "5. What is the largest mammal in the world?";
    char question6[] = "6. Who is known as the 'Father of Modern Physics'?";
    char question7[] = "7. Which country is famous for the Eiffel Tower?";
    char question8[] = "8. What is the chemical symbol for gold?";
    char question9[] = "9. Which gas is used for filling balloons that float in the air?";
    char question10[] = "10. What is the smallest prime number?";

    // HERE I STORED THE ANSWES AS STRING
    char answer1[] = "B. Paris";
    char answer2[] = "A. Mars";
    char answer3[] = "William Shakespeare";
    char answer4[] = "Carbon dioxide (CO2)";
    char answer5[] = "Blue whale";
    char answer6[] = "Albert Einstein";
    char answer7[] = "France";
    char answer8[] = "Au";
    char answer9[] = "Helium (He)";
    char answer10[] = "2";

    int correct_answers = 0;

    // QUESTION 1
    printf("%s\n", question1);
    printf("Options:\n");
    printf("A. London\n");
    printf("B. Paris\n");
    printf("C. Rome\n");
    printf("D. Berlin\n");

    char user_answer1;
    printf("Enter your answer (A/B/C/D): ");
    scanf(" %c", &user_answer1);

    if (user_answer1 == 'B' || user_answer1 == 'b') {
        printf("Correct!\n");
        correct_answers++;
    } else {
        printf("Wrong!\n");
    }

    // QUESTION 2
    printf("%s\n", question2);
    printf("Options:\n");
    printf("A. Mars\n");
    printf("B. Venus\n");
    printf("C. Jupiter\n");
    printf("D. Saturn\n");

    char user_answer2;
    printf("Enter your answer (A/B/C/D): ");
    scanf(" %c", &user_answer2);

    if (user_answer2 == 'A' || user_answer2 == 'a') {
        printf("Correct!\n");
        correct_answers++;
    } else {
        printf("Wrong!\n");
    }

    // QUESTION 3
    printf("%s\n", question3);
    printf("Options:\n");
    printf("A. Charles Dickens\n");
    printf("B. William Shakespeare\n");
    printf("C. Jane Austen\n");
    printf("D. Mark Twain\n");

    char user_answer3;
    printf("Enter your answer (A/B/C/D): ");
    scanf(" %c", &user_answer3);

    if (user_answer3 == 'B' || user_answer3 == 'b') {
        printf("Correct!\n");
        correct_answers++;
    } else {
        printf("Wrong!\n");
    }

    // QUESTION 4
    printf("%s\n", question4);
    printf("Options:\n");
    printf("A. Oxygen (O2)\n");
    printf("B. Nitrogen (N2)\n");
    printf("C. Carbon dioxide (CO2)\n");
    printf("D. Hydrogen (H2)\n");

    char user_answer4;
    printf("Enter your answer (A/B/C/D): ");
    scanf(" %c", &user_answer4);

    if (user_answer4 == 'C' || user_answer4 == 'c') {
        printf("Correct!\n");
        correct_answers++;
    } else {
        printf("Wrong!\n");
    }

    // QUESTION 5
    printf("%s\n", question5);
    printf("Options:\n");
    printf("A. Elephant\n");
    printf("B. Giraffe\n");
    printf("C. Blue whale\n");
    printf("D. Lion\n");

    char user_answer5;
    printf("Enter your answer (A/B/C/D): ");
    scanf(" %c", &user_answer5);

    if (user_answer5 == 'C' || user_answer5 == 'c') {
        printf("Correct!\n");
        correct_answers++;
    } else {
        printf("Wrong!\n");
    }

    // QUESTION 6
    printf("%s\n", question6);
    printf("Options:\n");
    printf("A. Isaac Newton\n");
    printf("B. Galileo Galilei\n");
    printf("C. Albert Einstein\n");
    printf("D. Thomas Edison\n");

    char user_answer6;
    printf("Enter your answer (A/B/C/D): ");
    scanf(" %c", &user_answer6);

    if (user_answer6 == 'C' || user_answer6 == 'c') {
        printf("Correct!\n");
        correct_answers++;
    } else {
        printf("Wrong!\n");
    }

    // QUESTION 7
    printf("%s\n", question7);
    printf("Options:\n");
    printf("A. Italy\n");
    printf("B. Germany\n");
    printf("C. Spain\n");
    printf("D. France\n");

    char user_answer7;
    printf("Enter your answer (A/B/C/D): ");
    scanf(" %c", &user_answer7);

    if (user_answer7 == 'D' || user_answer7 == 'd') {
        printf("Correct!\n");
        correct_answers++;
    } else {
        printf("Wrong!\n");
    }

    // QUESTION 8
    printf("%s\n", question8);
    printf("Options:\n");
    printf("A. Ag\n");
    printf("B. Au\n");
    printf("C. Hg\n");
    printf("D. Pt\n");

    char user_answer8;
    printf("Enter your answer (A/B/C/D): ");
    scanf(" %c", &user_answer8);

    if (user_answer8 == 'B' || user_answer8 == 'b') {
        printf("Correct!\n");
        correct_answers++;
    } else {
        printf("Wrong!\n");
    }



    printf("\nYou answered %d questions correctly out of 10.\n", correct_answers);

    if (correct_answers == 10) {
        printf("Congratulations! You got all the questions correct!\n");
    }

    return 0;
}