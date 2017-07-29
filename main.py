# -*- coding: utf-8 -*-

import numpy as np
import cv2

H, S, V = 0, 1, 2

def main():
	img = cv2.imread('./output/cam-bad.png', cv2.IMREAD_UNCHANGED)
	detect_damage(img)

# show image format (basically a 3-d array of pixel color info, in BGR format)
def detect_damage(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  pm = { 'sx': 80, 'sy': 430, 'ex': 150, 'ey': 500 }
  pe = { 'sx': 220, 'sy': 550, 'ex': 280, 'ey': 700 }

  pmx = np.average(img[pm['sy']:pm['ey'], pm['sx']:pm['ex']], axis=(0, 1))
  pex = np.average(img[pe['sy']:pe['ey'], pe['sx']:pe['ex']], axis=(0, 1))

  pxm = img[pm['sy'], pm['sx']]
  pxe = img[pe['sy'], pe['sx']]

  cv2.rectangle(img, (pm['sx'], pm['sy']), (pm['ex'], pm['ey']), (0, 0, 255), 4)
  cv2.rectangle(img, (pe['sx'], pe['sy']), (pe['ex'], pe['ey']), (0, 0, 255), 4)
  cv2.imwrite("output/cam-bad-ck.png", img)

  # damage logic
  v_th = 30
  pm_vhigh = pmx[H] > v_th
  pe_vhigh = pex[H] > v_th

  s_th = 140
  pm_shigh = pmx[S] > s_th
  pe_shigh = pex[S] > s_th

  hd_th = 60
  hdhigh = abs(pmx[H] - pex[H]) > 60

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

  if all([pm_vhigh, pe_vhigh, pm_shigh, pe_shigh, hdhigh]):
  	print("-----------------")
  	print("> IS DAMAGE!!!! <")
  	print("-----------------")
  else:
  	print("OK")

if __name__ == '__main__':
	main()
