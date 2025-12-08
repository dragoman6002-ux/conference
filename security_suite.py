import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import subprocess
import threading
import os
import json
import sys
from pathlib import Path

class SecuritySuiteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Suite - AI Defense System")
        self.root.geometry("1000x700")
        
        self.create_menu()
        self.create_main_frame()
        self.create_status_bar()
        
        self.running_processes = {}
        
        self.load_config()
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Log File", command=self.open_log_file)
        file_menu.add_command(label="Save Output", command=self.save_output)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Network Security Analyzer", command=lambda: self.run_tool("network_security_analyzer.py"))
        tools_menu.add_command(label="Infinite Thought", command=lambda: self.run_tool("infinite_thought.py"))
        tools_menu.add_command(label="Unified Defense System", command=lambda: self.run_tool("unified_defense_system.py"))
        tools_menu.add_command(label="Fake Data Generator", command=lambda: self.run_tool("fake_data_generator.py"))
        tools_menu.add_command(label="AI Logic Battle System", command=lambda: self.run_tool("ai_logic_battle_system.py"))
        tools_menu.add_command(label="Quantum Honeypot Core", command=lambda: self.run_tool("quantum_honeypot_core.py"))
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        
    def create_main_frame(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        left_frame = ttk.LabelFrame(main_frame, text="Security Tools", padding="10")
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        tools = [
            ("Network Security Analyzer", "Analyze network traffic for threats", "network_security_analyzer.py"),
            ("Infinite Thought", "Generate infinite mathematical possibilities", "infinite_thought.py"),
            ("Unified Defense System", "Comprehensive defense against AI attacks", "unified_defense_system.py"),
            ("Fake Data Generator", "Generate fake data to waste attacker resources", "fake_data_generator.py"),
            ("AI Logic Battle System", "Engage attackers in resource-draining battles", "ai_logic_battle_system.py"),
            ("Quantum Honeypot Core", "Trap AI pattern extractors in computational dead ends", "quantum_honeypot_core.py")
        ]
        
        for name, description, script in tools:
            btn_frame = ttk.Frame(left_frame)
            btn_frame.pack(fill=tk.X, pady=5)
            
            btn = ttk.Button(btn_frame, text=name, command=lambda s=script: self.run_tool(s))
            btn.pack(fill=tk.X)
            
            desc_label = ttk.Label(btn_frame, text=description, font=("TkDefaultFont", 8))
            desc_label.pack(anchor=tk.W, padx=(5, 0))
        
        right_frame = ttk.LabelFrame(main_frame, text="Output", padding="10")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.output_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=80, height=30)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        control_frame = ttk.Frame(right_frame)
        control_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.stop_btn = ttk.Button(control_frame, text="Stop Current Tool", command=self.stop_tool, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = ttk.Button(control_frame, text="Clear Output", command=self.clear_output)
        clear_btn.pack(side=tk.LEFT)
        
    def create_status_bar(self):
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def run_tool(self, script_name):
        if script_name in self.running_processes:
            messagebox.showwarning("Tool Already Running", f"{script_name} is already running.")
            return
            
        self.status_var.set(f"Running {script_name}...")
        self.output_text.insert(tk.END, f"\n{'='*50}\n")
        self.output_text.insert(tk.END, f"Starting {script_name}\n")
        self.output_text.insert(tk.END, f"{'='*50}\n\n")
        self.output_text.see(tk.END)
        
        thread = threading.Thread(target=self._run_tool_thread, args=(script_name,))
        thread.daemon = True
        thread.start()
        
        self.stop_btn.config(state=tk.NORMAL)
        
    def _run_tool_thread(self, script_name):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            script_path = os.path.join(script_dir, script_name)
            
            process = subprocess.Popen(
                [sys.executable, script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )
            
            self.running_processes[script_name] = process
            
            for line in iter(process.stdout.readline, ''):
                self.output_text.insert(tk.END, line)
                self.output_text.see(tk.END)
                self.root.update_idletasks()
            
            process.stdout.close()
            return_code = process.wait()
            
            if return_code == 0:
                self.output_text.insert(tk.END, f"\n{script_name} completed successfully.\n")
            else:
                self.output_text.insert(tk.END, f"\n{script_name} exited with error code {return_code}.\n")
                
            self.output_text.see(tk.END)
            
        except Exception as e:
            self.output_text.insert(tk.END, f"Error running {script_name}: {str(e)}\n")
            self.output_text.see(tk.END)
        finally:
            if script_name in self.running_processes:
                del self.running_processes[script_name]
            
            self.status_var.set("Ready")
            self.stop_btn.config(state=tk.DISABLED)
            
    def stop_tool(self):
        if not self.running_processes:
            return
            
        script_name, process = next(iter(self.running_processes.items()))
        
        try:
            process.terminate()
            self.output_text.insert(tk.END, f"\nStopping {script_name}...\n")
            self.output_text.see(tk.END)
        except Exception as e:
            self.output_text.insert(tk.END, f"Error stopping {script_name}: {str(e)}\n")
            self.output_text.see(tk.END)
            
    def clear_output(self):
        self.output_text.delete(1.0, tk.END)
        
    def open_log_file(self):
        file_path = filedialog.askopenfilename(
            title="Open Log File",
            filetypes=[("Text Files", "*.txt"), ("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, content)
                self.output_text.see(tk.END)
                
                self.status_var.set(f"Opened: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {str(e)}")
                
    def save_output(self):
        content = self.output_text.get(1.0, tk.END)
        
        if not content.strip():
            messagebox.showwarning("Empty Output", "There is no output to save.")
            return
            
        file_path = filedialog.asksaveasfilename(
            title="Save Output",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write(content)
                    
                self.status_var.set(f"Saved: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")
                
    def load_config(self):
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    self.config = json.load(f)
            except:
                self.config = {}
        else:
            self.config = {}
            
    def show_about(self):
        about_text = """Security Suite v1.0

A collection of advanced security tools for protecting against 
AI pattern extraction and other threats.

Tools included:
- Network Security Analyzer
- Infinite Thought
- Unified Defense System
- Fake Data Generator
- AI Logic Battle System
- Quantum Honeypot Core

Created with Python and Tkinter."""
        
        messagebox.showinfo("About Security Suite", about_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = SecuritySuiteApp(root)
    root.mainloop()
