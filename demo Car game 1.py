from ursina import *

class CarGame(Entity):
    def __init__(self):
        super().__init__()
        # Set up the player car
        self.car = Entity(model='cube', color=color.red, scale=(2, 0.5, 4), position=(0, 0.5, 0))
        self.car_speed = 0
        self.car_turn_speed = 80  # Degrees per second

        # Set up the ground
        self.ground = Entity(model='plane', texture='grass', scale=(100, 1, 100), position=(0, 0, 0))
        
        # Set up obstacles
        for x in range(-20, 21, 10):
            Entity(model='cube', color=color.brown, scale=(2, 2, 2), position=(x, 1, random.randint(-50, 50)))
        
        # Set up camera
        self.camera_pivot = Entity(position=(0, 2, -10))
        camera.parent = self.camera_pivot
        camera.position = (0, 5, -20)
        camera.rotation_x = 15

    def update(self):
        # Move the car forward/backward
        self.car_speed += held_keys['w'] * 0.02 - held_keys['s'] * 0.02
        self.car_speed = max(min(self.car_speed, 0.2), -0.1)  # Clamp speed
        
        self.car.position += self.car.forward * self.car_speed

        # Turn the car
        if held_keys['a']:
            self.car.rotation_y += self.car_turn_speed * time.dt
        if held_keys['d']:
            self.car.rotation_y -= self.car_turn_speed * time.dt
        
        # Smooth camera follow
        self.camera_pivot.position = lerp(self.camera_pivot.position, self.car.position + Vec3(0, 2, -10), 4 * time.dt)
        self.camera_pivot.rotation_y = self.car.rotation_y

# Create Ursina app
app = Ursina()
game = CarGame()
app.run()
