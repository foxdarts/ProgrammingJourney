// cs288_U2.1_DavidFinger.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;


class vertebrates; //sets class
{
public:
    int Bonyskeleton;
    int Brain;

};

int main()
{
    vertebrates creature;

    cout << "Does the creature have a bony skeleton? 0 = no, 1 = yes \n"; //asks for input of skeleton
    cin >> creature.Bonyskeleton;
    cout << "Does the creature have a brain? 0 = no, 1 = yes \n"; //asks for input of brain
    cin >> creature.Brain;



    if ((Bonyskeleton + Brain) = 2)
        cout << "creature is a vertibrate" << '\n';
}

