version = 0
sysroot = ""
sysroots_dir = ""
parts = []

[Application]
entry_point = "main.py"
is_console = true
is_bundle = true
name = "amigo"
qmake_configuration = ""
script = "main"
syspath = ""

[Application.Package]
name = "E:\\adutor"
exclude = [ "*.pyc", "*.pyd", "*.pyo", "*.pyx", "*.pxi", "__pycache__", "*-info", "EGG_INFO", "*.so",]
[[Application.Package.Content]]
name = "amigo.pro"
included = true
is_directory = false

[[Application.Package.Content]]
name = "Amigo.py"
included = true
is_directory = false

[[Application.Package.Content]]
name = "Amigo.txt"
included = true
is_directory = false

[[Application.Package.Content]]
name = "buildozer.spec"
included = true
is_directory = false

[[Application.Package.Content]]
name = "chatbot.py"
included = true
is_directory = false

[[Application.Package.Content]]
name = "data.txt"
included = true
is_directory = false

[[Application.Package.Content]]
name = "female.py"
included = true
is_directory = false

[[Application.Package.Content]]
name = "google.py"
included = true
is_directory = false

[[Application.Package.Content]]
name = "icon.png"
included = true
is_directory = false

[[Application.Package.Content]]
name = "mail.py"
included = true
is_directory = false

[[Application.Package.Content]]
name = "main.py"
included = true
is_directory = false

[[Application.Package.Content]]
name = "task_schedular.py"
included = true
is_directory = false

[[Application.Package.Content]]
name = "weather.py"
included = true
is_directory = false

[[Application.Package.Content]]
name = "youtube.py"
included = true
is_directory = false

