import io
import sys

output = io.StringIO()
sys.stdout = output

print('hello')
print('world')
print('hi')
sys.stdout = sys.__stdout__

t = output.getvalue()
print(t)


