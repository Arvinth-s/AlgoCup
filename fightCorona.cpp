    #include<bits/stdc++.h>
    using namespace std;

    #define MAX 2000
    #define MAX_int 10e7



    vector<long> Calculate(long N, long M, bool Graph[MAX][MAX], long D[])
    {
        vector<long> ans;
        for(long n = 0; n < N; n++)
            ans.push_back(MAX_int);
        for(long m = 0; m < M; m++)
        {
            printf("this D[%ld]:%ld..\n", m, D[m]);
            if(m >= ans[D[m]])
                continue;
            ans[D[m]] = m;
            bool visited[N];
            memset(visited, false, sizeof(visited));
            long src = D[m];
            visited[src] = true;
            long midx = src;
            while(midx != -1)
            {
                for(long n = 0; n < N; n++)
                {
                    if(!visited[n] && Graph[midx][n] && (ans[midx]+1 < ans[n]))
                        ans[n] = ans[midx]+1;
                }
                midx = -1;
                for(long n = 0; n < N; n++)
                {
                    if(!visited[n])
                    {
                        midx = n;
                        break;
                    }
                }
                if(midx==-1)
                    break;
                for(long n = midx; n < N; n++)
                {
                    if(!visited[n] && ans[n] < ans[midx])
                        midx = n;
                }
                visited[midx] = true;

            }
        }
        return ans;
    }

    int main()
    {

        bool Graph[MAX][MAX];
        memset(Graph,  false, sizeof(Graph));
        long a, b;
        for(long n = 0; n < R; n++)
        {
            scanf("%ld%ld", &a, &b);
            a--;b--;
            Graph[a][b] = Graph[b][a] = true;
        }

        long D[M];
        for(long m = 0; m < M; m++)
        {
            scanf("%ld", &D[m]);
            D[m]--;
            printf("D[%ld]:%ld\n", m, D[m]);
        }

        vector<long>Days = Calculate(N, M, Graph, D);


        for(long q = 0; q < Q; q++)
        {
            long d, t;
            scanf("%ld%ld", &d, &t);
            d--;
            if(Days[d] +1 <= t)
            {
                printf("YES\n");
            }
            else
            {
                printf("NO\n");
            }
        }
        return 0;
    }