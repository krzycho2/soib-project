using NUnit.Framework;
using Soib_dotnet;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Soib_dotnet.Tests
{
    [TestFixture()]
    public class PythonExecTests
    {
        [Test()]
        public void ExecuteTest()
        {
            var pythonExe = new PythonExec();
            string output = pythonExe.Execute();
            Console.Write(output);
        }
    }
}