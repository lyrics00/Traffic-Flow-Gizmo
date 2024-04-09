import pygame

class Lane(pygame.sprite.Sprite):
    def __init__(self, lane_number, y_position, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 100, 100))  # Gray color for the lane
        self.rect = self.image.get_rect(topleft=(0, y_position))
        self.lane_number = lane_number

# Define the Road class
class Road(pygame.sprite.Sprite):
    def __init__(self, num_lanes, lane_width, lane_height):
        super().__init__()
        self.image = pygame.Surface((800, num_lanes * lane_height))
        self.image.fill((200, 200, 200))  # Light gray color for the road background
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.num_lanes = num_lanes
        self.lane_width = lane_width
        self.lane_height = lane_height
        self.lanes = self.create_lanes()

    def create_lanes(self):
        lanes = pygame.sprite.Group()
        for i in range(self.num_lanes):
            lane = Lane(i, i * self.lane_height, self.lane_width, self.lane_height)
            lanes.add(lane)
        return lanes