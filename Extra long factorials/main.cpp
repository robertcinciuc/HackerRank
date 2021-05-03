#include <bits/stdc++.h>
#include <string>
using namespace std;

void extraLongFactorials(int n) {
    string fact = "1";
    for(int i=2; i<=n; ++i){
        string smol = to_string(i);
        string newFact = multiply(fact, smol);
        fact = newFact;
    }
    cout<<fact;
}

string multiply(string larg, string smol){

    string res ="";
    if(larg=="0" || smol=="0"){
        res = "0";
    }else{
        int addMult = 0;
        vector<vector<int>> sumy(smol.length(), vector<int> ((larg.length()+smol.length()), 0));

        int count = 0;
        int shift = smol.length();
        for(int i=(smol.length()-1); i>=0; --i){
            int addSum = 0;
            for(int j=(larg.length()-1); j>=0; --j){
                int tmp = (smol[i]-48)*(larg[j]-48);
                if((tmp%10 + addSum)<10){
                    sumy[count][j+shift]= tmp%10 + addSum;
                    addSum = tmp/10;
                }else{
                    sumy[count][j+shift]= (tmp%10 + addSum)%10;
                    addSum = tmp/10+1;
                }
            }        
            shift--;
            sumy[count][shift] = addSum;
            count++;
        }

        int addSum = 0;
        for(int j=(larg.length()+smol.length()-1); j>=0; --j){
            int tmp = 0;
            for(int i=(smol.length()-1); i>=0; --i){
                tmp += sumy[i][j];
            }
            tmp += addSum;
            addSum = tmp/10;
            res = to_string(tmp%10) + res;     
        }

        bool zeros = true;
        int i = 0;
        while(zeros){
            if(res[i]=='0'){
                res.erase(0,1);
            }else{
                zeros = false;
            }
        }
    }

    // cout<<res<<'\n';

    return res;
}

int main(){

    int n = 15;
    string fact = "1";
    for(int i=2; i<=n; ++i){
        string smol = to_string(i);
        string newFact = multiply(fact, smol);
        fact = newFact;
    }

    cout<<fact<<"END"<<'\n';

    return 0;
}
