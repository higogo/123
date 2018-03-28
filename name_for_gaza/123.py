fw=open("product.txt","w")
tsvfw=open("product.tsv","w")
fwr=open("test.txt","w")
fr=open("ABB.txt",'r')
for line in fr.readlines():
	fwr.write(line)
	line=line[:-1]
	for tag in line.split():
		tsvfw.write(tag.replace(u'\xa0', u' ')+"\tproduct\n")	
	fw.write(line.replace(u'\xa0', u' ')+"\n")
fr.close()
fr=open("Emerson.txt",'r')
for line in fr.readlines():
	line=line[:-1]
	fw.write(line.replace(u'\xa0', u' ')+"\n")
fr.close()
fr=open("GE.txt",'r')
for line in fr.readlines():
	line=line[:-1]
	fw.write(line.replace(u'\xa0', u' ')+"\n")
fr.close()
fr=open("Rockwell.txt",'r')
for line in fr.readlines():
	line=line[:-1]
	fw.write(line.replace(u'\xa0', u' ')+"\n")
fr.close()
fr=open("Schneider Electric.txt",'r')
for line in fr.readlines():
	line=line[:-1]
	fw.write(line.replace(u'\xa0', u' ')+"\n")
fr.close()
fr=open("Siemens.txt",'r')
for line in fr.readlines():
	fwr.write(line)
	line=line[:-1]
	for tag in line.split():
		tsvfw.write(tag.replace(u'\xa0', u' ')+"\tproduct\n")	
	tsvfw.write(" \tO\n")
	fw.write(line.replace(u'\xa0', u' ')+"\n")
fr.close()