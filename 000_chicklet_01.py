# 000_chicklet_01
# Chicklet visits his friend Rusty the dog

# set up the game board
autotab('board')
board('set_size', 7)
board('clear')

# place all the actors on the board
board('set_tile_image', 0, 0, 'hen_with_chick.jpg')
board('set_tile_image', 0, 6, 'dog_at_home.png')

# wait a few seconds
sleep(3)

# chicklet leaves home
board('set_tile_image', 0, 0, 'hen_right.jpg')
board('set_tile_image', 0, 1, 'chick_right.png')

sleep(1)

# Chicklet walks over to see Rusty
for i in range(1, 5):
    board('move_tile', 0, i, 'right')
    sleep(1)

# Chicklet is talking to Rusty
sleep(3)

# Chicklet turns around
board('set_tile_image', 0, 5, 'chick_left.png')
sleep(2)

# Chicklet walks back to his mother
for i in range(5, 1, -1):
    board('move_tile', 0, i, 'left')
    sleep(1)

# Chicklet says hello to his mother
sleep(2)

# Chicklet is back home with his mother
board('move_tile', 0, 1, 'left')
board('set_tile_image', 0, 0, 'hen_with_chick.jpg')

# end of story
