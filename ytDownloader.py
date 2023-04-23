import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox, filedialog

class YoutubeDownloader:
    def __init__(self, master):
        self.master = master

        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold the content
        content_frame = tk.Frame(self.master)
        content_frame.pack(expand=True, fill="both")

        # Add a spacer at the top of the content frame to center the content vertically
        spacer = tk.Label(content_frame, text="")
        spacer.pack(expand=True)

        # Add the content to the content frame
        self.url_label = tk.Label(content_frame, text="Enter Youtube Video URL:", font=("Arial", 14))
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(content_frame, width=50)
        self.url_entry.pack(pady=10)

        self.download_button = ttk.Button(content_frame, text="Download", command=self.download_video, style='my.TButton')
        self.download_button.pack(pady=10)

        # Add another spacer to center the content vertically
        spacer2 = tk.Label(content_frame, text="")
        spacer2.pack(expand=True)

        # Configure the style for the button
        self.style = ttk.Style()
        self.style.configure('my.TButton', font=("Arial", 9), width=12, height=5, anchor='center')

    def download_video(self):
        video_url = self.url_entry.get()
        youtube = YouTube(video_url)

        try:
            # Get the highest resolution stream
            video = youtube.streams.get_highest_resolution()

            # Open a file dialog box to select the download location
            download_location = filedialog.askdirectory()

            # Download the video
            video.download(download_location, filename="video.mp4")

            # Show a success message box
            messagebox.showinfo("Success", "Video Downloaded Successfully")

        except Exception as e:
            # Show an error message box
            messagebox.showerror("Error", f"Error Occurred: {e}")

root = tk.Tk()
root.title("Youtube Downloader")
root.iconbitmap("YouTubeLogo.ico")
root.geometry("400x200")
root.resizable(width=False, height=False)

# Center the app on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (500 / 2))
y = int((screen_height / 2) - (400 / 2))
root.geometry(f"400x200+{x}+{y}")

# Create a frame to hold the content
frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

downloader = YoutubeDownloader(frame)

root.mainloop()