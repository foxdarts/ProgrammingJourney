#include <bits/stdc++.h>
#include <algorithm>
#include <Bits.h>
#include <iostream>

using namespace std;

#define M 4

int travelingsalesmanproblem(int graph[][M], int j)
{

	vector <int> vertex;

	for (int d = 0; d < M; d++)
		if (d != j)
			vertex.push_back(d);

	int min_path = INT_MAX;
	do {

		int current_pathweight = 0;

		int c = j;

		for (int d = 0; d < vertex.size(); d++)
		{

			current_pathweight += graph[c][vertex[d]];

			c = vertex[d];

		}

		current_pathweight += graph[c][j];

		min_path = min(min_path, current_pathweight);


	} while (next_permutation(vertex.begin(), vertex.end()));

	return min_path;

}

int main()
{

	int graph[][M] = { {0, 10, 15, 20},
						{10, 0, 35, 25},
						{15, 35, 0, 30},
						{20, 25, 30, 0} };

	int j = 0;
	cout << travelingsalesmanproblem(graph, j) << endl;

	return 0;

}


