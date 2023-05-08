import java.io.*;
import java.util.*;
import java.util.LinkedList;

class buildGraph{

   public LinkedList<Integer> adj[]; //provides list for points

   //Constructor
    buildGraph(int c)
    {
        adj = new LinkedList[c];
        for (int i=0; i<c; ++i)
            adj[i] = new LinkedList();
    }

   
   void addEdge(int p, int s){ //adds paths between nodes
       adj[p].add(p);
       adj[s].add(s);
   }

   void colorGraph(int c){
       int ans[] = new int[c];   // array to store color

       for(int i=0; i<c;i++)    //sets starting color of points to -1
           ans[i]=-1;

       ans[0]=0; //sets first point color to 0

       
       boolean totalColors[] = new boolean[c]; //checks if path is already taken
       for(int i=0; i<c; i++)
               totalColors[i]=true;
      
       for(int s = 1; s < c; s++){
           
           Iterator<Integer> itr = adj[s].iterator(); //runs a path and changes the point color
           while(itr.hasNext()){
               int x = itr.next();
               if(ans[x] != -1){
                   totalColors[ans[x]] = false;
               }
           }

          
           int color;
           for(color = 0; color < c; color++){
               if(totalColors[color]==true)
                   break;
           }
           ans[s] = color;
           //again reseting value for new iteration
           for(int i = 0; i < s; i++)
               totalColors[i]=true;
       }

       System.out.println("Vertex\tColor");
       for(int p = 0; p < c; p++){
           System.out.println(p +"\t"+ans[p]);
       }
   }

   public static void main(String[] args){
       int V = 6, E = 8;
       GraphProblem g = new GraphProblem(V);
       g.addEdge(0,1);
       g.addEdge(0,4);
       g.addEdge(0,5);
       g.addEdge(4,5);
       g.addEdge(1,4);
       g.addEdge(1,3);
       g.addEdge(2,3);
       g.addEdge(2,4);

       System.out.println("Coloring of the graph is: ");
       g.ColorGraph(V);
   }
}
