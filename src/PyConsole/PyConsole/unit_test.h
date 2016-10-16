#pragma once
#include <string>
#include <vector>
#include <iostream>
#include <map>

#ifdef _WIN32
#include <cstdlib>
#endif
#include "ffpython.h"
using namespace std;


void testMain();

inline void testMain()
{	
	/// init python interpreter
	Py_Initialize();

	ffpython_t::add_path("./");
	ffpython_t i_interpretor;

	try
	{
		i_interpretor.call<void>("test_interface", "add", 99, 1);
		string i_current_dir = i_interpretor.call<string>("test_interface","getCurrentDir");
		string i_working_dir = i_interpretor.call<string>("test_interface","getWorkingDir");
		cout << i_current_dir << endl;
		cout << i_working_dir << endl;
		
#ifdef _PKG
		i_interpretor.call<void>("Py2CplusZipper", "beginPackagePy",i_working_dir);
#endif // _PKG
		
	}
	catch (exception & ex)
	{
		cout << ex.what() << endl;
	}
	Py_Finalize();
}



class TestSocket
{
public:
	TestSocket() {}
	bool connnect(string t_ip, string t_port) { return false; }
	bool send(string t_data) { return false; }
	bool onRecieve(string t_data) { return false; }
	bool close() { return false; }

};