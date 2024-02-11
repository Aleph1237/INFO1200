import tkinter as tk
  from tkinter import ttk
  class TipCalcFrame(ttk.Frame):
      def __init__(self, parent):
          ttk.Frame.__init__(self, parent, padding="20 20 20 20")
          self.pack()
          self.mealCost = tk.StringVar()
          self.tipPercent = tk.StringVar()
          self.tipAmount = tk.StringVar()
         ttk.Label(self, text="Cost of your meal:").grid(
                      column=0, row=0, sticky=tk.E)
         ttk.Entry(self, width=30, textvariable=self.mealCost).grid(
                      column=1, row=0)
         ttk.Label(self, text="Percent to leave as a tip:").grid(
                      column=0, row=1, sticky=tk.E)
         ttk.Entry(self, width=30, textvariable=self.tipPercent).grid(
                      column=1, row=1)
         ttk.Label(self, text="Tip amount:").grid(
                      column=0, row=2, sticky=tk.E)
         ttk.Entry(self, width=30, textvariable=self.tipAmount,
                      state="readonly").grid(column=1, row=2)
         ttk.Button(self, text="Calculate",
                   command=self.calculate).grid(column=1,row=3, sticky=tk.E)
         for child in self.winfo_children():
             child.grid_configure(padx=5, pady=3)
     def calculate(self):
         mealCost = float(self.mealCost.get())
         tipPercent = float(self.tipPercent.get())
         tipPercent = tipPercent/100
         tip = mealCost * tipPercent
         yourTip = "$" + str(round(tip, 2))
         self.tipAmount.set(yourTip)
 if __name__ == "__main__":
     root = tk.Tk()
     root.title("Tip Calculator")
     TipCalcFrame(root)
     root.mainloop()
