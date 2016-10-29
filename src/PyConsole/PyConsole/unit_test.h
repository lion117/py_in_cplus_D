#pragma once
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <memory>

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
        string i_current_dir = i_interpretor.call<string>("test_interface", "getCurrentDir");
        string i_working_dir = i_interpretor.call<string>("test_interface", "getWorkingDir");
        cout << i_current_dir << endl;
        cout << i_working_dir << endl;

        //i_interpretor.call<void>("PycZipperPrototype", "simpleZip");


#ifdef _PKG
        i_interpretor.call<void>("Py2CplusZipper", "beginPackagePy", i_working_dir);
#endif // _PKG

    }
    catch (exception & ex)
    {
        cout << ex.what() << endl;
    }
    Py_Finalize();
}


class TestClass
{
public:
    TestClass()
    {
        Py_Initialize();
        ffpython_t::add_path("./");
        _py_interpretor = new ffpython_t();


        cout << "py class init " << endl;
    }

    ~TestClass()
    {
        if (_py_interpretor != nullptr)
        {
            delete _py_interpretor;
            _py_interpretor = nullptr;
        }
        Py_Finalize();
        cout << "py class finalize " << endl;

    }

    void printCurrentDir()
    {
        try
        {
            _py_interpretor->call<void>("test_interface", "add", 99, 1);
            string i_current_dir = _py_interpretor->call<string>("test_interface", "getCurrentDir");
            string i_working_dir = _py_interpretor->call<string>("test_interface", "getWorkingDir");
            cout << i_current_dir << endl;
            cout << i_working_dir << endl;
        }
        catch (exception & ex)
        {
            cout << ex.what() << endl;

        }
    }


    void TestObjCall()
    {
        try
        {
            PyObject * i_ptr_obj = _py_interpretor->call<PyObject*>("test_interface", "getObjClass");
            _py_interpretor->obj_call<void>(i_ptr_obj, "whoAmI");
            cout << "add algorithm:  " << _py_interpretor->obj_call<int>(i_ptr_obj, "add", 23, 56) << endl;
            cout << "get time::  " << _py_interpretor->obj_call<string>(i_ptr_obj, "getCurrentTime") << endl;
            Py_XDECREF(i_ptr_obj);
        }
        catch (exception & ex)
        {
            cout << ex.what() << endl;
        }

    }


private:
    ffpython_t *  _py_interpretor;


#pragma region MAIN
public:
    static void main()
    {

        TestClass i_this;
        //i_this.printCurrentDir();
        i_this.TestObjCall();
    }
#pragma endregion MAIN

};





