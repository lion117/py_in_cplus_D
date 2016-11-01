#pragma once
#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

#include "FfpyFactory.h"



class IOImpl
{
public:
    virtual void onRecieve(string t_data) {};
};





class ScreenIO : public IOImpl
{
public:
	ScreenIO()
	{
        _ptr_intepretor = new ffpython_t();
        registToPy();
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

#define POC void(*)

    void registToPy()
    {
        _ptr_intepretor->reg_class<IOImpl ,void** >("IOImpl")
            .reg(&IOImpl::onRecieve, "onRecieve");
        _ptr_intepretor->init("ScreenIO_py");
    }


	void stop(){}
	void onRecieve(string t_data){}

public:
	PyObject*  _pobj;
    ffpython_t * _ptr_intepretor;

#pragma region MAIN
public:
    static void main()
    {
        ScreenIO i_obj;


    }

#pragma endregion MAIN

};



