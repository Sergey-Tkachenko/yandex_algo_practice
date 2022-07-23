#include "iostream"
#include "vector"
#include "string"
#include "unordered_map"
#include <fstream>

using namespace std;
int main(){

    ifstream fin("input_15.txt");
    if (!fin.is_open())
    {
        return 1;
    }

    long long int s;

    fin >> s;

    long int len_a, len_b, len_c;


    // input
    fin >> len_a;
    vector<long long int> seq_a(len_a);
    for(long int i = 0; i < len_a; i++)
    {
        fin >> seq_a[i];
    }
    
    fin >> len_b;
    vector<long long int> seq_b(len_b);
    for (long int  i = 0; i < len_b; i++)
    {
        fin >> seq_b[i];
    }

    fin >> len_c;
    unordered_map<long long int, long int> set_c(len_c);
    for(long int  i = 0; i < len_c; i++)
    {
        long long t; fin >> t;
        if(set_c.find(t) != set_c.end())
        {
            set_c[t] = min(set_c[t], i);
        }
        else
        {
            set_c[t] =i;
        }
    }

    // find elements
    vector<long int> ans = {len_a, len_b, len_c};
    for(long int i = 0; i < len_a; ++i)
    {
        for(long int j = 0; j < len_b; ++j)
        {
            if(set_c.find(s - seq_a[i] - seq_b[j]) != set_c.end())
            {
                if (ans[0] == len_a)
                {
                    ans[0] = i; ans[1] = j; ans[2] = set_c[s - seq_a[i] - seq_b[j]];
                }  
            }
        }
    }

    if(ans[0] == len_a)
    {
        cout << -1 << endl;
    }
    else
    {
        cout << ans[0] << " " << ans[1] << " " << ans[2] << endl;
    }
    return 0;
}