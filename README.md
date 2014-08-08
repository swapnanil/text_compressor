text_compressor
===============

A simple text files compressor written in Python

<b>Requirements</b> 
Python 2.6 or higher

<b>Usage</b>

python text_compressor.py source_dir destination_dir

The above command creates a new directory named <i>destination_dir</i> in the same root directory 
as the directory named <i>source_dir</i> with all text files compressed.


python text_compressor.py filename

The above command compresses the file named named <i>filename</i> and <u>overwrites it</u>


<b>Utilities</b>
text_compressor.py can be used to reduce the size of html, css, xml, javascript etc. files. 
Hosting a website with compressed files significantly increases its speed.

The software can also be used to compress the codes of programs like c, cpp, java (programs where statements 
are separated/terminated with characters like ';')


<b>Common issues</b>
In Windows, if you get the message 
<i>'python' is not recognized as an internal or external command, operable program or batch file</i>,
is because Python is not not added to your environment path.

===========================================================================================================

