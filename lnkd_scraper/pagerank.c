#include<stdlib.h>
#include<stdio.h>
#include<math.h>

typedef struct _node {
  char* name;
  //struct _node** neighbors;
  /* neighbors are inlink nodes */
  int* neighbors;
  int num_neighbors;
  int num_inlinks;
  int num_outlinks;
} node;

void init_node(node* n) {
  n->name="_unknown_";
  n->neighbors=NULL;
  n->num_neighbors=0;
}

/* edge is *n2 -> n1 ? *n2 referring n1 */
void set_edges(node** allnodes,int n1, int* n2, int sz_n2) {
  int i;
  allnodes[n1]->neighbors=n2;
  allnodes[n1]->num_neighbors=sz_n2;
  for(i=0;i<sz_n2;i++) {
    allnodes[i]->num_neighbors
  } 
}

void add_node(node* n1) {
}

void add_edge(node* n1, node* n2) {
  
}

void get_node_from() {
}

void print_pagerank(node** allnodes, int num_nodes, float* pr) {
  int i;
  for(i=0;i<num_nodes;i++) {
    printf("node %s score %f\n", allnodes[i]->name,pr[i]);
  }
}

void comp_pagerank(node** allnodes,int num_nodes,int max_iter, float* pagerank) {
  int i,j,k;
  float diff;
  float damping_factor=0.85;
  float min_value=(1.0-damping_factor)/num_nodes;
  float rank;

  for(i=0;i<num_nodes;i++) {
    pagerank[i]=1.0/num_nodes;
  }

  for(i=0;i<max_iter;i++) {
    diff=0.0;
    for(j=0;j<num_nodes;j++) {
      node* curnode=allnodes[j];
      //printf("cur node:%s. #neighbor:%d\n", curnode->name,curnode->num_neighbors);
      int* neighbors=curnode->neighbors;
      rank=min_value;
      //printf("pagerank=%f,rank=%f\n", pagerank[j],rank);
      for(k=0;k<curnode->num_neighbors;k++) {
        int neighbor=neighbors[k];
        node* node_neighbor=allnodes[neighbor];
        //printf("working on neighbor:%d\n", neighbor);
        rank +=damping_factor*pagerank[neighbor]/node_neighbor->num_neighbors;
      }
      diff+=fabs(pagerank[j]-rank);
      pagerank[j]=rank;
    }
    printf("diff:%f\n", diff);
  }
}

int main() {
  //node* n1 = (node*)malloc(sizeof(node));
  //node* n2 = (node*)malloc(sizeof(node));
  //node* n3 = (node*)malloc(sizeof(node));
  //node* n4 = (node*)malloc(sizeof(node));
  //node** ns = (node**)malloc(sizeof(node*)*4);
  int neibors[3];
  int N=4;//1,2,3,4
  node* allnodes[N];
  node n1,n2,n3,n4;
  init_node(&n1);
  init_node(&n2);
  init_node(&n3);
  init_node(&n4);
  allnodes[0]=&n1;
  allnodes[1]=&n2;
  allnodes[2]=&n3;
  allnodes[3]=&n4;
  n1.name="n1";
  n2.name="n2";
  n3.name="n3";
  n4.name="n4";
  neibors[0]=1;
  neibors[1]=2;
  neibors[2]=3;
  set_edges(allnodes,0,neibors,3);
  //printf("%s\n", n1.name);
  float pr[N];
  comp_pagerank(allnodes,N,10, pr);
  print_pagerank(allnodes,N,pr);
  //free(ns);

  return 1;
}
