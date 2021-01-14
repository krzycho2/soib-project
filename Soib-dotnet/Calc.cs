using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.Json;

namespace Soib_dotnet
{
    public class Calc
    {
        public Dictionary<string, double> CalcBER(double mer, int qamOrder)
        {
            var pythonExec = new PythonExec();
            string command = $"calc_ber -m {mer} -o {qamOrder}";
            string output = pythonExec.Execute(command);
            output = output.Substring(0, output.Length - 2);
            output = output.Replace("\'", "\"");
            var values = JsonSerializer.Deserialize<Dictionary<string, double>>(output);
            Console.WriteLine($"ber: {values["ber"]}, error: {values["error"]}");
            return values;
        }

        public void MakePlots() 
        {
            var pythonExec = new PythonExec();
            string command = $"plot_all";
            string output = pythonExec.Execute(command);
            Console.WriteLine(output);
        }
    }
}
