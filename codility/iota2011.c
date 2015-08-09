#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <queue>

int solution ( const std::vector<int> &A );
int solution ( const std::vector<int> &A ) 
{
    int N(A.size()), s(A[0]), t(A[A.size()-1]);

    std::map<int, std::list<int> > graph;
    std::map<int, int> distance;
    // Construct graph
    graph[s].push_front(A[1]);
    for (int i = 1; i < N - 1; ++i) {
        graph[A[i]].push_front(A[i-1]);
        graph[A[i]].push_front(A[i+1]);
        distance[A[i]] = 0;
    }
    graph[t].push_front(A[N-2]);
    distance[t] = 0;
    // Setup distance
    distance[s] = 1;

    // BFS
    std::queue<int> q;
    q.push(s);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (std::list<int>::const_iterator it = graph[u].begin();
             it != graph[u].end(); ++it ) {
            if (distance[*it] == 0) {
                distance[*it] = distance[u] + 1;
                q.push(*it);
            }
        }
    }
    return distance[t];
}

int main()
{
    int arr[] = {1, 10, 6, 5, 10, 7, 5, 1};
    std::vector<int> A(arr, arr + 8);

    std::cout << solution( A ) << '\n';
}
