from constants import *
from circleshape import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.velocity = pygame.Vector2(0, 0)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # override from parent class
        pygame.draw.polygon(screen, (255,0,0), self.triangle(),2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_cooldown -= dt
        keys = pygame.key.get_pressed()

        self.move(dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and not self.get_speed() >= PLAYER_SPEED_LIMIT:
            self.velocity += forward * PLAYER_SPEED * dt
        elif keys[pygame.K_s] and not self.get_speed() >= PLAYER_SPEED_LIMIT:
            self.velocity -= forward * PLAYER_SPEED * dt

        if self.position.x >= SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x <= 0:
            self.position.x = SCREEN_WIDTH
        
        if self.position.y >= SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y <= 0:
            self.position.y = SCREEN_HEIGHT
                
        self.velocity *= pow(PLAYER_DRAG, dt)        
        self.position += self.velocity * dt

    def get_speed(self):
        return self.velocity.length()

    def shoot(self):
        if self.shot_cooldown > 0:
            return
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

