#include <iostream>
#include <Bits.h>
#include <list>
#include <deque>
#include <vector>
#include <cstdbool>
#include <algorithm>


//using namespace std::list;
using namespace std;

bool descending(int a, int b)
{

	return a > b;

}

int main()
{

	cout << "how many numbers will be sorted? ";
	
	int n, a;

	cin >> n; 

	vector <int> v;

	list <int> l;

	deque <int> d;

	cout << "enter numbers : ";

	for (int i = 0; i < n; i++)
	{

		cin >> a;

		v.push_back(a);

		l.push_back(a);

		d.push_back(a);

	}

	sort(v.rbegin(), v.rend());

	l.sort(descending);

	sort(d.begin(), d.end(), descending);

	cout << "numbers in a vector after descending sort: ";

	for (int i = 0; i < v.size(); i++)
	{
		cout << v[i] << endl;
	}
	cout << "numbers in a vector after descending sort: ";

	for (auto i = l.begin(); i != l.end(); i++)
		cout << *i << endl;

	cout << "numbers in a deque after decending sort: ";

	for (auto i = d.begin(); i != d.end(); i++)
		cout << *i << endl;



}