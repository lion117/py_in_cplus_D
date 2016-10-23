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





class ScreenIO;

void regToPy();
inline void regToPy(ffpython_t& t_ffpython)
{
    //t_ffpython.reg_class<ScreenIO>("ScreenIO")
    //	.reg(&ScreenIO::onRecieve, "onRecieve")
    //	.reg(&ScreenIO::start, "start")
    //	.reg(&ScreenIO::start, "stop")
    //	.reg_property(&ScreenIO::_ffpython, "t_ffpython")
    //	.reg_property(&ScreenIO::_pobj, "_pobj");

    //t_ffpython.init("ScreenIO_py");
}



class ScreenIO
{
public:
	ScreenIO()
	{
		Py_Initialize();
		ffpython_t::add_path("./");
	}

	~ScreenIO()
	{
		Py_Finalize();
	}



	void start()
	{
		//_pobj = _ffpython.call<PyObject*>("test_screen_IO", "getPyObj");
		//_ffpython.obj_call(_pobj, "regCallBackObj", this);
	}

	void stop()
	{

	}
	void onRecieve(string t_data)
	{

	}


public:
	ffpython_t _ffpython;
	PyObject*  _pobj;

#pragma region MAIN
public:
	static void main()
	{
		ScreenIO i_this;
		regToPy(i_this._ffpython);



	}

#pragma endregion MAIN

};
