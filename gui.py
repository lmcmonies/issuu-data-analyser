import tkinter as tk
import datamethods as methods
import tasks


def launchGUI():
    # Launch GUI
    root = tk.Tk()
    root.title('Document Tracker')

    # All Tasks For The Coursework
    def tsk2a():
        fName = methods.selectFile()
        tasks.task2a(fName, documentId.get())

    def tsk2b():
        fName = methods.selectFile()
        tasks.task2b(fName, documentId.get())

    def tsk3a():
        fName = methods.selectFile()
        tasks.task3a(fName)

    def tsk3b():
        fName = methods.selectFile()
        tasks.task3b(fName)

    def tsk4():
        fName = methods.selectFile()
        sortedTop10Readers = tasks.task4(fName)
        displayBox.config(text=methods.displayTool("Top 10 Readers \n File: ", fName, sortedTop10Readers))

    def tsk5d():
        fName = methods.selectFile()
        sortedTop10AlsoLikes, docsReadDict = tasks.task5d(documentId.get(), visitorId.get(), fName)
        displayBox.config(text=methods.displayTool("Top 10 Also Likes \n File: ", fName, sortedTop10AlsoLikes))

    def tsk6():
        fName = methods.selectFile()
        tasks.task6(documentId.get(), visitorId.get(), fName)

    # GUI Elements
    canvas = tk.Canvas(root, height=900, width=700, bg='#2d4f54')
    canvas.pack()

    frame = tk.Frame(canvas, bg="white")
    frame.place(relwidth=0.8, relheight=0.85, relx=0.1, rely=0.1)

    # Document Id Entry Box
    documentId = tk.Entry(frame, font=50)
    documentId.insert(0, 'Enter Document Id')
    documentId.pack()

    # Visitor Id Entry Box
    visitorId = tk.Entry(frame, font=50)
    visitorId.insert(0, 'Enter Visitor Id')
    visitorId.pack()

    # Buttons For Tasks
    t2a = tk.Button(frame, text="Task 2a", padx=10, pady=5, bg="#2d4f54", fg="white",
                    command=tsk2a)
    t2a.pack()

    t2b = tk.Button(frame, text="Task 2b", padx=10, pady=5, bg="#2d4f54", fg="white",
                    command=tsk2b)
    t2b.pack()

    t3a = tk.Button(frame, text="Task 3a", padx=10, pady=5, bg="#2d4f54", fg="white",
                    command=tsk3a)
    t3a.pack()

    t3b = tk.Button(frame, text="Task 3b", padx=10, pady=5, bg="#2d4f54", fg="white",
                    command=tsk3b)
    t3b.pack()

    t4 = tk.Button(frame, text="Task 4", padx=10, pady=5, bg="#2d4f54", fg="white",
                   command=tsk4)
    t4.pack()

    t5d = tk.Button(frame, text="Task 5d", padx=10, pady=5, bg="#2d4f54", fg="white",
                    command=tsk5d)
    t5d.pack()

    t6 = tk.Button(frame, text="Task 6", padx=10, pady=5, bg="#2d4f54", fg="white",
                   command=tsk6)
    t6.pack()

    # Box For Displaying Output
    displayBox = tk.Label(frame, text='', height=40, width=50, font=('Times New Roman', 12))

    displayBox.pack(pady=20)

    root.mainloop()
