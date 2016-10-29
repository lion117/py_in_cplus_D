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

	void stop(){}
	void onRecieve(string t_data){}

public:
	ffpython_t _ffpython;
	PyObject*  _pobj;



};



class ScreenIOManager
{
public:
    void regToPy(ffpython_t& t_ffpython)
    {
        t_ffpython.reg_class<ScreenIO, void>("ScreenIO")
            .reg(&ScreenIO::onRecieve, "onRecieve")
            .reg(&ScreenIO::start, "start")
            .reg(&ScreenIO::start, "stop")
            .reg_property(&ScreenIO::_ffpython, "t_ffpython")
            .reg_property(&ScreenIO::_pobj, "_pobj");

        t_ffpython.init("ScreenIO_py");
    }

#pragma region MAIN
public:
    static void main()
    {
        ScreenIOManager i_boss;
        ScreenIO i_worker;
        i_boss.regToPy(i_worker._ffpython);


    }
#pragma endregion MAIN


};
