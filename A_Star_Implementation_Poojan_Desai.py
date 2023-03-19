# IMPORTING NECESSARY LIBRARIES
import numpy as np
from math import dist
import matplotlib.pyplot as plt
import time
import heapq

# DEFINING A NODE CLASS TO STORE NODES AS OBJECTS  
class Node:

    def __init__(self, x, y, theta, cost, parent_id, c2g = 0):
        self.x = x
        self.y = y
        self.theta = theta
        self.cost = cost
        self.parent_id = parent_id
        self.c2g = c2g 
        
        
    def __lt__(self,other):
        return self.cost + self.c2g < other.cost + other.c2g


# DEFINING ACTIONS TO BE PERFORMED  
# CALCULATING COST TO COME FOR ALL ACTIONS  
def move_60up(x,y,theta,step_size, cost):
    theta = theta + 60
    x = x + (step_size*np.cos(np.radians(theta)))
    y = y + (step_size*np.sin(np.radians(theta)))

    x = round(x)
    y = round(y)
    cost = 1 + cost
    return x,y,theta,cost

def move_30up(x,y,theta, step_size, cost):
    theta = theta + 30
    x = x + (step_size*np.cos(np.radians(theta)))
    y = y + (step_size*np.sin(np.radians(theta)))

    x = round(x)
    y = round(y)
    cost = 1 + cost
    return x,y,theta, cost

def move_0(x,y,theta, step_size, cost):
    theta = theta + 0
    x = x + (step_size*np.cos(np.radians(theta)))
    y = y + (step_size*np.sin(np.radians(theta)))

    x = round(x)
    y = round(y)
    cost = 1 + cost
    return x,y,theta, cost

def move_30down(x,y,theta, step_size, cost):
    theta = theta - 30
    x = x + (step_size*np.cos(np.radians(theta)))
    y = y + (step_size*np.sin(np.radians(theta)))

    x = round(x)
    y = round(y)
    cost = 1 + cost
    return x,y,theta, cost

def move_60down(x,y,theta, step_size, cost):
    theta = theta - 60
    x = x + (step_size*np.cos(np.radians(theta)))
    y = y + (step_size*np.sin(np.radians(theta)))

    x = round(x)
    y = round(y)
    cost = 1 + cost
    return x,y,theta,cost


# DEFINING A FUNCTION TO PERFORM ACTIONS THAT ARE DEFINED
def Action_set(move,x,y,theta,step_size,cost):

	if move == 'ext_right':
		return move_60up(x,y,theta, step_size,cost)
	elif move == 'right':
		return move_30up(x,y,theta, step_size,cost)
	elif move == 'straight':
		return move_0(x,y,theta,step_size,cost)
	elif move == 'left':
		return move_30down(x,y,theta,step_size,cost)
	elif move == 'ext_left':
		return move_60down(x,y,theta,step_size,cost)
	else:
		return None


# CONFIGURATION SPACE CONSTRUCTION WITH OBSTACLES  
def obstacle_space(width, height, obstacle_clearence, robot_radius):
    
    # Generating Obstacle Space
    obstacle_space = np.full((height, width),0)
    
    for y in range(0, height) :
        for x in range(0, width):
            
            # Plotting Buffer Space for the Obstacles using Half Plane Equations
            
            # Rectangle 1 Obastacle
            r11_buffer = (x + ( obstacle_clearence + robot_radius)) - 100  
            r12_buffer = (y - ( obstacle_clearence + robot_radius)) - 100
            r13_buffer = (x - ( obstacle_clearence + robot_radius)) - 150
            # r14_buffer = y - 0    # No need to define lower most line at boundry
            
            # Rectangle 2 Obastacle
            r21_buffer = (x + ( obstacle_clearence + robot_radius)) - 100  
            # r22_buffer = y - 250  # No need to define upper most line at boundry
            r23_buffer = (x - ( obstacle_clearence + robot_radius)) - 150
            r24_buffer = (y + ( obstacle_clearence + robot_radius)) - 150 
            
            # Hexagon Obstacle
            h6_buffer = (y + ( obstacle_clearence + robot_radius)) +  0.58*(x + ( obstacle_clearence + robot_radius)) - 223.18
            h5_buffer = (y + ( obstacle_clearence + robot_radius)) - 0.58*(x - ( obstacle_clearence + robot_radius)) + 123.21
            h4_buffer = (x - ( obstacle_clearence + robot_radius)) - 364.95
            h3_buffer = (y - ( obstacle_clearence + robot_radius)) + 0.58*(x - ( obstacle_clearence + robot_radius)) - 373.21
            h2_buffer = (y - ( obstacle_clearence + robot_radius)) - 0.58*(x + ( obstacle_clearence + robot_radius)) - 26.82
            h1_buffer = (x + ( obstacle_clearence + robot_radius)) - 235.040
            
            # Triangle Obstacle
            t1_buffer = (x + ( obstacle_clearence + robot_radius)) - 460
            t2_buffer = (y - ( obstacle_clearence + robot_radius)) + 2*(x - ( obstacle_clearence + robot_radius)) - 1145
            t3_buffer = (y + ( obstacle_clearence + robot_radius)) - 2*(x - ( obstacle_clearence + robot_radius)) + 895
        
            # Setting the line constrain to obatain the obstacle space with buffer
            if((h6_buffer>0 and h5_buffer>0 and h4_buffer<0 and h3_buffer<0 and h2_buffer<0 and h1_buffer>0) or (r11_buffer>0 and r12_buffer<0 and r13_buffer<0) or (r21_buffer>0 and r23_buffer<0 and r24_buffer>0) or (t1_buffer>0 and t2_buffer<0 and t3_buffer>0)):
                obstacle_space[y, x] = 1
             
             
            # Plotting Actual Object Space Half Plane Equations
            
            # Rectangle 1 Obastacle
            r11 = (x) - 100  
            r12 = (y) - 100
            r13 = (x) - 150
            # r14 = y - 0
            
            # Rectangle 2 Obastacle
            r21 = (x) - 100  
            # r22 = (y) - 250
            r23 = (x) - 150
            r24 = (y) - 150 
            
            # Hexagon Obstacle
            h6 = (y) +  0.58*(x) - 223.18
            h5 = (y) - 0.58*(x) + 123.21
            h4 = (x) - 364.95
            h3 = (y) + 0.58*(x) - 373.21
            h2 = (y) - 0.58*(x) - 26.82
            h1 = (x) - 235.04  
            
            # Triangle Obstacle
            t1 = (x) - 460
            t2 = (y) + 2*(x) - 1145
            t3 = (y) - 2*(x) + 895

            # Setting the line constrain to obatain the obstacle space with buffer
            if((h6>0 and h5>0 and h4<0 and h3<0 and h2<0 and h1>0) or (r11>0 and r12<0 and r13<0 ) or (r21>0  and r23<0 and r24>0) or (t1>0 and t2<0 and t3>0)):
                obstacle_space[y, x] = 2    
                
       
    return obstacle_space


# TO SEE IF THE MOVE IS VALID OR NOT 
def ValidMove(x, y, obstacle_space):

	e = obstacle_space.shape

	if( x > e[1] or x < 0 or y > e[0] or y < 0 ):
		return False
	
	else:
		try:
			if(obstacle_space[y][x] == 1  or obstacle_space[y][x] == 2):
				return False
		except:
			pass
	return True


# DEFINING A FUNCTION TO CHECK IF THE PRESENT NODE IS GOAL NODE 
def Check_goal(present, goal):
    
    dt = dist((present.x, present.y), (goal.x, goal.y))             

    if dt < 1.5:
        return True
    else:
        return False


#   TO SEE IF THE OREINTATION IS VALID OR NOT   
def validorient(theta):
    if((theta%30)==0):
        return theta
    else:
        return False
    

# GENERATE UNIQUE KEY  
def key(node):
    key = 1022*node.x + 111*node.y 
    return key


# A STAR ALGORITHM  
def a_star(start,goal,obstacle_space,step_size):                       

    if Check_goal(start, goal):
        return None,1
    goal_node = goal
    start_node = start
    
    moves = ['ext_right','right', 'straight', 'left', 'ext_left']   
    unexplored_nodes = {}  #List of all open nodes
    
    start_key = key(start_node) #Generating a unique key for identifying the node
    unexplored_nodes[(start_key)] = start_node
    
    explored_nodes = {} #List of all closed nodes
    priority_list = []  #List to store all dictionary entries with cost as the sorting variable
    heapq.heappush(priority_list, [start_node.cost, start_node]) #This Data structure will prioritize the node to be explored which has less cost.
    
    all_nodes = [] #stores all nodes that have been traversed, for visualization purposes.
    

    while (len(priority_list) != 0):

        present_node = (heapq.heappop(priority_list))[1]
        all_nodes.append([present_node.x, present_node.y, present_node.theta])          
        present_id = key(present_node)
        if Check_goal(present_node, goal_node):
            goal_node.parent_id = present_node.parent_id
            goal_node.cost = present_node.cost
            print("Goal Node found")
            return all_nodes,1

        if present_id in explored_nodes:  
            continue
        else:
            explored_nodes[present_id] = present_node
		
        del unexplored_nodes[present_id]

        for move in moves:
            x,y,theta,cost = Action_set(move,present_node.x,present_node.y,present_node.theta, step_size, present_node.cost)  ##newaddd
            
            c2g = dist((x, y), (goal.x, goal.y))  
   
            new_node = Node(x,y,theta, cost,present_node, c2g)   
   
            new_node_id = key(new_node) 
   
            if not ValidMove(new_node.x, new_node.y, obstacle_space):
                continue
            elif new_node_id in explored_nodes:
                continue
   
            if new_node_id in unexplored_nodes:
                if new_node.cost < unexplored_nodes[new_node_id].cost: 
                    unexplored_nodes[new_node_id].cost = new_node.cost
                    unexplored_nodes[new_node_id].parent_id = new_node.parent_id
            else:
                unexplored_nodes[new_node_id] = new_node
   			
            heapq.heappush(priority_list, [(new_node.cost + new_node.c2g), new_node]) 
   
    return  all_nodes,0


# BACKTRACK AND GENERATE SHORTEST PATH  
def Backtrack(goal_node):  
    x_path = []
    y_path = []
    x_path.append(goal_node.x)
    y_path.append(goal_node.y)

    parent_node = goal_node.parent_id
    while parent_node != -1:
        x_path.append(parent_node.x)
        y_path.append(parent_node.y)
        parent_node = parent_node.parent_id
        
    x_path.reverse()
    y_path.reverse()
    
    x = np.asarray(x_path)
    y = np.asanyarray(y_path)
    
    return x,y


#  PLOT OBSTACLES SPACE, EXPLORED NODES, SHORTEST PATH   
def plot(start_node,goal_node,x_path,y_path,all_nodes,obstacle_space):
    plt.figure()
    
    # Start node and Goal node # ##
    plt.plot(start_node.x, start_node.y, "Dw")
    plt.plot(goal_node.x, goal_node.y, "Dg")

    # Configuration Space for Obstacles  
    plt.imshow(obstacle_space, "GnBu")
    ax = plt.gca()
    ax.invert_yaxis() #y-axis inversion
    
    # All visited nodes  
    for i in range(len(all_nodes)):
        plt.plot(all_nodes[i][0], all_nodes[i][1], "2g-")
        plt.pause(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)

    # Shortest path found ###
    plt.plot(x_path,y_path, ':r')
    plt.show()
    plt.pause(3)
    plt.close('all')



# CALLING ALL MY FUNCTIONS TO IMPLEMENT A STAR ALGORITHM ON A POINT ROBOT  
if __name__ == '__main__':
    
    # Clearance of the Obstacle  
    # obs_clearance = input("Assign Clearance to the Obstacles: ")
    # obs_clearance = float(obs_clearance)
    obstacle_clearence = 5 #mm
    
    # Radius of the Robot  
    robot_radius = input("Enter the Radius of the Robot: ") 
    robot_radius = int(robot_radius)
    
    # Step Size of the Robot  
    robot_step_size = input("Enter Step size of the Robot: ")
    robot_step_size = int(robot_step_size)
    
    width = 600
    height = 250
    obstacle_space = obstacle_space(width, height, obstacle_clearence, robot_radius)
    c2g = 0
    
    # Taking start node coordinates as input from user  
    start_coordinates = input("Enter coordinates for Start Node (separated by space)(x form 0 to 600 and y from 0 to 250): ")
    s_x, s_y = start_coordinates.split()
    s_x = int(s_x)
    s_y = int(s_y)
    
    # Taking Orientation for the robot  
    s_theta = input("Enter Orientation of the robot at start node: ")
    s_t = int(s_theta)
    
    # Checking if the user input is valid 
    if not ValidMove(s_x, s_y, obstacle_space):
        print("Start node is out of bounds or in obstacle space")
        exit(-1)
        
    if not validorient(s_t):
        print("Orientation has to be a multiple of 30")
        exit(-1)
		    
	# Taking Goal node coordinates as input from user   
    goal_coordinates = input("Enter coordinates for Goal Node (separated by space)(x form 0 to 600 and y from 0 to 250): ")
    g_x, g_y = goal_coordinates.split()
    g_x = int(g_x)
    g_y = int(g_y)
    
    # Taking Orientation for the robot  
    g_theta = input("Enter Orientation of the robot at goal node: ")
    g_t = int(g_theta)
    
    
    # Checking if the user input is valid  
    if not ValidMove(g_x, g_y, obstacle_space):
        print("Goal node is out of bounds")
        exit(-1)
        
    if not validorient(g_t):
        print("Orientation has to be a multiple of 30")
        exit(-1)

    # Timer to calculate computational  time  
    timer_start = time.time()
    
	# Creating start_node and goal_node objects 
    start_node = Node(s_x, s_y,s_t, 0.0, -1,c2g)
    goal_node = Node(g_x, g_y,g_t, 0.0, -1, c2g)
    all_nodes,flag = a_star(start_node, goal_node, obstacle_space, robot_step_size)
    
    # Plot shortest path only when goal node is reached  
    if (flag)==1:
        x_path,y_path = Backtrack(goal_node)
        cost = goal_node.cost
        print("Total cost is:", cost)

    else:
        print("No path was found")
		
    plot(start_node,goal_node,x_path,y_path,all_nodes,obstacle_space)
    timer_stop = time.time()
    
    C_time = timer_stop - timer_start
    print("The Total Runtime is:  ", C_time) 
	



	










