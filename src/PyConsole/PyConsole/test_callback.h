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
    IOImpl(int){}
    virtual void onRecieve(string t_data) {};
};

#define  PYCTOR int (*)
#define  PYCVOD void (*)



class ScreenIO : public IOImpl
{
public:
	ScreenIO(int t_data): IOImpl(t_data)
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
        _pobj = _ptr_intepretor->call<PyObject*>("test_IO", "getPyObj");
        _ptr_intepretor->obj_call<void>(_pobj, "regFuc", this);
        _ptr_intepretor->obj_call<void>(_pobj, "start");

	}

#define POC void(*)

    void registToPy()
    {
        _ptr_intepretor->reg_class<ScreenIO, PYCTOR(int) >("IOImpl")
            .reg(&ScreenIO::onRecieve, "onRecieve");
        _ptr_intepretor->init("ScreenIO_py");
    }


	void stop(){}
	void onRecieve(string t_data)
    {
        cout << "C++: " << t_data << endl;
    }

public:
	PyObject*  _pobj;
    ffpython_t * _ptr_intepretor;

#pragma region MAIN
public:
    static void main()
    {
        try
        {
            ScreenIO i_obj(12);
            i_obj.start();
        }
    
        catch (exception & ex)
        {
            cout << ex.what() << endl;
        }


    }

#pragma endregion MAIN

};



