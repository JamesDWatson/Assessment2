
from matplotlib import pyplot as plt
from matplotlib import animation
import random

#Introduce variables to remove hard coded variables.
Num_boids = 50  # Number of boids. Maybe have this as a command line input?



boids_x=[random.uniform(-450,50.0) for x in range(Num_boids)]   #Defines the boids' x, y positions and velocities respectively.
boids_y=[random.uniform(300.0,600.0) for x in range(Num_boids)] #These are chosen from a random number distribution.
boid_x_velocities=[random.uniform(0,10.0) for x in range(Num_boids)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(Num_boids)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    x_pos,y_pos,x_vel,y_vel=boids #Change to more descriptive variable names.
    
    # Fly towards the middle
    for i in range(Num_boids):   #This code is repeated.
        for j in range(Num_boids):
            x_vel[i]=x_vel[i]+(x_pos[j]-x_pos[i])*0.01/len(xs)# Remove hardcoded numbers.
    for i in range(Numboids):
        for j in range(Numboids):
            y_vel[i]=y_vel[i]+(y_pos[j]-y_pos[i])*0.01/len(xs)
            
    # Fly away from nearby boids
    for i in range(Num_boids):
        for j in range(Num_boids):
            if (x_pos[j]-x_pos[i])**2 + (y_pos[j]-y_pos[i])**2 < 100:  #If distance between two boids is sufficiently small, moves them away.
                x_vel[i]=x_vel[i]+(x_pos[i]-x_pos[j])
                y_vel[i]=y_vel[i]+(y_pos[i]-y_pos[j])
                
    # Try to match speed with nearby boids
    for i in range(Num_boids):
        for j in range(Num_boids):
            if (x_pos[j]-x_pos[i])**2 + (y_pos[j]-y_pos[i])**2 < 10000:
                x_vel[i]=x_vel[i]+(x_vel[j]-x_vel[i])*0.125/len(xs)
                y_vel[i]=y_vel[i]+(y_vel[j]-y_vel[i])*0.125/len(xs)
                
    # Move according to velocities
    for i in range(Num_boids):
        x_pos[i]=x_pos[i]+x_vel[i]
        y_pos[i]=y_pos[i]+y_vel[i]

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):    #Maybe put in a library.
    update_boids(boids)
    scatter.set_offsets(zip(boids[0],boids[1]))

anim = animation.FuncAnimation(figure, animate,
                                    frames=50, interval=50)

if __name__ == "__main__":
    plt.show()