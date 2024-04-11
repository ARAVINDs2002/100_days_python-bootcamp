#include<iostream>
using namespace std;

int total_money = 1000;


void deposit(int &total_deposition) {
    int deposition;
    cout << "How much do you want to deposit now? ";
    cin >> deposition;
    total_deposition += deposition;
    cout << "Deposited successfully. Your new balance is: " << total_deposition << endl;
}


void withdraw(int &total_deposition) {
    int withdrawal;
    cout << "How much do you want to withdraw? ";
    cin >> withdrawal;
    if (withdrawal <= total_deposition) {
        total_deposition -= withdrawal;
        cout << "Withdrawn successfully. Your new balance is: " << total_deposition << endl;
    } else {
        cout << "Insufficient funds. Your current balance is: " << total_deposition << endl;
    }
}


void balance(int total_deposition) {
    cout << "Your current balance is: " << total_deposition << endl;
}

int main() {
    cout << "**********************************************\n";
    cout << "               Banking Software               \n";
    cout << "**********************************************\n";

    int choice;
    do {
        cout << "1. Deposit money\n";
        cout << "2. Withdraw money\n";
        cout << "3. Show balance\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                deposit(total_money);
                break;
            case 2:
                withdraw(total_money);
                break;
            case 3:
                balance(total_money);
                break;
            case 4:
                cout << "Exiting the banking system. Thank you!\n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 4);

    return 0;
}
