import base64
import binascii
import hashlib

#opening the given file
f=open("corrupted.docx","r")

#opening a file to store base64 decoded data
f1=open("base64.docx","w")
#opening a file to store hex code of the give file
f2=open("hexconverted.docx","w")
#opening files to store the extracted files
f3=open("extractedjpg.jpg","wb")
f4=open("extractedpdf.pdf","wb")
f5=open("extractedgif.gif","wb")
f6=open("extractedpng.png","wb")

#decoding base64 encoded file f and storing the data in f1
base64_decoded_data = (base64.standard_b64decode(f.read()))
j= str(base64_decoded_data)
f1.write(j)

#hex conversion of base64 decoded file f1 and storing the data in f2
hex_converted_data = binascii.hexlify(base64_decoded_data)
k = str(hex_converted_data)
f2.write(k)


#jpeg file extraction
#using the magic numbers to find first file i.e. jpg file by string manipulations
j1 = k.split('ffd8')
j11= j1[1]
j12= j11.split('ffd9')
jpg_data= j12[0]
jpg_data= 'ffd8'+ jpg_data + 'ffd9'

#converting the hex file back to bytes
byte_converted_jpg =(binascii.unhexlify(jpg_data))

#writing the data into a jpg file
f3.write(byte_converted_jpg)


#pdf file extraction
#using the magic numbers to find first file i.e. pdf file by string manipulations
p1 = k.split('255044')
p11= p1[1]
p12= p11.split('4f460a')
pdf_data= p12[0]
pdf_data= '255044'+ pdf_data + '4f460a'

#converting the hex file back to bytes
byte_converted_pdf = (binascii.unhexlify(pdf_data))

#writing the data into a pdf file
f4.write(byte_converted_pdf)


#gif file extraction
#using the magic numbers to find first file i.e. gif file by string manipulations
g1 = k.split('474946')
g11= g1[1]
g12= g11.split('5a00003b')
gif_data= g12[0]
gif_data= '474946'+ gif_data + '5a00003b'

#converting the hex file back to bytes
byte_converted_gif = (binascii.unhexlify(gif_data))

#writing the data into a gif file
f5.write(byte_converted_gif)


#png file extraction
#using the magic numbers to find first file i.e. png file by string manipulations
p1 = k.split('89504e')
p11= p1[1]
p12= p11.split('ae426082')
png_data= p12[0]
png_data= '89504e'+ png_data + 'ae426082'

#converting the hex file back to bytes
byte_converted_png = (binascii.unhexlify(png_data))

#writing the data into a  file
f6.write(byte_converted_png)



#md5 value finding code(function)
def md5_checker(x):
    y=open(x,"rb")
    md5_finding_function = hashlib.md5()
    ym = y.read()
    md5_finding_function.update(ym)
    print(md5_finding_function.hexdigest()+'\t It is md5 value for \t' + x)
md5_checker("corrupted.docx")
md5_checker("extractedjpg.jpg")
md5_checker("extractedpdf.pdf")
md5_checker("extractedgif.gif")
md5_checker("extractedpng.png")
