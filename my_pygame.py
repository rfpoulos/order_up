import pygame, random
pygame.init()
canvas_width = 800
canvas_height = 600

screen = pygame.display.set_mode((canvas_width, canvas_height))

clock = pygame.time.Clock()
done = False

class Button(object):
    def __init__(self, xcoor, ycoor, width, height):
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.width = width
        self.height = height
    def draw_button(self):
        pygame.draw.rect(screen, (175, 175, 175), (self.xcoor, self.ycoor, self.width, self.height))

class IngredientButton(Button):
    def __init__(self, name, *args):
        super(IngredientButton, self).__init__(*args)
        self.name = name
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
ingredient_y = 300
ingredient_width = 75
ingredient_height = 150
shape = (ingredient_y, ingredient_width, ingredient_height)
lettuce = IngredientButton("Lettuce", 150, *shape)
olives = IngredientButton("Kalamata Olives", 235, *shape)
cheese = IngredientButton("Blue Cheese", 320, *shape)
tomatoes = IngredientButton("Cherry Tomatoes", 405, *shape)
croutons = IngredientButton("Croutons", 490, *shape)
dressing = IngredientButton("Dressing", 575, *shape)

list_of_ingredients = [lettuce, olives, cheese, tomatoes, croutons, dressing]

#Other Buttons
order_up = Button(300, 500, 200, 75)

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
                print bowl
                print bowl_key
                print score
            
            
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

        pygame.display.update()
        clock.tick(60)
        
pygame.quit()