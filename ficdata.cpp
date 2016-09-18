#include<bits/stdc++.h>
using namespace std;
bool flag =true;
string randomStrGen(int length) {
    static string charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    string result;
    result.resize(length);
	if(flag){
		srand(time(NULL));
		flag = false;
	}
    for (int i = 0; i < length; i++)
        result[i] = charset[rand() % charset.length()];

    return result;
}
int main(){
	fstream fout;
	fout.open("abc.csv",ios::out);
	float date;
	string s1[9];
	float LO = 0,HI = 100;
	
	for (int i=0;i<10;i++){
		float r3 = LO + static_cast <float> (rand()) /( static_cast <float> (RAND_MAX/(HI-LO)));
		fout<<randomStrGen(10)<<" "<<r3<<" "<<randomStrGen(12)<<" "<<randomStrGen(5)<<" "<<randomStrGen(15)<<" "<<randomStrGen(10)<<" "<<randomStrGen(10)<<" "<<randomStrGen(10)<<" "<<randomStrGen(10)<<" "<<randomStrGen(10)<<" "<<randomStrGen(10)<<endl;
	}

}
