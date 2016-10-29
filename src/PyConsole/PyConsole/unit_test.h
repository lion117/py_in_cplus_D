#pragma once
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <memory>

#include "PyEmbeder.h"
using namespace std;


void testMain();

inline void testMain()
{	
	/// init python interpreter
    PyEmbeder::init();
	ffpython_t i_interpretor;

	try
	{
		i_interpretor.call<void>("test_interface", "add", 99, 1);
		string i_current_dir = i_interpretor.call<string>("test_interface","getCurrentDir");
		string i_working_dir = i_interpretor.call<string>("test_interface","getWorkingDir");


		cout << i_current_dir << endl;
		cout << i_working_dir << endl;	

        PyEmbeder::finilize(i_interpretor, i_working_dir);
	}
	catch (exception & ex)
	{
		cout << ex.what() << endl;
	}
}



