import pygame
import os

def get_music_files(folder_path):
    music_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp3"):
                music_files.append(os.path.join(root, file))
    return music_files

def print_song_list(music_files):
    print("Available songs:")
    for idx, file in enumerate(music_files, 1):
        print(f"{idx}. {os.path.basename(file)}")

def play_song(music_files, index):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(music_files[index])
        pygame.mixer.music.play()

        print(f"Now playing: {os.path.basename(music_files[index])}")

        while pygame.mixer.music.get_busy():
            pass  # Wait for the song to finish playing
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\nMusic stopped.")

def main():
    music_folder = "music"  # Replace this with the path to your music folder

    music_files = get_music_files(music_folder)

    if not music_files:
        print("No music files found in the specified folder.")
        return

    print_song_list(music_files)

    while True:
        try:
            choice = int(input("Enter the number of the song you want to play (0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(music_files):
                play_song(music_files, choice - 1)
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()