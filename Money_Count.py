import pygame

class MoneyCounter:
    def __init__(self, increment_amount=10, interval=300000):  # 300,000 ms = 5 minutes
        self.money = 50
        self.increment_amount = increment_amount
        self.interval = interval
        self.last_increment_time = pygame.time.get_ticks()

    def update(self):
        """Increment the money if 5 minutes have passed."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_increment_time >= self.interval:
            self.money += self.increment_amount
            self.last_increment_time = current_time

    def draw(self, surface, font):
        """Display the current money on the screen."""
        money_text = font.render(f"Money: ${self.money}", True, (255, 255, 255))
        surface.blit(money_text, (10, 10))