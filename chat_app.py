import tkinter as tk
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk
import os

class ChatApplication:
    def __init__(self):
        # Initialize the main application window
        self.root = tk.Tk()
        self.root.title("Chat Bot")
        self.root.geometry("450x400")
        
        # Image paths
        self.user1_image_path = "user1.png"  
        self.user2_image_path = "user2.png"
        self.send_icon_path = "send_icon.png"
        
        # Load images with error handling
        self.user1_image = self.load_image_safe(self.user1_image_path, "👤")
        self.user2_image = self.load_image_safe(self.user2_image_path, "🤖")
        self.send_icon_image = self.load_image_safe(self.send_icon_path, "➤", size=(25, 25))
        
        self.setup_ui()
        
    def load_image_safe(self, image_path, fallback_text, size=(30, 30)):
        """Load image with fallback to text if image doesn't exist"""
        try:
            if os.path.exists(image_path):
                img = Image.open(image_path)
                img = img.resize(size, Image.LANCZOS)
                return ImageTk.PhotoImage(img)
            else:
                # Create a simple colored rectangle as fallback
                img = Image.new('RGB', size, color='lightblue')
                return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Could not load image {image_path}: {e}")
            # Return None to use text fallback
            return None
    
    def setup_ui(self):
        """Set up the user interface"""
        # Frames for chat display and user input
        chat_frame = tk.Frame(self.root)
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollable chat box
        self.chat_box = scrolledtext.ScrolledText(
            chat_frame, 
            wrap=tk.WORD, 
            state='disabled', 
            height=20,
            font=("Arial", 10)
        )
        self.chat_box.pack(fill=tk.BOTH, expand=True)
        
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Entry widget for typing messages
        self.message_entry = tk.Entry(
            input_frame, 
            font=("Arial", 12)
        )
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        # Button to send the message
        self.send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_user_message,
            cursor="hand2",
            bg="lightblue",
            relief="raised"
        )
        
        # Use image if available, otherwise use text
        if self.send_icon_image:
            self.send_button.config(image=self.send_icon_image, compound=tk.LEFT)
            
        self.send_button.pack(side=tk.RIGHT)
        
        # Bind Enter key to send message
        self.message_entry.bind('<Return>', self.on_enter)
        
        # Focus on entry field
        self.message_entry.focus()
        
        # Add welcome message
        self.add_message("Bot", "Welcome to the chat! Type your message and press Enter.", self.user2_image, "bot")
    
    def add_message(self, user, message, user_image, message_type="user"):
        """Add a message to the chat box"""
        self.chat_box.config(state='normal')
        
        # Add some spacing
        self.chat_box.insert(tk.END, "\n")
        
        # Add user image if available
        if user_image:
            self.chat_box.image_create(tk.END, image=user_image)
        else:
            # Fallback to text emoji
            emoji = "👤" if message_type == "user" else "🤖"
            self.chat_box.insert(tk.END, emoji)
        
        # Add message with formatting
        color = "blue" if message_type == "user" else "green"
        self.chat_box.insert(tk.END, f" {user}: ")
        self.chat_box.insert(tk.END, f"{message}\n", message_type)
        
        # Configure text tags for colors
        self.chat_box.tag_config("user", foreground="blue")
        self.chat_box.tag_config("bot", foreground="green")
        
        self.chat_box.config(state='disabled')
        self.chat_box.see(tk.END)  # Scroll to the latest message
    
    def send_user_message(self):
        """Handle sending user message"""
        user_message = self.message_entry.get().strip()
        if user_message:
            # Add user message
            self.add_message("You", user_message, self.user1_image, "user")
            self.message_entry.delete(0, tk.END)
            
            # Simulate bot response (you can replace this with actual bot logic)
            self.simulate_bot_response(user_message)
    
    def simulate_bot_response(self, user_message):
        """Simulate a bot response (replace with actual bot logic)"""
        # Simple echo bot for demonstration
        bot_responses = [
            f"I heard you say: '{user_message}'",
            "That's interesting! Tell me more.",
            "I understand. How can I help you further?",
            "Thanks for sharing that with me!",
            "I'm here to chat. What else would you like to discuss?"
        ]
        
        import random
        response = random.choice(bot_responses)
        
        # Delay the response slightly to make it feel more natural
        self.root.after(1000, lambda: self.add_message("Bot", response, self.user2_image, "bot"))
    
    def on_enter(self, event):
        """Handle Enter key press"""
        self.send_user_message()
        return 'break'  # Prevent default behavior
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    app = ChatApplication()
    app.run()
