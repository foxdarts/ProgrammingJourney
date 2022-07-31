#include <iostream> 
using namespace std;

class Rectangle //class creation
{

	int length;
	int width;


public:

	Rectangle() //class constructor setting default values to 0
	{

		length = 0;

		width = 0;
	}

	Rectangle(int l, int w)
	{

		length = l;

		width = w;
	}

	Rectangle operator+(Rectangle rectangle)  //overloading addition operator
	{
		Rectangle f;

		f.length = length + rectangle.length;

		f.width = width + rectangle.width;

		return f;

	}

	void PrintRectangle()
	{

		cout << endl << "\tLength = " << length << endl;

		cout << endl << "\twidth = " << width << endl;

	}

};

int main()
{

	Rectangle r1(2, 5), r2(5, 20), r3;

	cout << "\n Display Rectangles" << endl;

	cout << "Rectangle 1 : " << endl;

	r1.PrintRectangle();

	cout << "Rectangle 2 : " << endl;

	r2.PrintRectangle();

	r3 = r1 + r2;

	cout << "combined rectangle : " << endl;

	r3.PrintRectangle();


	return 0;

};