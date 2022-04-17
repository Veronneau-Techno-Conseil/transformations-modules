// See https://aka.ms/new-console-template for more information
using Python.Runtime;
using System.Linq;
Console.WriteLine("Hello, World!");


var pythonPath = Path.GetFullPath("./python");
var exe = Path.Combine(pythonPath, "python.exe");
//var pythonPath = @"C:\Users\andrea\AppData\Local\Programs\Python\Python37";

//Environment.SetEnvironmentVariable("PATH", $@"{pythonPath};" + Environment.GetEnvironmentVariable("PATH"));
Environment.SetEnvironmentVariable("PYTHONHOME", pythonPath);

Environment.SetEnvironmentVariable("PYTHONPATH", $@"{pythonPath};{pythonPath}\python39.zip;{pythonPath}\Lib;{pythonPath}\Lib\site-packages;", EnvironmentVariableTarget.Process);
//Environment.SetEnvironmentVariable("PYTHONPATH ", $@"{pythonPath}");
Environment.SetEnvironmentVariable("PYTHONPATH", $@"{pythonPath};{pythonPath}\python39.zip;{pythonPath}\Lib;{pythonPath}\Lib\site-packages;", EnvironmentVariableTarget.Process);
Console.WriteLine(Environment.GetEnvironmentVariable("PYTHONPATH", EnvironmentVariableTarget.Process));

string setup = @"
if missing:
    subprocess.check_call(' '.join([r'" + exe.ToString() + "', '-m', 'pip', 'install', *missing]))";

PythonEngine.PythonHome = Environment.GetEnvironmentVariable("PYTHONHOME", EnvironmentVariableTarget.Process);
PythonEngine.PythonPath = Environment.GetEnvironmentVariable("PYTHONPATH", EnvironmentVariableTarget.Process);
//PythonEngine.ProgramName = exe;

using (Py.GIL())
{
    
    using (PyScope scope = Py.CreateScope())
    {
        dynamic sys = Py.Import("sys");
        dynamic subprocess = Py.Import("subprocess");
        dynamic pkg_resources = Py.Import("pkg_resources");
        dynamic json = Py.Import("json");
        
        scope.Set("pkg_resources", pkg_resources);
        scope.Set("subprocess", subprocess);
        scope.Set("json", json);


        scope.Exec(@"required = {'numpy','matplotlib','pandas'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = list(required - installed)");
        
        scope.Exec(setup);

        dynamic pd = Py.Import("pandas");
        scope.Set("pd", pd);
        dynamic np = Py.Import("numpy");
        scope.Set("np", np);

        Console.WriteLine(pd.Series(scope.Eval("[1, 3, 5, np.nan, 6, 8]")));

        Console.WriteLine(np.cos(np.pi * 2));

        dynamic sin = np.sin;
        Console.WriteLine(sin(5));

        double c = np.cos(5) + sin(5);
        Console.WriteLine(c);

        dynamic a = np.array(new List<float> { 1, 2, 3 });
        Console.WriteLine(a.dtype);

        dynamic b = np.array(new List<float> { 6, 5, 4 }, dtype: np.int32);
        Console.WriteLine(b.dtype);

        Console.WriteLine(a * b);
    }

    
}

Console.WriteLine("Press any key to continue...");
Console.ReadLine();