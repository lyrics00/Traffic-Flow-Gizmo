import pygame
class Lane(pygame.sprite.Sprite):
    def __init__(self, lane_number: int, x_position: int, y_position: int, width: int, height: int, orientation: str, turn_direction='straight',):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.lane_number = lane_number
        self.orientation = orientation
        self.turn_direction = turn_direction
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

# Define the Road class
class Road(pygame.sprite.Sprite):
    def __init__(self, num_lanes: int, lane_height: int, lane_width: int, road_x_position: int, road_y_position: int, lane_directions: list[str], orientation: str):
        super().__init__()
        # Light gray color for the road background
        self.num_lanes = num_lanes
        self.lane_height = lane_height
        self.lane_width = lane_width
        self.road_x_position = road_x_position
        self.road_y_position = road_y_position
        self.lane_directions = lane_directions
        self.orientation = orientation  # Angle in degrees for the road's direction
        self.lanes = self.create_lanes()
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
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, (i * self.lane_width) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, (i * self.lane_width) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, turn_direction="straight")
                    lanes.add(lane)
            elif self.orientation == 'right':
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, self.road_x_position, (i * self.lane_height) + self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, self.road_x_position, (i * self.lane_height) + self.road_y_position, self.lane_width, self.lane_height, self.orientation, turn_direction="straight")
                    lanes.add(lane)
            elif self.orientation == 'down':
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, -(i * self.lane_width) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, -(i * self.lane_width) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, turn_direction="straight")
                    lanes.add(lane)
            elif self.orientation == 'left':
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, self.road_x_position, -(i * self.lane_height) + self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, self.road_x_position, -(i * self.lane_height) + self.road_y_position, self.lane_width, self.lane_height, self.orientation, turn_direction='straight')
                    lanes.add(lane)
        return lanes
class Intersection:
    def __init__(self):
        self.roads = [] 
    def add_road(self, road: Road):
        self.roads.append(road)

    def remove_road(self, road: Road):
        self.roads.remove(road)