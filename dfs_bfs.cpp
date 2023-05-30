#include<iostream>
#include<vector>
#include<queue>
using namespace std;

const int N = 1e5+10;
vector<int> g[N];

bool vis[N];

void dfs(int vertex){
    vis[vertex] = 1;
    cout << vertex << " ";
    for(int child: g[vertex]) {
        if(vis[child]) continue;
        dfs(child);
    }
}

void bfs(int source) {
    queue<int> q;
    q.push(source);
    vis[source] = true;
    while(!q.empty()) {
        int cur_v = q.front();
        q.pop();
        cout << cur_v << " ";
        for(int child : g[cur_v]){
            if(vis[child]) continue;
            q.push(child);
            vis[child] = 1;
        }
    }
}

int main(){
    int v,e;
    cin >> v >> e;
    for(int i=0;i<e;i++){
        int v1,v2;
        cin >> v1 >> v2;
        g[v1].push_back(v2);
        g[v2].push_back(v1);
    }
    dfs(1);
    return 0;
    // int n;
    // cout << "Enter the starting vertex for dfs :\t";
    // cin >> n;
    bfs(1);
}