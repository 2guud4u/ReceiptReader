from PIL import Image
import re
import pytesseract

text = pytesseract.image_to_string(Image.open('shop.png'))
pattern = r'\d{9}'
item_dpci = []
for i, line in enumerate(text.split('\n')):
    
        
        matchh = re.search(pattern, str(line))
        if matchh:
            item_dpci.append(matchh.group(0))

print(item_dpci)


       

