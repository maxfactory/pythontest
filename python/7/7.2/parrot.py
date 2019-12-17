# prompt = "\nTell me something,and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
# 	message = input(prompt)
# 	if message != 'quit':
# 		print(message)

# 使用标志
prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
action = True
while action:
	message = input(prompt)

	if message == 'quit':
		action = False
	else:
		print(message)