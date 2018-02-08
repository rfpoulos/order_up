import pygame
pygame.init()
canvas_width = 800
canvas_height = 600
screen = pygame.display.set_mode((canvas_width, canvas_height))

clock = pygame.time.Clock()
done = False

class Ingredient:
    def __init__(self, name, xcoor, ycoor):
        self.name = name
        self.xcoor = xcoor
        self.ycoor = ycoor
    def draw_ingredient(self):
        pygame.draw.rect(screen, (175, 175, 175), (self.xcoor, self.ycoor, 75, 150), 0)

class Bowl:
    def __init__(self, ingredients = []):
        self.ingredients = ingredients
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient.name)

lettuce = Ingredient("Lettuce", 50, 400)
olives = Ingredient("Kalamata Olives", 150, 400)
cheese = Ingredient("Blue Cheese", 250, 400)
tomatoes = Ingredient("Cherry Tomatoes", 350, 400)
croutons = Ingredient("Croutons", 450, 400)
dressing = Ingredient("Dressing", 550, 400)
while not done:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
        

        if event.type == pygame.QUIT:
            done = True
        screen.fill((225, 225, 225))
        
        #draw buttons
        lettuce.draw_ingredient()
        olives.draw_ingredient()
        cheese.draw_ingredient()
        tomatoes.draw_ingredient()
        croutons.draw_ingredient()
        dressing.draw_ingredient()

        pygame.display.update()
        clock.tick(60)
        
pygame.quit()