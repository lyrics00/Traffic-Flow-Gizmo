import pygame
import time
clock = pygame.time.Clock()
class Lane(pygame.sprite.Sprite):
    def __init__(self, lane_number: int, x_position: int, y_position: int, width: int, height: int, orientation: str, restriction_time: float, turn_direction='straight'):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.lane_number = lane_number
        self.orientation = orientation
        self.turn_direction = turn_direction
        self.restriction_time = restriction_time
        self.stopSignLine=0
        self.time = 0
    def updateTimer(self, FPS):
            self.time += clock.tick(FPS)
    def TimeDone(self):
        if self.time >= self.restriction_time:
            self.time = 0
            return True
        return False
    def collidepoint(self, point_x, point_y):
        """
        Check if the given point (point_x, point_y) is within the rectangle defined by this Lane.
        """
        if self.x_position <= point_x <= self.x_position + self.width and self.y_position <= point_y <= self.y_position + self.height:
            return True
        else:
            return False
    def draw_border(self, surface, border_color=(255, 0, 0), border_width=2):
        pygame.draw.rect(surface, border_color, (self.x_position, self.y_position, self.width, self.height), border_width)
    def Delay(self, time_restriction):
        self.elapsed_time = time.time()
        return True

# Define the Road class
class Road(pygame.sprite.Sprite):
    def __init__(self, num_lanes: int, lane_height: int, lane_width: int, road_x_position: int, road_y_position: int, lane_directions: list[str], orientation: str, restriction_time: float, stopSignLine):
        super().__init__()
        # Light gray color for the road background
        self.num_lanes = num_lanes
        self.lane_height = lane_height
        self.lane_width = lane_width
        self.road_x_position = road_x_position
        self.road_y_position = road_y_position
        self.lane_directions = lane_directions
        self.orientation = orientation  # Angle in degrees for the road's direction
        self.restriction_time = restriction_time
        self.lanes = self.create_lanes()
        arrlanes = self.getLanes()
        self.stopSignLine= stopSignLine
        self.time=0
    def getLanes(self):
        lane_sprites = self.lanes.sprites()  # Get a list of Lane sprites from the Group
    # Check if there are any Lane sprites in the list
        if len(lane_sprites) > 0:
            return lane_sprites
        return False

    def create_lanes(self): 
        lanes = pygame.sprite.Group()
        for i in range(self.num_lanes):
            if self.orientation == 'up':
                self.stopSignLine= 700
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, (i * self.lane_width) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.restriction_time, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, (i * self.lane_width) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.restriction_time, turn_direction="straight")
                    lanes.add(lane)
            elif self.orientation == 'right':
                self.stopSignLine=125
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, self.road_x_position, (i * self.lane_height) + self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.restriction_time, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, self.road_x_position, (i * self.lane_height) + self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.restriction_time, turn_direction="straight")
                    lanes.add(lane)
            elif self.orientation == 'down':
                self.stopSignLine=400
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, -(i * self.lane_width) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.restriction_time, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, -(i * self.lane_width) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.restriction_time, turn_direction="straight")
                    lanes.add(lane)
            elif self.orientation == 'left':
                self.stopSignLine=900
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, self.road_x_position, -(i * self.lane_height) + self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.restriction_time, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, self.road_x_position, -(i * self.lane_height) + self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.restriction_time, turn_direction='straight')
                    lanes.add(lane)
        return lanes
class Intersection:
    def __init__(self):
        self.roads = [] 
    def add_road(self, road: Road):
        self.roads.append(road)

    def remove_road(self, road: Road):
        self.roads.remove(road)