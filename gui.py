import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class gui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Markdown to Document Converter")
        self.geometry("400x300")

        # Markdown file selection
        self.md_file_label = tk.Label(self, text="Select Markdown File:")
        self.md_file_label.pack()
        self.md_file_path = tk.Entry(self, width=50)
        self.md_file_path.pack()
        self.md_file_button = tk.Button(self, text="Browse", command=self.browse_md_file)
        self.md_file_button.pack()

        # Style selection
        self.style_label = tk.Label(self, text="CSS Style File:")
        self.style_label.pack()
        self.style_path = tk.Entry(self, width=50)
        self.style_path.pack()
        self.style_button = tk.Button(self, text="Browse", command=self.browse_style_file)
        self.style_button.pack()

        # New document name
        self.doc_name_label = tk.Label(self, text="New Document Name:")
        self.doc_name_label.pack()
        self.doc_name_entry = tk.Entry(self, width=50)
        self.doc_name_entry.pack()

        # Document type selection
        self.doc_type_label = tk.Label(self, text="Select Document Type:")
        self.doc_type_label.pack()
        self.doc_type_var = tk.StringVar(value="pdf")
        self.doc_type_pdf = tk.Radiobutton(self, text="PDF", variable=self.doc_type_var, value="pdf")
        self.doc_type_pdf.pack()
        self.doc_type_docx = tk.Radiobutton(self, text="DOCX", variable=self.doc_type_var, value="docx")
        self.doc_type_docx.pack()

        # Convert button
        self.convert_button = tk.Button(self, text="Convert", command=self.convert_md)
        self.convert_button.pack()

    def browse_md_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
        self.md_file_path.insert(0, file_path)

    def browse_style_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSS files", "*.css")])
        self.style_path.insert(0, file_path)

    def convert_md(self):
        md_file = self.md_file_path.get()
        style_file = self.style_path.get()
        new_doc_name = self.doc_name_entry.get()
        doc_type = self.doc_type_var.get()

        if not md_file or not new_doc_name:
            messagebox.showerror("Error", "Please provide the necessary details.")
            return

        output_file = f"{new_doc_name}.{doc_type}"
        command = ["pandoc", md_file, "-o", output_file]

        if style_file:
            command.extend(["--css", style_file])

        try:
            subprocess.run(command, check=True)
            messagebox.showinfo("Success", f"Converted to {output_file} successfully.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Conversion failed: {e}")

if __name__ == "__main__":
    app = gui()
    app.mainloop()
