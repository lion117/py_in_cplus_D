using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Runtime.InteropServices;

namespace dlltest
{
    class Program
    {
        static void Main(string[] args)
        {
            string path = "D:\\test\\";
            del_folder_chr(path);
            //sayhi();
            Console.ReadLine();
        }

        [DllImport("dllobj.dll", EntryPoint = "del_folder_chr")]
        public static extern int del_folder_chr(string strpath);

        [DllImport("dllobj.dll", EntryPoint = "del_folder_str")]
        public static extern int del_folder_str(string strpath);

        [DllImport("dllobj.dll", EntryPoint = "sayhi")]
        public static extern void sayhi();

    }
}
