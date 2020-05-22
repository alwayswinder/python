import tkinter as tk
    
    
class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.test_there = tk.Button(frame, text='测试', command=self.test_click)
        self.test_there.pack(side=tk.TOP)
        
    def test_click(self):
        print('test ok')

        
        
root = tk.Tk()
app = App(root)
root.mainloop()
   
 
