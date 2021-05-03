// #include <bits/stdc++.h>

// using namespace std;

// string ltrim(const string &);
// string rtrim(const string &);
// vector<string> split(const string &);


// //Creates all combinations of elements
// //Selects combinations that respect that rule (s[i]+s[j])% k != 0
// int genPermut(int nbLeft, vector<int> taken, vector<int> left, int lenMax, int k){

//     bool found = false;
//     for(int i=0; i<taken.size(); ++i){
//         for(int j=i+1; j<taken.size(); ++j){
//             if((taken[i]+taken[j])%k==0){
//                 found = true;
//             }
//         }    
//     }

//     int iterations = left.size();
//     if(iterations==0){
//         if(!found && taken.size() >= lenMax){
//                 lenMax = taken.size();
//             }
//     }else{
//         while(iterations>0){
//             if(nbLeft>0){
//                 if(!found && taken.size() >= lenMax){
//                     lenMax = taken.size();
//                 }
//                 int elem = left.back();
//                 taken.push_back(elem);
//                 left.pop_back();
//                 --nbLeft;
//                 int len = genPermut(nbLeft,taken,left,lenMax,k);
//                 if(len>=lenMax){
//                     lenMax=len;
//                 }
//                 taken.pop_back();
//             }
//             iterations--;
//         }
//     }
//     return lenMax;
// }


// //Extracts all elements that are divisible by k - for optimization
// //Extracts the max lenth by calling genPermut
// //Adds 1 to length if the dividents list contains at least 1 element
// int nonDivisibleSubset(int k, vector<int> s) {
    
//     vector<int> dividents;
//     auto it = s.begin();
// 	while (it != s.end())
// 	{
// 		if (*it>k && *it % k == 0 ) {
//             dividents.push_back(*it);
// 			it = s.erase(it);
// 		}else {
// 			++it;
// 		}
// 	}

//     vector<int> taken;
//     int lengthy = genPermut(s.size(), taken, s, 0, k);
//     if(dividents.size() > 0 ){
//         lengthy++;
//     }

//     return lengthy;
// }


// int main()
// {
//     // ofstream fout(getenv("OUTPUT_PATH"));

//     // string first_multiple_input_temp;
//     // getline(cin, first_multiple_input_temp);

//     // vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

//     // int n = stoi(first_multiple_input[0]);

//     // int k = stoi(first_multiple_input[1]);

//     // string s_temp_temp;
//     // getline(cin, s_temp_temp);

//     // vector<string> s_temp = split(rtrim(s_temp_temp));

//     // vector<int> s(n);

//     // for (int i = 0; i < n; i++) {
//     //     int s_item = stoi(s_temp[i]);

//     //     s[i] = s_item;
//     // }

//     // vector<int> s = {14, 15, 16, 21, 18, 13, 5, 12};
//     // int k = 3;

//     vector<int> s = {19, 10, 12, 10, 24, 25, 22};
//     int k = 4;
//     // vector<int> s = {1, 7, 2, 4};
//     // int k = 3;
//     int result = nonDivisibleSubset(k, s);
//     // vector<int> t;
//     // int lengthy = genPermut(s.size(), t, s, 0, k);
//     cout<<"len="<<result<<'\n';

//     // vector<int> s = {14, 15, 16, 21, 18, 13, 5, 12};
//     // vector<int> s = {1, 2, 3};
//     // int k = 3;
//     // vector<int> s = {19, 10, 12, 10, 24, 25, 22};
//     // int k = 4;
//     // vector<int> t;
//     // int lengthy = genPermut(s.size(), t, s, 0, k);
//     // cout<<"len="<<lengthy<<'\n';


//     // fout << result << "\n";

//     // fout.close();

//     return 0;
// }

// string ltrim(const string &str) {
//     string s(str);

//     s.erase(
//         s.begin(),
//         find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
//     );

//     return s;
// }

// string rtrim(const string &str) {
//     string s(str);

//     s.erase(
//         find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
//         s.end()
//     );

//     return s;
// }

// vector<string> split(const string &str) {
//     vector<string> tokens;

//     string::size_type start = 0;
//     string::size_type end = 0;

//     while ((end = str.find(" ", start)) != string::npos) {
//         tokens.push_back(str.substr(start, end - start));

//         start = end + 1;
//     }

//     tokens.push_back(str.substr(start));

//     return tokens;
// }
