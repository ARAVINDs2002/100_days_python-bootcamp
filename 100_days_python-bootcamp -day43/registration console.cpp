#include <iostream>
#include <fstream>
using namespace std;
void login();
void registration();
void forgot_pass();

int main()
{
    int choice;

cout << "|--------------------------------------------|\n";
cout << "|         WELCOME TO LOGIN PAGE              |\n";
cout << "|--------------------------------------------|\n";
cout << "|                   MENU                     |\n";
cout << "|--------------------------------------------|\n";
cout << "|  -> For Login, press 1                     |\n";
cout << "|  -> For Registration, press 2              |\n";
cout << "|  -> Forgot Password?, press 3              |\n";
cout << "|  -> Exit, press 4                          |\n";
cout << "|--------------------------------------------|\n";

cout << "\nPLEASE ENTER YOUR CHOICE : ";
cin >> choice;
cout << "\n";

switch (choice)
{
case 1:
    login();
    break;
case 2:
    registration();
    break;
case 3:
    forgot_pass();
    break;
case 4:
    cout << "\n\t\t\tTHANK YOU FOR USING OUR SERVICE. SEE YOU AGAIN\n\n";
    break;
default:
    cout << "\n PLEASE CHOOSE A NUMBER FROM THE OPTIONS!!!!\n\n";
}

return 0;
}

void login()
{
int count = 0;
string username, password, id, pass;

cout << "YOU SELECTED LOGIN !!!\n\n";
cout << "PLEASE ENTER YOUR USERNAME AND PASSWORD BELOW...\n\n";
cout << "ENTER USER-NAME: ";
cin >> username;
cout << "\nENTER PASSWORD: ";
cin >> password;

ifstream input("records.txt");

while (input >> id >> pass)
{
if (id == username && pass == password)
{
  count = 1;
  break;
}
}

input.close();

if (count == 1)
{
 cout << username << "\n\t\t\t HURRAY!!!! LOGIN SUCCESSFUL!!!\n\n";
}
else
{
 cout << "\n\t\t\tNO MATCHES FOUND IN OUR DATABASE :(. MAKE SURE THE PASSWORD AND USERNAME ARE CORRECT\n\n";
}
}

void registration()
{
string rusername, rpassword;

cout << "YOU SELECTED REGISTRATION";
cout << "ENTER THE USER-NAME : ";
cin >> rusername;
cout << "ENTER THE PASSWORD : ";
cin >> rpassword;

ofstream f1("records.txt", ios::app);

f1 << rusername << ' ' << rpassword << endl;
f1.close();

cout << "\t\t\tREGISTERED SUCCESSFULLY!!!!\n\n";
}

void forgot_pass()
{
int option;
  
cout << "YOU SELECTED FORGOT PASSWORD.\n";
  
cout << "PRESS 1 TO SEARCH FOR YOUR PASSWORD BY USERNAME\n";
  
cout << "PRESS 2 TO GO BACK TO MENU\n";
  
cout << "\tENTER YOUR CHOICE: ";
  
cin >> option;
  
switch (option)
{
    case 1:
    {
        int count = 0;
        string suserid, sid, spass;
        cout << "\n\tENTER THE USERNAME YOU USED LAST: ";
        cin >> suserid;
        ifstream f2("records.txt");
        while (f2 >> sid >> spass)
        {
            if (sid == suserid)
            {
                count = 1;
            }
        }
        f2.close();
        if (count == 1)
        {
            cout << "\nYOUR ACCOUNT IS FOUND :)\n";
            cout << "YOUR PASSWORD IS: " << spass << "\n";
            cout << "\n";
            main();
        }
        else
        {
            cout << "\n\tSORRY, ACCOUNT NOT FOUND   :(\n";
            main();
        }
        break;
    }
    case 2:
    {
        main();
        break;
    }
    default:
        cout << "\tWRONG CHOICE! PLEASE TRY AGAIN";
        forgot_pass();
}
}

//the above sourcecode can be copied and pasted in a compiler to get the required output and to understand the working

