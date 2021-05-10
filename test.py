TargetFile = 'C:/PythonProject/Pycub/scripts/test1.txt'

Target = open(TargetFile, 'w', encoding='utf8')

Target.write("testset")

Target.close()

def line_prepender(filename, line):
    with open(TargetFile, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

line_prepender(TargetFile,"top")
