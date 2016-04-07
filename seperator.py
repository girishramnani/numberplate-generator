from PIL import ImageFont, Image, ImageDraw

__author__ = 'Girish'
import string
import os
import sys
import glob
import random

LOCATION="C:\Windows\Fonts"
MAXL = 2000
SIZE=128
STATE_MAX_CITY ={'GJ':[2,6],'MH':[1,5]}
FORMAT=".png"

def generate_list(location):
  """generates the list of all the fonts in the windows environment """
  for i in glob.glob(os.path.join(location,"*.TTF")):
    yield os.path.join(location,i)

def randomizer():
  lis=[]
  for i in glob.glob(os.path.join(LOCATION,"*.TTF")):
    lis.append(i.split(".")[0].split("\\")[-1])
  def work():
    return random.choice(lis)
  return work


get_random_file = randomizer()

# use a truetype font
def main():
  loc = LOCATION #speed
  for font_file in generate_list(loc):
    print("generation "+font_file)
    dirname = font_file.rsplit(".")[-2].split("\\")[-1]
    if not os.path.isdir(dirname):
      os.mkdir(dirname)
    font = ImageFont.truetype(font_file, SIZE)
    im = Image.new("RGBA", (SIZE, SIZE))
    draw = ImageDraw.Draw(im)
    for code in range(ord('A'), ord('Z') + 1):
      w, h = draw.textsize(chr(code), font=font)
      im = Image.new("RGBA", (w, h))
      draw = ImageDraw.Draw(im)
      draw.text((-2, 0), chr(code), font=font, fill="#000000")
      im.save(os.path.join(dirname,chr(code) + FORMAT))
    for code in range(ord('0'), ord('9') + 1):
      w, h = draw.textsize(chr(code), font=font)
      im = Image.new("RGBA", (w, h))
      draw = ImageDraw.Draw(im)
      draw.text((-2, 0), chr(code), font=font, fill="#000000")
      im.save(os.path.relpath(os.path.join(dirname,chr(code) + FORMAT)))


def get_random_alphabet():
  return random.choice(string.ascii_uppercase)


def get_random_state():
  li = ['GJ','MH']
  state = random.choice(li)
  return state

def get_n_random(n,li=None):
  for i in range(n):
    if li ==None:
      yield str(random.choice(range(10)))
    else:
      yield str(random.choice(range(li[i])))



def get_random():
  li=[]
  state =get_random_state()
  li.extend(list(state))
  li.append(" ")
  li.extend(get_n_random(2,STATE_MAX_CITY[state]))
  li.extend(" ")
  li.extend( get_random_alphabet() for _ in range(2))
  li.extend(" ")
  li.extend(get_n_random(4))
  return li




def generate_numplate(font):
  new_im = Image.new('RGBA', ((118*13),SIZE))
  each_plate = get_random()
  for i in range(13):
    char = each_plate[i]
    if char ==" ":
      continue
    im =Image.open(os.path.join(font,str(char)+".png"),"r")
    new_im.paste(im,(i*(118),0))

  new_im.save("".join(each_plate)+".png")

def generate_numplates():
  for i in range(MAXL):
    font ="ARIALNBI"
    generate_numplate(font)


generate_numplates()
