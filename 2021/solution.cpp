//OM NAMO NARAYANA
#include<bits/stdc++.h>
using namespace std;


long getMaxArea(vector<long> hist)
{

    long n = hist.size();
    
    // Create an empty stack. The stack holds indexes 
    // of hist[] array. The bars stored in stack are 
    // always in increasing order of their heights.
    
    stack<long> s;
  
    long max_area = 0; // Initialize max area
    long tp;  // To store top of stack
    long area_with_top; // To store area with top bar
                       // as the smallest bar
  
    // Run through all bars of given histogram
    long i = 0;
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
    ifstream qfile, ifile;
    string iname = "./uploaded/judgement_day/input/input";
    string oname = "./uploaded/judgement_day/output/output";
    int t = 20;
    while(--t){
        string ifile_name = iname + to_string(t) + ".txt";
        string ofile_name = oname + to_string(t) + ".txt";
        ifstream qfile, afile;
        qfile.open(ifile_name);
        afile.open(ofile_name);
        if(!qfile || !afile){
            cout<<t<<" file doesn't exist.\n";
        }

        long n, m, k;
        qfile>>n>>m;
        vector<pair<long, long> > edges(n);
        for(long i = 0; i < n; i++){
            edges[i] = pair<long, long>(-1, -1);
        }
        bool corner[n];
        memset(corner, true, sizeof(corner));
        long values[n];
        for(long i = 0; i < n; i++)cin>>values[i];
        for(long i = 0; i < m; i++){
            long u, v;
            qfile>>u>>v;
            if(edges[u].first==-1){
                edges[u].first = v;
            }else{
                edges[u].second = v;
                corner[u] = false;
            }
            
            if(edges[v].first==-1){
                edges[v].first = u;
            }else{
                edges[v].second = u;
                corner[v] = false;
            }
        }
        
        qfile>>k;
        
        long res=0;
        
        bool visited[n];
        memset(visited, false, sizeof(visited));
        
        for(long i = 0; i < n; i++){
            if(corner[i] && !visited[i]){
                if(edges[i].first==-1){
                    visited[i] = true;
                    corner[i]=false;
                    res=max(res, values[i]);
                    continue;
                }
                
                corner[i]=false;
                assert(edges[i].second==-1);
                vector<long> hist;
                hist.push_back(values[i]);
                long u = edges[i].first;
                corner[u] = false;
                hist.push_back(values[u]);
                while(edges[u].second!=-1){
                    long v = (edges[u].first==v)?edges[u].second:edges[u].first;
                    hist.push_back(values[v]);
                    u = v;
                    visited[u]=true;
                    corner[u]=false;
                }
                //cout<<i<<" "<<getMaxArea(hist)<<endl;
                res = max(res, getMaxArea(hist));
            }
        }

        string ans;
        afile>>ans;
        cout<<t<<" - ";
        if(res<k){
            if(ans == "Hell")cout<<t<<"correct\n";
            else cout<<"wrong\n";
        }else{
            if(ans == "Hell")cout<<t<<"wrongt\n";
            else cout<<"correct\n";
        }
        
    /*
        0 1 2 3 4 5 6 7 8
        8 3 1 2 6 9 7 4 5 
        7 5
        4 8
        3 6
        6 0
        
        [4, 9] [6, 5] [2, 7, 8]
    */
        
    
    }
}