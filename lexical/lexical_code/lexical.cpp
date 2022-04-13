#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

typedef pair<string, string> pss;

struct{
	bool stringFlag;
	bool integerFlag;
	bool
}flag;

bool isDeli(char c) {

}

pss tokenize(string input) {
	pss output;
	//string token
	if (flag.stringFlag) {
		output.first = "STRING";
		output.second = input;
	}
	//integer token
	else if (flag.integerFlag) {
		output.first = "INTEGER";
		output.second = input;
	}
	//variable token
	else if (input == "int" || input == "INT") {
		output.first = "VARTYPE";
		output.second = "INT";
	}
	else if (input == "char" || input == "CHAR") {
		output.first = "VARTYPE";
		output.second = "CHAR";
	}
	//keyword token
	else if (input == "if" || input == "IF") {
		output.first = "KEYWORD";
		output.second = "IF";
	}
	else if (input == "else" || input == "ELSE") {
		output.first = "KEYWORD";
		output.second = "ELSE";
	}
	else if (input == "while" || input == "WHILE") {
		output.first = "KEYWORD";
		output.second = "WHILE";
	}
	else if (input == "return" || input == "RETURN") {
		output.first = "KEYWORD";
		output.second = "RETURN";
	}
	//operator token
	else if (input == "+") {
		output.first = "OP";
		output.second = "+";
	}
	else if (input == "-") {
		output.first = "OP";
		output.second = "-";
	}
	else if (input == "*") {
		output.first = "OP";
		output.second = "*";
	}
	else if (input == "/") {
		output.first = "OP";
		output.second = "/";
	}
	else if (input == "=") {
		output.first = "ASSIGN";
	}
	//compare operator token
	else if (input == "<") {
		output.first = "COMPARE";
		output.second = "<";
	}
	else if (input == ">") {
		output.first = "COMPARE";
		output.second = ">";
	}
	else if (input == "<=") {
		output.first = "COMPARE";
		output.second = "<=";
	}
	else if (input == ">=") {
		output.first = "COMPARE";
		output.second = "<";
	}
	else if (input == "==") {
		output.first = "COMPARE";
		output.second = "==";
	}
	else if (input == "!=") {
		output.first = "COMPARE";
		output.second = "!=";
	}
	//other character token
	else if (input == ";") {
		output.first = "SEMICOLON";
		output.second = ";";
	}
	else if (input == "{") {
		output.first = "LB";
		output.second = "{";
	}
	else if (input == "}") {
		output.first = "RB";
		output.second = "}";
	}
	else if (input == "(") {
		output.first = "LPAREN";
		output.second = "(";
	}
	else if (input == ")") {
		output.first = "RPAREN";
		output.second = ")";
	}
	else if (input == ",") {
		output.first = "COMMA";
		output.second = ",";
	}

	return output;
}

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

		for (int i = 0; i < buffer.length; i++) {
			
		}

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
