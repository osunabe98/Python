import pywhatkit

try:
	pywhatkit.sendwhatmsg("+34667578285", "He hecho un programa que puedo enviar un mensaje a quien sea a una hora programada, este habre whatsapp web y despues lo envia",13,24)
	print("Successfully Sent!")
except:
	print("An Unexpected Error!")