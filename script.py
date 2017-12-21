import pyautogui, time
time.sleep(2)
check = 0
k = 0
l = 0
while(1):
	im = pyautogui.screenshot()
	for i in range(15):
		if im.getpixel((550-i, 216)) >= (83, 83, 83) and im.getpixel((550-i, 216)) <= (172, 172, 172) and im.getpixel((200, 200)) != im.getpixel((550-i, 216)):
			pyautogui.press('space')
			break
		elif im.getpixel((553-i, 193)) >= (83, 83, 83) and im.getpixel((553-i, 193)) <= (172, 172, 172) and im.getpixel((200, 200)) != im.getpixel((553-i, 193)):
			pyautogui.press('space')
			break
		elif im.getpixel((550-i, 205)) >= (83, 83, 83) and im.getpixel((550-i, 205)) <= (172, 172, 172) and im.getpixel((200, 200)) != im.getpixel((550-i, 205)):
			pyautogui.press('space')
			break
