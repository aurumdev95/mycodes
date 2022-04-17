with open('readme.txt', 'w') as f:
    f.write('readme')
    
#f = open(path_to_file, mode)
#modes
#'w'	Open a text file for writing text
#'a'	Open a text file for appending text


lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
        
lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    f.write('\n'.join(lines))
    
    
more_lines = ['', 'Append text files', 'The End']
with open('readme.txt', 'a') as f:
    f.writelines('\n'.join(more_lines))
    
quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'

with open('quotes.txt', 'w', encoding='utf-8') as f:
    f.write(quote)
    
    
#read
with open('readme.txt') as f:
    lines = f.readlines()
    
Mode	Description
'r'	Open for text file for reading text
'w'	Open a text file for writing text
'a'	Open a text file for appending text

#
with open('the-zen-of-python.txt') as f:
    contents = f.read()
    print(contents)
 
    
###         
            
lines = []
with open('the-zen-of-python.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(f'line {count}: {line}')   
    
    
#readline() to read the text file line by line:

with open('the-zen-of-python.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)