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



class FfpyFactory
{
public:
#pragma region API
    ffpython_t* getFactoryObj(const string & t_objname = "default")
    {
        if (_interpretor_dict.count(t_objname) == 0)
        {
            ffpython_t i_obj;
            _interpretor_dict.insert(pair<string, ffpython_t>(t_objname, i_obj));
        }
        return &_interpretor_dict[t_objname];
    }

    static FfpyFactory* getInstance()
    {
        if (_this_obj == nullptr)
        {
            _this_obj = new FfpyFactory();
        }
        return _this_obj;
    }
#pragma endregion API


private:
    FfpyFactory()
    {
        cout << "init ffpython" << endl;
        Py_Initialize();
        ffpython_t::add_path("./");

    }
    ~FfpyFactory()
    {
        zipPy();
        Py_Finalize();
        if (_this_obj != nullptr)
        {
            delete _this_obj;
        }
        cout << "finalize ffpython" << endl;
    }

    void zipPy(const string & t_destdir = "")
    {
        for (auto& itor : _interpretor_dict)
        {
#ifdef _PKG
            itor.second.call<void>("Py2CplusZipper", "beginPackagePy", t_destdir);
#endif // _PKG
            break;
        }
    }
private:
    map<string,ffpython_t> _interpretor_dict;
    static FfpyFactory*  _this_obj ;
    
};

