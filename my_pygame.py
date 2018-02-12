import pygame, random, time
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
        self.ticks = 0
        self.is_toggle = False

    def is_clicked(self, position):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = position
            if x >= self.xcoor and x <= self.xcoor + self.width and y >= self.ycoor and y <= self.ycoor + self.height:
                return True
            else:
                return False
    def toggle(self):
        if self.is_toggle == False:
            self.is_toggle = True
            self.ticks = pygame.time.get_ticks()
            self.ycoor -= 5

    def draw_button(self):
        toggle_stickiness = 15
        if self.ticks == 0:
            pass
        elif (self.is_toggle == True) and (self.ticks + toggle_stickiness <= pygame.time.get_ticks()):
            self.ycoor += 5
            self.ticks = 0
            self.is_toggle = False

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

def draw_buttons():
    lettuce.draw_button()
    olives.draw_button()
    cheese.draw_button()
    tomatoes.draw_button()
    croutons.draw_button()
    dressing.draw_button()

    order_up.draw_button()

    current_order = ", ".join(bowl_key.ingredients)
    current_bowl = ", ".join(bowl.ingredients)
    key_label = myfont.render("%s" % current_order, 1, (0, 0, 0))
    score_label = myfont.render("%s" % score, 2, (0, 0, 0))
    bowl_label = myfont.render("%s" % current_bowl, 1, (0, 0, 0))
    screen.blit(key_label, (50, 75))
    screen.blit(score_label, (50, 100))
    screen.blit(bowl_label, (50, 125))
    pygame.display.update()

#All ingredients in game
lettuce_image = pygame.image.load('lettuce.png')
olives_image = pygame.image.load('olives.png')
cheese_image = pygame.image.load('cheese.png')
tomatoes_image = pygame.image.load('tomatoes.png')
croutons_image = pygame.image.load('croutons.png')
dressing_image = pygame.image.load('dressing.png')

ingredient_y = 300
ingredient_width = 75
ingredient_height = 150
shape = (ingredient_y, ingredient_width, ingredient_height)
lettuce = Button("Lettuce", lettuce_image, 150, *shape)
olives = Button("Kalamata Olives", olives_image, 235, *shape)
cheese = Button("Blue Cheese", cheese_image, 320, *shape)
tomatoes = Button("Cherry Tomatoes", tomatoes_image, 405, *shape)
croutons = Button("Croutons", croutons_image, 490, *shape)
dressing = Button("Dressing", dressing_image, 575, *shape)

list_of_ingredients = [lettuce, olives, cheese, tomatoes, croutons, dressing]

#Other Buttons
order_up_image = pygame.image.load('orderup.png')
order_up = Button("Order Up", order_up_image, 300, 500, 200, 75)

bowl_key = Bowl()
bowl_key.generate_order(list_of_ingredients)
bowl = Bowl()
score = 0
while not done:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:          
            for button in list_of_ingredients:
                if button.is_clicked(event.pos):
                    bowl.add_ingredient(button)
                    button.toggle()
            
            if order_up.is_clicked(event.pos):
                if bowl_key.ingredients == bowl.ingredients:
                    score += 1
                order_up.toggle()
                bowl.empty()
                bowl_key.generate_order(list_of_ingredients)
            
        if event.type == pygame.QUIT:
            done = True
    screen.fill((225, 225, 225))
        
    draw_buttons()
    clock.tick(60)
        
pygame.quit()