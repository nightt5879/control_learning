from control import shijue1

a = None


a=shijue1.Img()
a.camera(0)
a.finger_init()
while  True:
  a.get_img()
  a.finger_detect()
  a.show_image('img')
  a.delay(1)
