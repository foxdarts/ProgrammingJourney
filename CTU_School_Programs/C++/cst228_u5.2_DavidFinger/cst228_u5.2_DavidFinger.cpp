#include <iostream>
#include <algorithm>

using namespace std;

int b_search(int a[], int l, int r, int s)
{

	if (r >= l)
	{

		int mid = l + (r - l) / 2;

		if (a[mid] == s)
			return mid;

		if (a[mid] > s)
			return b_search(a, l, mid - 1, s);

		return b_search(a, mid + 1, r, s);
	}
	
	return -1;

}

int main()
{

	int n = 20, s;

	int a[20];

	cout << "please enter 20 numbers: ";

	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	sort(a, a + n);

	cout << "what number do you want to look for? ";
	
	cin >> s;

	int index = b_search(a, 0, n - 1, s);

	if (index == -1)
	{

		cout << "number not in array";

	}
		else
		{

		cout << "\nnumber found at place # " << index;

		}

	return 0;
}