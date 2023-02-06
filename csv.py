fnameIn = 'a.csv'
fnameOut = 'a.txt'
with open(fnameIn) as fin, open(fnameOut, 'w') as fout:
    data = fin.read()              
    data = data.replace('\n',',',4)  
    data = data.replace('"', '') 
    print (data)
    
    for x in data.split(','):      
        fout.write(x + '\n')