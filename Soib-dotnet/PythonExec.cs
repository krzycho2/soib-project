using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Soib_dotnet
{
    public class PythonExec
    {
        public string Execute(string command)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = "python";
            string scriptPath = @"D:\Dokumenty\Programowanie\Repos\soib-project\main.py";
            start.Arguments = string.Format("{0} {1}", scriptPath, command);
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            string result = "";
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    result = reader.ReadToEnd();
                    Console.Write(result);
                }
            }
            return result;
        }
    }
}
