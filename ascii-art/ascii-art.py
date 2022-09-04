# I searched for another ascii art generator since the herokuapp is gone. 
# Unfortunately this request returned the html for the webpage that generates the ascii art
# rather than the art itself...

import requests

r = requests.get(f'https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=Caligraphy&text=Awesomesauce%0A')
print(r.text)  