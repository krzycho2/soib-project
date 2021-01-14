using NUnit.Framework;
using Soib_dotnet;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.Json;

namespace Soib_dotnet.Tests
{
    [TestFixture()]
    public class CalcTests
    {
        [Test()]
        public void CalcBERTest()
        {
            double mer = 12;
            int qamOrder = 16;
            var pythonExec = new PythonExec();
            string command = $"calc_ber -m {mer} -o {qamOrder}";
            string output = pythonExec.Execute(command);
            output = output.Substring(0, output.Length - 2);
            output = output.Replace("\'", "\"");
            var values = JsonSerializer.Deserialize<Dictionary<string, double>>(output);
            Console.WriteLine($"ber: {values["ber"]}, error: {values["error"]}");
        }
    }
}