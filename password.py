password = 'a123456'
count = 1

while count < 4:
	input_pw = input('請輸入密碼: ')
	if input_pw == password:
		print('登入成功! ')
		break
	else:
		#print('密碼錯誤! 還有', 3 - count, '機會') casting
		print('密碼錯誤! 還有', str(3 - count), '機會')
	count += 1