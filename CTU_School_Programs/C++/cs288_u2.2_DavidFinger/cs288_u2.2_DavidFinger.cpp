// cs288_u2.2_DavidFinger.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;


int main()
{
    
    string ui1;
    string ui2;

    cout << "type string input: ";

    getline (cin, ui1);

    cout << "type string input again: ";

    getline (cin, ui2);

    cout << "you typed: " << ui1 << "\nthen typed: " << ui2 << '\n';

    if (ui1.compare(ui2) != 0)
        cout << ui1 << " doesnt match " << ui2 << '\n';

    if (ui1.compare(ui2) == 0)
        cout << "Inputs matched" << '\n';

    string combo = ui1 + " " + ui2;
   
    cout << combo << " is your combined input." << '\n';

    cout << "the length of input 1 is: " << ui1.length() << '\n';
   
    cout << "the length of input 2 is: " << ui2.length() << '\n';
   
    cout << "the length of total inputs, including spaces, is: " << combo.length() << '\n';

    int len = combo.length();
    
    int n = len - 1;
    
    for (int i = 0; i < len / 2; i++)
    {
        swap(combo[i], combo[n]);

        n = n - 1;
    }

    cout << "backwards: " << combo << '\n';
   

}

