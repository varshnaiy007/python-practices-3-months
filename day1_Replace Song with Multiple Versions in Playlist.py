# Write your code here

playlist = ["Song A", "Song B", "Song D"]
versions = ["Song B - Acoustic", "Song B - Remix"]

index = playlist.index("Song B")
result = playlist[:index] + versions + playlist[index + 1:]
print(result)  # ['Song A', 'Song B - Acoustic', 'Song B - Remix', 'Song D']
