// #include <bits/stdc++.h>
// #include <iostream>

// using namespace std;

// // Complete the formingMagicSquare function below.
// int formingMagicSquare(vector<vector<int>> s) {

//     int val = 0;
//     val = max((s[0][0]+s[1][1]+s[2][2]),(s[0][2]+s[1][1]+s[2][0]));

//     cout<<"val="<<val<<'\n';

//     int delta = 0;
//     bool end = false;
//     while(!end){
        
//         int weight[3][3][4] = { { {0,0,0,0}, {0,0,0,0}, {0,0,0,0} }, 
//                                 { {0,0,0,0}, {0,0,0,0}, {0,0,0,0} }, 
//                                 { {0,0,0,0}, {0,0,0,0}, {0,0,0,0} } };

//         for(int i=0; i<s.size(); ++i){
//             for(int j=0; j<s[i].size(); ++j){
//                 cout<<s[i][j]<<" ";
//             }
//             cout<<'\n';
//         }
        
//         for(int i=0; i<s.size(); ++i){
//             int sum = 0;
//             for(int j=0; j<s[i].size(); ++j){
//                 sum += s[i][j];
//             }
//             for(int j=0; j<s[i].size(); ++j){
//                 weight[i][j][0]=val-sum;
//             }
//         }

//         for(int j=0; j<s.size(); ++j){
//             int sum = s[0][j] + s[1][j] + s[2][j];
//             weight[0][j][1]=val-sum;
//             weight[1][j][1]=val-sum;
//             weight[2][j][1]=val-sum;
//         }

//         // int sum = s[0][0] + s[1][1] + s[2][2];
//         // weight[0][0][2]=val-sum;
//         // weight[1][1][2]=val-sum;
//         // weight[2][2][2]=val-sum;

//         // sum = s[0][2] + s[1][1] + s[2][0];
//         // weight[0][2][2]=val-sum;
//         // weight[1][1][3]=val-sum;
//         // weight[2][0][2]=val-sum;

//         int posI = -1;
//         int posJ = -1;
//         int max = INT_MIN;
//         for(int i=0; i<s.size(); ++i){
//             for(int j=0; j<s[i].size(); ++j){
//                 if(abs(weight[i][j][0] + weight[i][j][1] + weight[i][j][2] + weight[i][j][3]) >= max){
//                     max = abs(weight[i][j][0] + weight[i][j][1] + weight[i][j][2] + weight[i][j][3]);
//                     posI = i;
//                     posJ = j;
//                 }
//             }
//         }

//         cout<<"posI="<<posI<<", posJ="<<posJ<<", max="<<max<<'\n';

//         int min = INT_MAX;
//         for(int k=0; k<4; ++k){
//             if(weight[posI][posJ][k] <= min && weight[posI][posJ][k] != 0){
//                 min = weight[posI][posJ][k];
//             }
//         }


//         s[posI][posJ] += min;
//         delta += abs(min);

//         for(int i=0; i<s.size(); ++i){
//             for(int j=0; j<s[i].size(); ++j){
//                 cout<<weight[i][j][0]<<" "<<weight[i][j][1]<<" "<<weight[i][j][2]<<" "<<weight[i][j][3]<<" | ";
//                 // cout<<weight[i][j][0]+weight[i][j][1]+weight[i][j][2]+weight[i][j][3]<<" ";
//             }
//             cout<<'\n';
//         }

//         cout<<"change="<<min<<'\n';

//         bool end1 = true;
//         for(int i=0; i<s.size(); ++i){
//             int sumy = 0;
//             for(int j=0; j<s[i].size(); ++j){
//                 sumy += s[i][j];
//             }
//             if(sumy != val){
//                 end1 = false;
//             }
//         }

//         bool end2 = true;
//         for(int j=0; j<s.size(); ++j){
//             int sumy = s[0][j] + s[1][j] + s[2][j];
//             if(sumy != val){
//                 end2 = false;
//             }
//         }

//         bool end3 = true;
//         int sumy3 = s[0][0] + s[1][1] + s[2][2];
//         if(sumy3 != val){
//             end3 = false;
//         }

//         bool end4 = true;
//         int sumy4 = s[0][2] + s[1][1] + s[2][0];
//         if(sumy4 != val){
//             end4 = false;
//         }

//         if(end1 && end2 && end3 && end4){
//             end = true;
//         }else{
//             if(end1 && end2 && end3 && !end4){
//                 if(sumy4<val){
//                     val += 1;
//                 }else {
//                     val -= 1;
//                 }
//             }else if(end1 && end2 && !end3 && end4){
//                 if(sumy3<val){
//                     val += 1;
//                 }else {
//                     val -= 1;
//                 }
//             }
//         }
//         cout<<'\n';
//     }

//     return delta;
// }

// int formingMagicSquare2(vector<vector<int>> s){
    
// }

// int main()
// {
//     ofstream fout(getenv("OUTPUT_PATH"));

//     // vector<vector<int>> s { {4,8,2}, {4,5,7}, {6,1,6}};
//     // vector<vector<int>> s { {4,9,2}, {3,5,7}, {8,1,5}};
//     vector<vector<int>> s { {5,3,4}, {1,5,8}, {6,4,2}};
//     // vector<vector<int>> s { {1,3,8}, {6,4,1}, {2,6,5}};
//     // int result = formingMagicSquare(s);

//     int result = formingMagicSquare2(s);
    

//     cout << result << "\n";

//     return 0;
// }
