#include <iostream>
#include <list>
using namespace std;

class Graph
{

	int c;  //connections aka vertices

	list <int> *adj;  //list for adjacent lists

public:

	Graph(int c)  //constructor for class
	{
		this -> c = c; adj = new list<int>[c];
	}

	~Graph()  //destructor for class
	{
		delete[] adj;
	}


	void addLine(int c, int w);  // adds lines between graph points

	void greedyColoring(); //constructor for greedy algorithm coloring
};


void Graph::addLine(int c, int w)
{

	adj[c].push_back(w);

	adj[w].push_back(c);

}

void Graph::greedyColoring()
{

	int color[c];

	color[0] = 0;  //starts points at 0 color

	for (int s = 1; s < c; s++)
		color[s] = -1;  //assigns null color to s


	bool accessable[c];
	for (int iu = 0; iu < c; iu++)
		accessable[iu] == false;  //iu means in use,  sees if adjacent vertices are assigned a color

	for (int s = 1; s < c; s++)  //assignes points as unavailable
	{

		list<int>::iterator i;

		for (i = adj[s].begin(); i != adj[s].end(); i++)
			if (color[*i] != -1)
				accessable[color[*i]] = true;

		int iu;  //finds first available color

		for (iu = 0; iu < c; iu++)
			if (accessable[iu] == false)
				break;

		color[s] = iu;  //assigns color as used

		for (i = adj[s].begin(); i != adj[s].end(); i++) // resets points for next ping
			if (color[*i] != -1)
				accessable[color[*i]] = false;

	}

	for (int s = 0; s < c; s++)
		cout << "point " << s << "has been colored " << color[s] << " Times." << endl;


}


int main()
{

	Graph r1(6);  //representation 1 for this graph
	r1.addLine(0, 1);
	r1.addLine(0, 4);
	r1.addLine(0, 5);
	r1.addLine(1, 3);
	r1.addLine(1, 4);
	r1.addLine(2, 3);
	r1.addLine(2, 4);
	r1.greedyColoring();

	return 0;

};