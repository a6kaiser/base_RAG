import tkinter as tk
from tkinter import filedialog, messagebox

def load_file(corpus_input):
    filepath = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    if filepath:
        with open(filepath, 'r') as f:
            corpus_input.delete(1.0, tk.END)
            corpus_input.insert(tk.END, f.read())

def run_rag_method(generated_text):
    # Placeholder function to demonstrate functionality
    messagebox.showinfo("Run RAG", "RAG method would be run here and result displayed in the 'generated_text' widget.")

def run_visualization():
    # Placeholder function for visualization
    messagebox.showinfo("Visualization", "Visualization logic would go here.")

def update_ui(selection, corpus_frame, query_frame, generation_frame, visualization_button, methods):
    method_config = methods[selection]
    corpus_frame.pack_forget()
    query_frame.pack_forget()
    generation_frame.pack_forget()
    visualization_button.pack_forget()

    if method_config["corpus"]:
        corpus_frame.pack()
    if method_config["query"]:
        query_frame.pack()
    if method_config["generation"]:
        generation_frame.pack()
    if method_config.get("visualization", False):
        visualization_button.pack()

def main():
    root = tk.Tk()
    root.title("RAG Interface")

    methods = {
        "Method 1": {"corpus": True, "query": True, "generation": True, "visualization": True},
        "Method 2": {"corpus": True, "query": False, "generation": True, "visualization": False},
        "Method 3": {"corpus": False, "query": True, "generation": True, "visualization": True}
    }

    dropdown_frame = tk.Frame(root)
    dropdown_frame.pack(pady=10)
    selected_method = tk.StringVar(root)
    selected_method.set(list(methods.keys())[0])
    dropdown = tk.OptionMenu(dropdown_frame, selected_method, *methods.keys(), command=lambda method=selected_method.get(): update_ui(method, corpus_frame, query_frame, generation_frame, visualization_button, methods))
    dropdown.pack()

    corpus_frame = tk.Frame(root)
    tk.Label(corpus_frame, text="Corpus Input:").pack()
    corpus_input = tk.Text(corpus_frame, height=5, width=50)
    corpus_input.pack()
    upload_button = tk.Button(corpus_frame, text="Upload File", command=lambda: load_file(corpus_input))
    upload_button.pack(pady=5)

    query_frame = tk.Frame(root)
    tk.Label(query_frame, text="Query Input:").pack()
    query_input = tk.Entry(query_frame, width=50)
    query_input.pack()

    generation_frame = tk.Frame(root)
    tk.Label(generation_frame, text="Generated Text:").pack()
    generated_text = tk.Label(generation_frame, text="Output will appear here", wraplength=400)
    generated_text.pack()

    action_frame = tk.Frame(root)
    action_frame.pack(pady=10)
    run_button = tk.Button(action_frame, text="Run RAG", command=lambda: run_rag_method(generated_text))
    run_button.pack(side=tk.LEFT, padx=10)
    visualization_button = tk.Button(action_frame, text="Visualize", command=run_visualization)

    update_ui(selected_method.get(), corpus_frame, query_frame, generation_frame, visualization_button, methods)

    root.mainloop()

if __name__ == "__main__":
    main()
