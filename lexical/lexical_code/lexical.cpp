#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int main(void) {
	
	ifstream fin;
	ofstream fout;
	string buffer;
	string token, value;
	vector<pair<string, string>> result;

	fin.open("test.c");

	while (fin.peek() != EOF) {
		token = value = "";
		getline(fin, buffer);



		result.push_back({token, value});
	}

	fin.close();

	fout.open("test.out");

	for (auto i : result) {
		if (i.second == "")
			buffer = "<" + i.first + ">\n";
		else 
			buffer = "<" + i.first + ", " + i.second + ">\n";
		fout << buffer;
	}

	fout.close();

	return 0;
}
