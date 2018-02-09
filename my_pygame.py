import pygame, random
pygame.init()
canvas_width = 800
canvas_height = 600

screen = pygame.display.set_mode((canvas_width, canvas_height))
myfont = pygame.font.SysFont("monospace", 30)

clock = pygame.time.Clock()
done = False

class Button(object):
    def __init__(self, name, image, xcoor, ycoor, width, height):
        self.name = name
        self.image = image
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.width = width
        self.height = height
    def draw_button(self):
        screen.blit(self.image, (self.xcoor, self.ycoor))
class Bowl:
    def __init__(self, ingredients = []):
        self.ingredients = ingredients
    def __repr__(self):
        return "%s" % self.ingredients
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient.name)
    def empty(self):
        self.ingredients = []
    def generate_order(self, options):
        self.empty()
        order_size = random.randint(3, 5)
        while len(self.ingredients) != order_size:
            randindex = random.randint(1, len(options)) - 1
            if options[randindex].name not in self.ingredients:
                self.add_ingredient(options[randindex])


#All ingredients in game
lettuce_image = pygame.image.load('lettuce.png')
ingredient_y = 300
ingredient_width = 75
ingredient_height = 150
shape = (ingredient_y, ingredient_width, ingredient_height)
lettuce = Button("Lettuce", lettuce_image, 150, *shape)
olives = Button("Kalamata Olives", lettuce_image, 235, *shape)
cheese = Button("Blue Cheese", lettuce_image, 320, *shape)
tomatoes = Button("Cherry Tomatoes", lettuce_image, 405, *shape)
croutons = Button("Croutons", lettuce_image, 490, *shape)
dressing = Button("Dressing", lettuce_image, 575, *shape)

list_of_ingredients = [lettuce, olives, cheese, tomatoes, croutons, dressing]

#Other Buttons
order_up = Button("Order Up", lettuce_image, 300, 500, 200, 75)

bowl_key = Bowl()
bowl_key.generate_order(list_of_ingredients)
print bowl_key
bowl = Bowl()
score = 0
while not done:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos            
            for button in list_of_ingredients:
                if x >= button.xcoor and x <= button.xcoor + button.width and y >= button.ycoor and y <= button.ycoor + button.height:
                    bowl.add_ingredient(button)
                    print bowl
            if x >= order_up.xcoor and x <= order_up.xcoor + order_up.width and y >= order_up.ycoor and y <= order_up.ycoor + order_up.height:
                if bowl.ingredients == bowl_key.ingredients:
                    score += 1
                bowl.empty()
                bowl_key.generate_order(list_of_ingredients)
            
        if event.type == pygame.QUIT:
            done = True
        screen.fill((225, 225, 225))
        
        #draw buttons
        lettuce.draw_button()
        olives.draw_button()
        cheese.draw_button()
        tomatoes.draw_button()
        croutons.draw_button()
        dressing.draw_button()

        order_up.draw_button()
        current_order = ", ".join(bowl_key.ingredients)
        label = myfont.render("%s" % current_order, 1, (0, 0, 0))
        score_label = myfont.render("%s" % score, 2, (0, 0, 0))
        screen.blit(label, (50, 75))
        screen.blit(score_label, (50, 100))

        pygame.display.update()
        clock.tick(60)
        
pygame.quit()