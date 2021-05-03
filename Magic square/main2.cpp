#include <bits/stdc++.h>
#include <iostream>

using namespace std;

// Complete the formingMagicSquare function below.
int formingMagicSquare3(vector<vector<int>> s) {
    vector<vector<vector<int>>> all = {
            {{8, 1, 6}, {3, 5, 7}, {4, 9, 2}},
            {{6, 1, 8}, {7, 5, 3}, {2, 9, 4}},
            {{4, 9, 2}, {3, 5, 7}, {8, 1, 6}},
            {{2, 9, 4}, {7, 5, 3}, {6, 1, 8}}, 
            {{8, 3, 4}, {1, 5, 9}, {6, 7, 2}},
            {{4, 3, 8}, {9, 5, 1}, {2, 7, 6}}, 
            {{6, 7, 2}, {1, 5, 9}, {8, 3, 4}}, 
            {{2, 7, 6}, {9, 5, 1}, {4, 3, 8}}};

    int mini = -1;
    for(int i=0; i<8; ++i){
        int tmpSum = 0;
        for(int j=0; j<3; ++j){
            for(int k=0; k<3; ++k){
                tmpSum += abs(all[i][j][k]-s[j][k]);
            }
        }
        // cout<<"tmpSum="<<tmpSum<<'\n';
        if(mini==-1 || tmpSum<=mini){
            mini = tmpSum;
        }

    }

    // cout<<"yo";
    return mini;
}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    // vector<vector<int>> s { {4,8,2}, {4,5,7}, {6,1,6}};
    // vector<vector<int>> s { {4,9,2}, {3,5,7}, {8,1,5}};
    vector<vector<int>> s { {5,3,4}, {1,5,8}, {6,4,2}};
    // vector<vector<int>> s { {1,3,8}, {6,4,1}, {2,6,5}};
    // int result = formingMagicSquare(s);

    int result = formingMagicSquare3(s);
    

    cout << result << "\n";

    return 0;
}
