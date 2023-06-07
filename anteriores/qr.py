import qrcode

img = qrcode.make("https://www.youtube.com/channel/UCyI23fQGTrJE-PmER8qwunQ")

f = open("output.png", "wb")
img.save(f)
f.close()