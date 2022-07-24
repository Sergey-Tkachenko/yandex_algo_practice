#include <fstream>
#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>

#define _USE_MATH_DEFINES


using namespace std;


bool sort_pairs(const pair<double, int> &a, const pair<double, int> &b)
{
    if (a.first < b.first)
    {
        return true;
    }
    else if (a.first > b.first)
    {
        return false;
    }
    else if (a.second < b.second)
    {
        return true;
    }
    
    return false;
}

int main()
{
    ifstream fin("005");
    long int N;
    fin >> N;

    vector<pair<double, int>> events;
    events.reserve(4 * N);

    double r_left_max = -1.0;
    double r_right_min = INT64_MAX * 1.0;
    for (long int i = 0; i < N; i++)
    {
        double phi_1, phi_2, r_1, r_2;
        fin >> r_1 >> r_2 >> phi_1 >> phi_2;

        // add new event
        if (phi_1 > phi_2)
        {
            // case when we should divide interval
            events.push_back({phi_1, 1});
            events.push_back({2 * M_PI, -1});

            events.push_back({phi_2, -1});
            events.push_back({0, 1});
        }
        else
        {
            events.push_back({phi_1, 1});
            events.push_back({phi_2, -1});
        }

        // update max and min

        r_left_max = max(r_left_max, r_1);
        r_right_min = min(r_right_min, r_2);
    }

    double mutiplier = max(0.0, (r_right_min * r_right_min - r_left_max * r_left_max) / 2 ); 

    sort(events.begin(), events.end(), sort_pairs);
    long int counter = 0;
    double total_area = 0;
    for(long int i=0; i < events.size(); ++i)
    {
        if (counter == N)
        {
            total_area += mutiplier * (events[i].first - events[i - 1].first);
        }

        // update counter
        if (events[i].second == 1)
        {
            counter++;
        }
        else if (events[i].second == -1)
        {
            counter--;
        }
        
    }

    cout << std::setprecision(20) << total_area;
    


    return 0;
}