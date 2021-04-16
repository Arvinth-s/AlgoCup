//OM NAMO NARAYANA
#include<bits/stdc++.h>
using namespace std;


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

void writeList(ofstream lfile, vector<long long> hist){

    lfile<<"\nwriting from solution.cpp\n";
    for(auto itr:hist){
        string temp = to_string(itr);
        lfile<<temp;
    }
}


int main(){
    ifstream qfile, ifile;
    string mode = "judgement_day";
    string iname = "./" +mode+ "/input/input";
    string oname = "./" +mode+ "/output/output";
    string lname = "./" +mode+ "/log/log";
    long long t = -1;
    while(++t<22){
        string ifile_name = iname + to_string(t) + ".txt";
        string ofile_name = oname + to_string(t) + ".txt";
        string lfile_name = lname + to_string(t) + ".txt";
        ifstream qfile, afile;
        ofstream lfile;
        qfile.open(ifile_name);
        afile.open(ofile_name);
        lfile.open(lfile_name, ios_base::app);
        if(!qfile || !afile || !lfile){
            cout<<ifile_name<<" file doesn't exist.\n";
        }

        long long n, m, k;
        qfile>>n>>m;
        vector<pair<long long, long long> > edges(n);
        for(long long i = 0; i < n; i++){
            edges[i] = pair<long long, long long>(-1, -1);
        }
        bool corner[n];
        memset(corner, true, sizeof(corner));
        long long values[n];
        for(long long i = 0; i < n; i++)qfile>>values[i];
        for(long long i = 0; i < m; i++){
            long long u, v;
            qfile>>u>>v;
            if(edges[u].first==-1){
                edges[u].first = v;
            }else{
                // if(edges[u].second!=-1){
                //     printf("edges[%lld]=(%lld, %lld) v:%lld\n", u, edges[u].first, edges[u].second, v);
                // }
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
        
        qfile>>k;
        
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
                    // if(edges[u].first==v){
                    //     assert(edges[u].second!=v);
                    //     v = edges[u].second;
                    // }
                    // else{
                    //     assert(edges[u].second==v);
                    //     v = ;
                    // }
                    hist.push_back(values[v]);
                    corner[v] = false;
                    prev = u;
                    u = v;
                    answer_length++;
                }


                // lfile<<"\nwriting from solution.cpp\n";
                // for(auto itr:hist){
                //     string temp = to_string(itr) + " ";
                //     lfile<<temp;
                // }


                int buffer = getMaxArea(hist);
                if(buffer >  res){
                    res = buffer;
                }
            }
        }

        // string ans;
        long long ans;
        afile>>ans;
        cout<<t<<" - ";

        if(res != ans){
            printf("res:%lld ans:%lld", res, ans);
        }else{
            printf("correct");
        }
        cout<<endl;

        /*
        if(res<k){
            if(ans == "Hell")cout<<"\tcorrect\n";
            else cout<<"\twrong. Predicted is less than answer."<<res<<" "<<k<<" answer length: "<<answer_length<<"\n";
        }else{
            if(ans == "Hell")cout<<"\twrong. Predicted is more than answer. "<<res<<" "<<k<<" answer length: "<<answer_length<<"\n";
            else cout<<"\tcorrect\n";
        }
        */
        
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