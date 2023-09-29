from control import shijue0

if __name__ == '__main__':
    a = shijue0.basicImg()
    a.camera(0)
    while True:
        a.get_img()
        a.show_image("test")
        a.delay(100)
