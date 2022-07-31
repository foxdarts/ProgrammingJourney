// cst228_1.2_davidfinger.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

void printFibNumb(int n)
{
    int num1 = 0, num2 = 1, i;

    if (n < 1)
        return;

    for (i = 1; i <= n; i++)
    {
        std::cout << num2 << " ";
        
        int next = num1 + num2;

        num1 = num2;

        num2 = next;
    }
}





int main()
{
    printFibNumb(20);
    return 0;
}

