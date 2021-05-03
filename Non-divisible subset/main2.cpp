#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);


//Extracts all elements divisible by k - optimization -> length++ if got elements like this
//Extracts all elements with remainder = k/2 -> length++ if got elements like this
//Creates map with remainders and their frequence
//ForX2 - Compares remainders with elements already present and swaps if
//length is greater with the new elements
int nonDivisibleSubset(int k, vector<int> s) {
    
    int length = 0;
    bool divisible = false;
    bool divisibleHalf = false;
    auto it = s.begin();
	while (it != s.end())
	{
		if (*it>k && *it % k == 0 ) {
            divisible = true;
			it = s.erase(it);
		}if(*it>k && *it % k == k/2 && k%2==0 ){
            divisibleHalf = true;
			it = s.erase(it);
        }else {
			++it;
		}
	}

    

    map<int, int> remainders;
    for(int i=1; i<k; ++i){
        remainders.insert(pair<int,int>(i,0));
    }

    // it = s.begin();
    // while(it != s.end()){
    //     cout<<*it<<" ";
    //     ++it;
    // }
    // cout<<'\n';

    it = s.begin();
    while(it != s.end()){
        int remain = *it%k;
        remainders[remain]++;
        ++it;
    }

    vector<int> taken;
    for(int i=1; i<k; ++i){
        if(taken.size()==0){
            taken.push_back(i);
            length += remainders[i];
        }
        else{
            bool ajout = true;
            int trouble = 0;
            for(int j=0; j<taken.size()&& j<(k-1); ++j){
                // cout<<i<<" "<<remainders[i]<<" | "<<taken[j]<<" "<<remainders[taken[j]]<<" "<<taken.size()<<'\n';
                if(i+taken[j] == k){
                    ajout = false;
                    trouble = taken[j];
                }
            }
                
            if( ajout && remainders[i] !=0 ){
                taken.push_back(i);
                length += remainders[i];
            }else{
                if(remainders[i] > remainders[trouble]){
                    length = length - remainders[trouble] + remainders[i];
                }
            }
        }
    }

    if( divisible && length>0 ){
        length++;
    }
    if( divisibleHalf ){
        length++;
    }

    return length;
}


int main()
{
    // ofstream fout(getenv("OUTPUT_PATH"));

    // string first_multiple_input_temp;
    // getline(cin, first_multiple_input_temp);

    // vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    // int n = stoi(first_multiple_input[0]);

    // int k = stoi(first_multiple_input[1]);

    // string s_temp_temp;
    // getline(cin, s_temp_temp);

    // vector<string> s_temp = split(rtrim(s_temp_temp));

    // vector<int> s(n);

    // for (int i = 0; i < n; i++) {
    //     int s_item = stoi(s_temp[i]);

    //     s[i] = s_item;
    // }

    // vector<int> s = {14, 15, 16, 21, 18, 13, 5, 12};
    // int k = 3;

    // vector<int> s= {278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436};
    // int k = 7;
    // vector<int> s = {19, 10, 12, 10, 24, 25, 22};
    // int k = 4;
    vector<int> s = {1, 7, 2, 4};
    int k = 3;
    // vector<int> s = {1, 2, 3};
    // int k = 3;
    int result = nonDivisibleSubset(k, s);
    cout<<"len="<<result<<'\n';

    // vector<int> s = {14, 15, 16, 21, 18, 13, 5, 12};


    // fout << result << "\n";

    // fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
