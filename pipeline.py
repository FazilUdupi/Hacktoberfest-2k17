import pipes

my_template = pipes.Template()

my_template.append('tr a-z A-Z', '--')
my_template.prepend('echo Python Programming', '--') #Prepend the item into queue
my_template.append('rev', '--')
my_template.debug(True)

my_file = my_template.open('test_file', 'w')
my_file.close()

content = open('test_file').read()
print(content)
