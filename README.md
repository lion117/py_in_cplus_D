# py_in_cplus 项目介绍
> py_in_cplus主要致力于解决python内嵌入C++环境依赖打包问题. 项目基于ffpyton库的情况上实现C++调用python接口, 用python海量的开源库弥补C++缺乏优秀开源库问题, 同时利用python脚本高效的开发效率, 解决涉及网络相关的业务逻辑问题. 

## 功能
- 提供C++调用python函数
- 提供C++调用python类
- 提供C++向python注册类和函数功能
- 提供python自动打包的功能

## 版本兼容
- 支持python2.7 debug和release模式
- python3+ release 模式（尚未测试） 




## 打包发行
- 运行releasePKG之后, 软件将自动生成python27.zip包,需要在重新运行生成release模式下的exe. 这样程序将不再运行打包功能