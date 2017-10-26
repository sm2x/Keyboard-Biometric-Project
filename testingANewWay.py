import win32api
import os
import moduleForCreatingAPassword
#[port, char]
nameDict = dict([(65, 'A'),(66, 'B'),(67, 'C'),(68, 'D'), (69, 'E'), (70, 'F'),(71,'G'), (72,'H'),(73,'I'),(74,'J'),(75,'K'),(76, 'L'),(77, 'M'),
(78,'N'),(79,'O'),(80,'P'),(81,'Q'),(82,'R'),(83,'S'),(84,'T'),(85,'U'),(86,'V'),(87,'W'),(88,'X'),(89,'Y'),(90,'Z'),
(97, 'a'), (98, 'b'),(99,'c'),(100,'d'),(101,'e'),(102,'f'),(103,'g'),(104,'h'),(105,'i'),(106,'j'),(107,'k'),(108,'l'),(109,'m'),
(110,'n'),(111,'o'),(112,'p'),(113,'q'),(114,'r'),(115,'s'),(116,'t'),(117,'u'),(118,'v'),(119,'w'),(120,'x'),(121,'y'),(122,'z'),
(32, ' '), (190,'.'), (13, '\n'),(8, "DELETE"),(16,"SHIFT"),(13, '\n'),(222, "'"),(189,'-'),(191,'?'),(188,','),
(48, '0'),(49, '1'),(50,'2'),(51,'3'),(52,'4'),(53,'5'),(54,'6'),(55,'7'),(56,'8'),(57,'9'),(33,'!')])

#[char, state]
stateDict = dict([('A',-32768),('B',-32768),('C',-32768),('D',-32768),('E',-32768),('F',-32768),('G',-32768),('H',-32768),('I',-32768),('J',-32768),
('K',-32768),('L',-32768),('M',-32768),('N',-32768),('O',-32768),('P',-32768),('Q',-32768),('R',-32768),('S',-32768),('T',-32768),('U',-32768),
('V',-32768),('W',-32768),('X',-32768),('Y',-32768),('Z',-32768),('.', -32768), ('\n', -32768),("DELETE", -32768),
("SHIFT",-32768),('a',-32768),('b', -32768),('c',-32768),('d',-32768),('e',-32768),('f',-32768),('g',-32768),('h',-32768),('i',-32768),('j',-32768),
('k',-32768),('l',-32768),('m',-32768),('n',-32768),('o',-32768),('p',-32768),('q',-32768),('r',-32768),('s',-32768),('t',-32768),('u',-32768),
('v',-32768),('w',-32768),('x',-32768),('y',-32768),('z',-32768),('1',-32768),('2',-32768),('3',-32768),('4',-32768),('5',-32768),(',',-32768),
('6',-32768),('7',-32768),('8',-32768),('9',-32768),('0', -32768),('!',-32768),(' ',-32768),('?', -32768),('\n', -32768),('-',-32768),("'", -32768)])
passageTyped = ""

passage = moduleForCreatingAPassword.Create("Story", 10)
print(passage)
end = True
while end:
	for i in range(0,257):
		try:
			if(win32api.GetAsyncKeyState(i) == stateDict[nameDict[i]]):
				char = nameDict[i]
				if char == "SHIFT":
					pass
					#Uppercase

				if stateDict[char] == 0:#Released
					stateDict[char] = -32768
				else:#Pressed
					os.system('cls')
					if char == '\n':#Enter
						end = False
					if char == "DELETE":#DELETE
						passageTyped = passageTyped[:-1]
					elif i<=57 and i>=48:#NUMBERS
						if stateDict["SHIFT"] == 0:
							passageTyped += nameDict[i-16]
						else:passageTyped += char
					elif char == "SHIFT":#SHIFT
						pass
					elif stateDict["SHIFT"] == 0:#UPPERCASE
						passageTyped += char
					elif char == '.':
						passageTyped+='.'
					else:#lowercase
						try:
							passageTyped += nameDict[i+32]
						except KeyError:
							pass
							passageTyped += nameDict[i]
					print(passage)
					print(passageTyped)
					stateDict[char] = 0
		except KeyError:
			pass
	