import pygame


# init
pygame.init()
isRun = True

# window
windowPanjang = 500
windowLebar = 500
window = pygame.display.set_mode((windowPanjang,windowLebar))


# object game
x = 250
y = 250

panjang = 10
lebar = 10

speed = 5

while isRun:
    # user input
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    # keyboard press
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    
    if keys[pygame.K_RIGHT] and x < windowLebar-lebar:
        x += speed

    if keys[pygame.K_DOWN] and y < windowPanjang-panjang:
        y += speed

    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # bawah

    #update asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,0,0), (x,y,lebar,panjang))

    # render to display
    pygame.display.update()




pygame.quit()

