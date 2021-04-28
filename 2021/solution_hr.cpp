#include<bits/stdc++.h>
using namespace std;


void processCycle(vector<pair<long long, long long> > &edges, bool corner[], int m, long long values[]){
    int n = edges.size();
    bool visited[n];
    memset(visited, false, sizeof(visited));
    for(int i = 0; i < n; i++){
        if(!corner[i])continue;
        visited[i] = true;

        long long u = edges[i].first;
        if(edges[i].first == -1)continue;
        long long prev = i;
        visited[u] = true;
        while(edges[u].second!=-1){
            long long v = (edges[u].first==prev)?edges[u].second:edges[u].first;
            visited[v] = true;
            prev = u;
            u = v;
        }
    }

    for(int i = 0; i < n; i++){
        if(visited[i])continue;
        visited[i] = true;

        int min_idx = i;


        long long u = edges[i].first;

        if(values[u] < values[i]){
            min_idx = u;
        }

        long long prev = i;
        visited[u] = true;
        while(true){
            long long v = (edges[u].first==prev)?edges[u].second:edges[u].first;
            if(visited[v]){
                int x = edges[min_idx].first;
                if(edges[x].first==min_idx){
                    edges[x].first=-1;
                }else{
                    edges[x].second=-1;
                }
                corner[x] = true;
                corner[min_idx] = true;
                break;
            }
            visited[v] = true;
            prev = u;
            u = v;
        }
    }
    return;
}

long long getMaxArea(vector<long long> hist)
{

    long long n = hist.size();
    
    // Create an empty stack. The stack holds indexes 
    // of hist[] array. The bars stored in stack are 
    // always in increasing order of their heights.
    
    stack<long long> s;
  
    long long max_area = 0; // Initialize max area
    long long tp;  // To store top of stack
    long long area_with_top; // To store area with top bar
                       // as the smallest bar
  
    // Run through all bars of given histogram
    long long i = 0;
    while (i < n)
    {
        // If this bar is higher than the bar on top 
        // stack, push it to stack
        if (s.empty() || hist[s.top()] <= hist[i])
            s.push(i++);
  
        // If this bar is lower than top of stack, 
        // then calculate area of rectangle with stack 
        // top as the smallest (or minimum height) bar. 
        // 'i' is 'right index' for the top and element 
        // before top in stack is 'left index'
        else
        {
            tp = s.top();  // store the top index
            s.pop();  // pop the top
  
            // Calculate the area with hist[tp] stack 
            // as smallest bar
            area_with_top = hist[tp] * (s.empty() ? i : 
                                   i - s.top() - 1);
  
            // update max area, if needed
            if (max_area < area_with_top)
                max_area = area_with_top;
        }
    }
  
    // Now pop the remaining bars from stack and calculate
    // area with every popped bar as the smallest bar
    while (s.empty() == false)
    {
        tp = s.top();
        s.pop();
        area_with_top = hist[tp] * (s.empty() ? i : 
                                i - s.top() - 1);
  
        if (max_area < area_with_top)
            max_area = area_with_top;
    }
  
    return max_area;
}



int main(){

        long long n, m;
        cin>>n>>m;
        vector<pair<long long, long long> > edges(n);
        for(long long i = 0; i < n; i++){
            edges[i] = pair<long long, long long>(-1, -1);
        }
        bool corner[n];
        memset(corner, true, sizeof(corner));
        long long values[n];
        for(long long i = 0; i < n; i++)cin>>values[i];
        for(long long i = 0; i < m; i++){
            long long u, v;
            cin>>u>>v;
            if(edges[u].first==-1){
                edges[u].first = v;
            }else{
                assert(edges[u].second==-1);
                edges[u].second = v;
                corner[u] = false;
            }
            
            if(edges[v].first==-1){
                edges[v].first = u;
            }else{
                assert(edges[v].second==-1);
                edges[v].second = u;
                corner[v] = false;
            }
        }
        
        processCycle(edges, corner,  m, values);
        
        long long res=0;
        long long answer_length = 2;
        
        for(long long i = 0; i < n; i++){
            if(corner[i]){
                answer_length = 2;
                corner[i] = false;//redundant. Won't be called again
                if(edges[i].first==-1){
                    res=max(res, values[i]);
                    continue;
                }

                assert(edges[i].second==-1);
                vector<long long> hist;
                hist.push_back(values[i]);
                long long u = edges[i].first;
                corner[u] = false;
                hist.push_back(values[u]);
                long long prev = i;
                while(edges[u].second!=-1){
                    long long v = (edges[u].first==prev)?edges[u].second:edges[u].first;

                    hist.push_back(values[v]);
                    corner[v] = false;
                    prev = u;
                    u = v;
                    answer_length++;
                }


                int buffer = getMaxArea(hist);
                if(buffer >  res){
                    res = buffer;
                }
            }
        }

        cout<<res;

        
    
    }