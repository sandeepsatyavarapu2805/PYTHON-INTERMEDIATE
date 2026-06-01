import subprocess

command1 = ['cmd', '/c', 'dir /o:g'] # /b gives bare names and /o:g sorts according to the name
result = subprocess.run(command1, capture_output=True, text=True)
# the text=True changes text into readable str and is used when capture_output because the variable captures output into  b'' - bytes literal
# you can also use .decode() in print so 
print(result.stdout)

command2 = 'dir /b /o:g' # /b gives bare names and /o:g sorts according to the name
subprocess.run(command2, shell=True) # without capture_output it does not store anything in a variable to run and shell internally does 'cmd /c'
# shell=True works like 'cmd' in command and if command contains it no need to write it again, use shell only when the input is set by you to avoid problems

# so you can write these outputs into a file with stdout attribute in subprocess.run()
# so we can use returncode for knowing if the run got an error(numbers other than 0) and no error(0)
# we use stderr for returning the error we got for this alternatively ' check=True is used '

# grp and -n are used in commands along with a word to search which takes imput=(retrn of previous subprocess.stdout)