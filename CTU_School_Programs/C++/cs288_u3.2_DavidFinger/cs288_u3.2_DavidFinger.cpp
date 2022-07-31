#include <iostream>
#include <string>
using namespace std;


class Vehicle //base class vehicle
{
public:

	string type;
	int doors;
	int occupancy;
	int milage;

	Vehicle() {};

	Vehicle(string t, int d, int o, int m)
	{
		type = t;
		doors = d;
		occupancy = o;
		milage = m;
	};


	string gettype()
	{
		return type;
	};

	int getdoors()
	{
		return doors;
	};

	int getoccupancy()
	{
		return occupancy;
	};

	int getmilage()
	{
		return milage;
	};

	void settype(string t)
	{
		type = t;
	};

	void setdoors(int d)
	{
		doors = d;
	};

	void setoccupancy(int o) 
	{
		occupancy = o;
	};

	void setmilage(int m)
	{
		milage = m;
	};

	virtual void features()
	{
		cout << "vehicle features : \n";

		cout << "vehicle is a " << type << ".  it has " << doors << " doors and can carry " << occupancy << " people.  it gets " << milage << "mpg on average.";
	};


};

class sedan : public Vehicle //sedan instance
{
public:

	

	sedan()
	{
		type = "sedan";
		doors = 4;
		occupancy = 5;
		milage = 30;

	};

};

class minivan : public Vehicle //minivan instance
{
public:

	

	minivan()
	{
		type = "minivan";
		doors = 4;
		occupancy = 7;
		milage = 22;

	};

	
};

class coupe : public Vehicle //coupe instance
{
public:

	

	coupe()
	{
		type = "coupe";
		doors = 2;
		occupancy = 2;
		milage = 24;

	};

	
};

class crossover : public Vehicle //crossover instance
{
public:

	

	crossover()
	{
		type = "crossover";
		doors = 4;
		occupancy = 7;
		milage = 28;

	};


};

class convertible : public Vehicle //convertable instance
{
public:

	

	convertible()
	{
		type = "convertible";
		doors = 2;
		occupancy = 5;
		milage = 30;

	};

	
};

int main() // main
{
	string i;
	Vehicle i1;
	sedan i2;
	minivan i3;
	coupe i4;
	crossover i5;
	convertible i6;
	
	cout << "what type of car would you like specs for? (sedan, minivan, crossover, coupe, or convertible): " << endl;
	
	cin >> i1.type;
	
	if (i1.type == "sedan") // sets sedan values
	{
		
		sedan i2;
		
		Vehicle &i1 = i2;
		
		i1.features();

	}
	
	else if (i1.type == "minivan") //sets minivan values
	{
		
		minivan i3;

		Vehicle &i1 = i3;
		
		i1.features();
	}
	
	else if (i1.type == "coupe") //sets coupe values
	{
		
		coupe i4;

		Vehicle &i1 = i4;
		
		i1.features();
	}
	
	else if (i1.type == "crossover") //cets crossover values
	{
		crossover i5;

		Vehicle &i1 = i5;
		
		i1.features();
	}

	else if (i1.type == "convertible") //sets convertible values
	{
		
		convertible i6;

		Vehicle &i1 = i6;
		
		i1.features();
	}
	
	else  //sets improper entry responce
	{
		cout << "Invalid car type";
	};

}; 