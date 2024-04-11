import pygame

class Lane(pygame.sprite.Sprite):
    def __init__(self, lane_number, x_position, y_position, width, height, orientation, turn_direction='straight',):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.lane_number = lane_number
        self.orientation = orientation
        self.turn_direction = turn_direction

# Define the Road class
class Road(pygame.sprite.Sprite):
    def __init__(self, num_lanes, lane_height, lane_width, road_x_position, road_y_position, lane_directions, orientation):
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

    def create_lanes(self): 
        lanes = pygame.sprite.Group()
        for i in range(self.num_lanes):
            if self.orientation == 'up':
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, (i * self.lane_height) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, (i * self.lane_height) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, turn_direction="straight")
            elif self.orientation == 'right':
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, self.road_x_position, (i * self.lanewidth) + self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, self.road_x_position, (i * self.lanewidth) + self.road_y_position, self.lane_width, self.lane_height, self.orientation, turn_direction="straight")
            elif self.orientation == 'down':
                if self.lane_directions[i] == 'straight-right' or self.lane_directions[i] == 'right' or self.lane_directions[i] == 'left' or self.lane_directions[i] == 'straight':
                    lane = Lane(i, -(i * self.lane_height) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, self.lane_directions[i])
                    lanes.add(lane)
                else:
                    lane = Lane(i, -(i * self.lane_height) + self.road_x_position, self.road_y_position, self.lane_width, self.lane_height, self.orientation, turn_direction="straight")
        return lanes
    

