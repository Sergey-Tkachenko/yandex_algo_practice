#include "iostream"
#include "vector"

using namespace std;
int main() {
    int n = 0;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        vector<int> coords(8);
        for (int j = 0; j < 8; ++j)
        {
            cin >> coords[j];
        }

        int x_min = coords[0];
        int i_min = 0;
        for (int j = 1; j < 4; ++j)
        {
            if (coords[2 * j] < x_min)
            {
                x_min = coords[2 * j];
                i_min = j;
            }
        }

        int x_2_min = 101;
        int i_2_min = -1;

        for (int j = 0; j < 4; ++j)
        {
            if ((coords[2 * j] < x_2_min) and (j != i_min))
            {
                x_2_min = coords[2 * j];
                i_2_min = j;
            }
        }

        int d_x = coords[2 * i_min] - coords[2 * i_2_min];
        int d_y = coords[2 * i_min + 1] - coords[2 * i_2_min + 1];


        int pt_3;
        int pt_4;
        for (int j = 0; j < 4; ++j)
        {
            if ((j != i_min) and (j != i_2_min))
            {
                pt_3 = j;
            }
        }

        for (int j = 0; j < 4; ++j)
        {
            if ((j != i_min) and (j != i_2_min) and (j != pt_3))
            {
                pt_4 = j;
            }
        }

        int d_x_2 = coords[2 * pt_3] - coords[2 * pt_4];
        int d_y_2 = coords[2 * pt_3 + 1] - coords[2 * pt_4 + 1];
        if (((d_x == d_x_2) and (d_y_2 == d_y)) or ((d_x == -d_x_2) and (d_y == - d_y_2)))
        {
            cout << "YES";
        }
        else
        {
            cout << "NO";
        }
        cout << endl;
    }
    return 0;
}
