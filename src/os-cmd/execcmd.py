# os.popen is depracated => use subprocess 
# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
import subprocess

#--- Example with "dir" (on Windows), dir is not an executable file
# subprocess.call('dir') # FileNotFoundError
subprocess.call('dir', shell=True)  # OK output is printed in the console 



# To store output to the output variable : 
p = subprocess.Popen('set', stdout=subprocess.PIPE, shell=True) # Use a "pipe"
output, err = p.communicate()
print( 'Command output is : ' )
print( output ) # output is a string with '\r\n' as line separator  

p = subprocess.Popen(['dir', '/a'], stdout=subprocess.PIPE, shell=True) # Use a "pipe"
output, err = p.communicate()
print( 'Command output is : ' )
print( output ) # output is a string with '\r\n' as line separator  


# output starts with a 'b' (mean byte litteral )
# see : https://stackoverflow.com/questions/2592764/what-does-a-b-prefix-before-a-python-string-mean
print( '-----' )
print( 'Command output is : ' )
# print( str(output, 'UTF-8') ) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x82 in position 52: invalid start byte
print( str(output, 'cp437') ) # The windows terminal uses legacy code pages for DOS : "cp437"

