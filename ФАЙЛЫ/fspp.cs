using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace CSharp_Shell
{

    public static class Program 
    {
        public static void Main() 
        {
           string a = Console.ReadLine();
           if (a.Contains("print(<")) {
           	   for (int i = 7; i < a.Length; i++ ) {
           	   	   if (a[i] != '>') {
           	   	   	   if (a[i] != ')') {
                           Console.Write(a[i]);
           	   	       }
           	   	   }
           	   }
           }
        }
    }
}
