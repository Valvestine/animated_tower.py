def create_tower():
    tower = [
        "   ||",
        "   ||",
        "___||___",
        "   ||",
        "   ||"
    ]
    return tower

def create_sky(width, height):
    sky = []
    for _ in range(height):
        sky.append(" " * width)
    return sky

def place_tower_in_sky(sky, tower, x, y):
    for i, line in enumerate(tower):
        if 0 <= y + i < len(sky):
            sky[y + i] = sky[y + i][:x] + line + sky[y + i][x + len(line):]
    return sky

def display_sky(sky):
    for line in sky:
        print(line)

# Define the dimensions of the sky
width = 30
height = 10

# Create an empty sky
sky = create_sky(width, height)

# Create a tower
tower = create_tower()

# Place the tower in the sky at a specific position
sky = place_tower_in_sky(sky, tower, x=10, y=5)

# Display the sky with the tower
display_sky(sky)
