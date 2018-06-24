# writing to text file
outfile = open('output.txt','at')
#print(type(outfile))
outfile.write('Aditya Kansal')
outfile.write('lives in Modinagar')
outfile.close()

infile = open('output.txt','rt')
print(infile.read())
infile.close()
