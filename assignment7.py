#21) r'[A-Z]\w*\sNakamoto'
import re
def regstrip(text,x="\s"):
	text = re.sub("^"+x+"*","",text)
	text = re.sub(x+"*$","",text)
	return text
