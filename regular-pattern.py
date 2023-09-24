def find_greeting(text):
	"""
	Return greeting string ("Hi", "Hello", etc) if greeting pattern matches
	"""
	if text[0]=="H":
		if text[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:
			return text[:2]
		elif text[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:
			return text[:5]
	elif text[0] == 'Y':
		if text[1] == 'o' and text[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:
			return text[:2]
	return None

if __name__=="__main__":
	print(find_greeting("Hi Mr. Yann!"))
	print(find_greeting("Hello, marie"))
	print(find_greeting("Hello"))
	print(find_greeting("hello!"))
	print(find_greeting("Helloworld"))
