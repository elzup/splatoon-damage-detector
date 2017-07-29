# -*- coding: utf-8 -*-

import numpy as np
import cv2
import time
import sys

width = 1280
height = 720

H, S, V = 0, 1, 2

def main():
  # img = cv2.imread('./output/cam-emp.png', cv2.IMREAD_UNCHANGED)
  # detect_damage(img)
  cap = cv2.VideoCapture(1)
  while True:
    ret, img = cap.read()
    detect_damage(img)
    time.sleep(0.1)

def beep():
	sys.stdout.write('\a')
	sys.stdout.flush()

# show image format (basically a 3-d array of pixel color info, in BGR format)
def detect_damage(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  pm = { 'sx': 300, 'sy': 450, 'ex': 1100, 'ey': 650 }
  pe = { 'sx': 0, 'sy': height - 65, 'ex': width - 1, 'ey': height - 1 }

  pmx = np.median(img[pm['sy']:pm['ey'], pm['sx']:pm['ex']], axis=(0, 1))
  pex = np.average(img[pe['sy']:pe['ey'], pe['sx']:pe['ex']], axis=(0, 1))

  pxm = img[pm['sy'], pm['sx']]
  pxe = img[pe['sy'], pe['sx']]

  cv2.rectangle(img, (pm['sx'], pm['sy']), (pm['ex'], pm['ey']), (0, 0, 255), 4)
  cv2.rectangle(img, (pe['sx'], pe['sy']), (pe['ex'], pe['ey']), (0, 0, 255), 4)
  # cv2.imwrite("output/cam-bad-ck.png", img)

  # damage logic
  v_th = 100
  pm_vhigh = pmx[H] > v_th
  pe_vhigh = pex[H] > v_th

  s_th = 50
  pm_shigh = pmx[S] > s_th
  pe_shigh = pex[S] > s_th

  hd_th = 20
  hdhigh = abs(pmx[H] - pex[H]) < hd_th

  print("HSV")
  print(" me   : " + str(pmx))
  print(" enemy: " + str(pex))

  print("V > " + str(v_th))
  print(" me   : " + str(pm_vhigh))
  print(" enemy: " + str(pe_vhigh))

  print("S > " + str(s_th))
  print(" me   : " + str(pm_shigh))
  print(" enemy: " + str(pe_shigh))

  print("H diff > " + str(hd_th))
  print(" v    : " + str(hdhigh))

  # if all([pm_vhigh, pe_vhigh, pm_shigh, pe_shigh, hdhigh]):
  if all([hdhigh, pe_vhigh]):
  	print("-----------------")
  	print("> IS DAMAGE!!!! <")
  	print("-----------------")
  	beep()
  else:
  	print("OK")

if __name__ == '__main__':
  main()
