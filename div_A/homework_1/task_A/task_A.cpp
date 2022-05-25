#include "iostream"

using namespace std;
int main(){
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    if (a == 0)
    {
        if (b == 0)
        {
            cout << "INF" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    else
    {
        if (abs(b) % abs(a) != 0)
        {
            cout << "NO" << endl;
        }
        else
        {
            int zero_num = - b / a;
            if (c == 0)
            {
                cout << zero_num << endl;
            }
            else
            {
                if (c * zero_num + d == 0)
                {
                    cout << "NO" << endl;
                }
                else
                {
                    cout << zero_num << endl;
                }
            }
        }
    }

    return 0;
}