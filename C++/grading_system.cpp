//Ceate a program that will take a student's score and grade them
//Based on the above grading system

//Variable for the score
//A, B, C, D, E, F
//A = 90+
//B = 80+
//C = 70+
//D = 60+
//E = 50+
//F = Anything below 49

#include<iostream>

int main(){
    //Variables
    float score;

    std::cout << "Enter your score: " << std::endl;
    std::cin >> score;

    // Exceptions Before Running
    if (score < 0 || score > 100){
        std::cout << "Invalid score. Please enter a value between 0 and 100." << std::endl;
    }else if (score < 50){
        std::cout << "Grade F";

    }else if (score < 60){
        std::cout << "Grade E";

    }else if (score < 70){
        std::cout << "Grade D";

    }else if (score < 80){
        std::cout << "Grade C";

    }else if (score < 90){
        std::cout << "Grade B";

    }else
    {
        std::cout << "Grade A";
    }

    return 0;
}