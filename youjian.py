
import tkinter
 
win = tkinter.Tk()
win.title("Kahn Software v1")    # #窗口标题
win.geometry("500x300+200+20")   # #窗口位置500后面是字母x
def mayclick():
    print('haha') 
'''
鼠标右键菜单
'''
menubar = tkinter.Menu(win)    # #创建菜单条
xMenu = tkinter.Menu(menubar, tearoff=False)      # #创建子菜单
for item in ["子菜单1", "子菜单2", "子菜单3", "子菜单4", "子菜单5"]:
    xMenu.add_command(label=item, command = mayclick)
menubar.add_cascade(label="右键总菜单1", menu=xMenu)      # #创建总菜单，将子菜单绑定进来
 
def xShowMenu(event):
    xMenu.post(event.x_root, event.y_root)   # #将菜单条绑定上事件，坐标为x和y的root位置
 
win.bind("<Button-3>", xShowMenu)     # #设定鼠标右键触发事件，调用xShowMenu方法
 
win.mainloop()
