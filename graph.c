#include <stdio.h>
#include <stdlib.h>

// Structure for adjacency list node
typedef struct Node {
    int vertex;
    struct Node* next;
} *NODE;

// Structure for Graph
typedef struct Graph {
    int numVertices;
    NODE* adjLists;  // array of linked lists
} *GRAPH;

// Function to create a new node
NODE createNode(int v) {
    NODE newNode = (NODE)malloc(sizeof(struct Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

// Function to create a graph with n vertices
GRAPH createGraph(int vertices) {
    GRAPH graph = (GRAPH)malloc(sizeof(struct Graph));
    graph->numVertices = vertices;

    // Create an array of adjacency lists
    graph->adjLists = (NODE*)malloc(vertices * sizeof(NODE));

    // Initialize all adjacency lists as empty
    for (int i = 0; i < vertices; i++)
        graph->adjLists[i] = NULL;

    return graph;
}

// Function to add an edge (undirected)
void addEdge(GRAPH graph, int src, int dest) {
    // Add edge from src to dest
    NODE newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;

    // Add edge from dest to src (since undirected)
    newNode = createNode(src);
    newNode->next = graph->adjLists[dest];
    graph->adjLists[dest] = newNode;
}

// Function to display the graph
void displayGraph(GRAPH graph) {
    printf("\nGraph adjacency list:\n");
    for (int v = 0; v < graph->numVertices; v++) {
        NODE temp = graph->adjLists[v];
        printf("Vertex %d: ", v);
        while (temp) {
            printf("-> %d ", temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
}

// Main function
int main() {
    int vertices, edges, src, dest;

    printf("Enter number of vertices: ");
    scanf("%d", &vertices);

    GRAPH graph = createGraph(vertices);

    printf("Enter number of edges: ");
    scanf("%d", &edges);

    for (int i = 0; i < edges; i++) {
        printf("Enter edge (src dest): ");
        scanf("%d %d", &src, &dest);
        addEdge(graph, src, dest);
    }

    displayGraph(graph);
    return 0;
}
