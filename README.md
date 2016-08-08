# FindingFilesInCorruptedDataPythonScript
Steps I have followed to complete this project
1. Initially I have used google, youtube to get to know about md5checksum, base64 decoding, how to use hex editor to extract files, python programming. I have downloaded two software’s i.e. Hex editor and python 3.5 which are essential to complete this project

2. I have used Wikipedia to know the file signatures of the different types of files like jpg, pdf, png, gif, xml etc.
For example jpeg has hex file signature as FF D8 FF E0 or FF D8 FF DB
3. I used Hex editor to again check whether the magic numbers are correct or not.
4. I have developed a python code which will decode base64 encoded code, convert it into hex code, search for the magic numbers and then convert hex back to bytes, storing them into different files with their extensions and finally check md5 values match.
5. I found the bonus file i.e. .docx file in hex editor by using the magic numbers of .docx file.
Steps for the way I used my program to complete this assignment
1. I have developed a python program which will do the following steps

1.1 The python program will initially read the corrupted.docx file

1.2 As the corrupted.docx is base64 encoded, I have used a command which will decode that corrupted.docx file and store it in a new file named base64.docx

1.3 Now for this base64.docx file I have used a command which will convert the byte type base decoded file into hex code file and store it in hexconverted.docx

1.4 As per the assignment the order of the files to be extracted is given as jpeg, pdf, gif, png. So I have used magic numbers in order to split the hex code into corresponding file extensions.

1.5 I have used a command to convert hex code back into bytes, then stored this byte data into files by opening them in binary mode i.e. extractedjpg.jpg, extractedpdf.pdf, extractedgif.gif, extractedpng.png respectively.

1.6 Finally I have defined a function called md5_checker which will give output the md5 value of the files.

1.7 I found that the md5 values of the extracted files matched with those given in the assignment details
