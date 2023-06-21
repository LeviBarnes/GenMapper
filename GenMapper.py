from read_gedcom import read_gedcom
from kmzcreate import create_kmz_file
from kmzcreate import colordict

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import os
import re

def generate_kmz(input_dir, output_file):
    #Find all the .ged files in the directory
    all_files = os.listdir(input_dir)
    gedre = re.compile(".*[.]ged$")
    ged_files = [f for f in all_files if gedre.match(f)]
    all_ind = []
    colorind = 0
    colorlist = list(colordict.values())
    for f in ged_files:
        print("Reading " + f)
        ind = read_gedcom(input_dir + "/" + f)
        color = colorlist[colorind]
        colorind = colorind + 1
        for i in ind:
            i['color']=color
        all_ind = all_ind + ind
    print(all_ind[1000])
    print(all_ind[2000])
    #TODO geo-code locations in all_ind
    #TODO convert dates in all_ind
    #TODO extract important keys from all_ind into kmz_dots
    #TODO call create_kmz_file(kmz_dots)
    print("KMZ output file:", output_file)

def browse_input_dir():
    input_dir = filedialog.askdirectory()
    input_dir_entry.delete(0, tk.END)
    input_dir_entry.insert(tk.END, input_dir)

def browse_output_file():
    output_file = filedialog.asksaveasfilename(defaultextension=".kmz", filetypes=[("KMZ Files", "*.kmz")])
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(tk.END, output_file)

def create_kmz():
    input_dir = input_dir_entry.get()
    output_file = output_file_entry.get()

    if not input_dir or not output_file:
        messagebox.showwarning("Missing Information", "Please specify both input directory and KMZ output file.")
    else:
        generate_kmz(input_dir, output_file)
        messagebox.showinfo("KMZ Created", "KMZ file created successfully.")
if __name__ == "__main__":
   # Create the main window
   window = tk.Tk()
   window.title("KMZ Generator")

   # Input directory
   input_dir_label = tk.Label(window, text="Input directory:")
   input_dir_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

   input_dir_entry = tk.Entry(window, width=50)
   input_dir_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

   input_dir_button = tk.Button(window, text="Browse", command=browse_input_dir)
   input_dir_button.grid(row=0, column=2, padx=10, pady=10)

   # KMZ output file
   output_file_label = tk.Label(window, text="KMZ output:")
   output_file_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

   output_file_entry = tk.Entry(window, width=50)
   output_file_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

   output_file_button = tk.Button(window, text="Browse", command=browse_output_file)
   output_file_button.grid(row=1, column=2, padx=10, pady=10)

   # Create button
   create_button = tk.Button(window, text="Create", command=create_kmz)
   create_button.grid(row=2, column=1, padx=10, pady=10)

   # Run the main event loop
   window.mainloop()
