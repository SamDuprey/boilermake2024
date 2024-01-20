from gtts import gTTS
import os

myText = "AITAH for divorcing my husband for a man who gave me a kidney? I (43F) have a genetic kidney condition and I lost the function of both of my kidneys a couple of years ago. I was on dialysis and on the transplant list. I never drank alcohol or did anything to exacerbate my disease. It’s just luck of the draw."

language = 'en'

# Use 'com' for male voice
output = gTTS(text=myText, lang=language, slow=False, tld='com')

output.save("aitah.mp3")
