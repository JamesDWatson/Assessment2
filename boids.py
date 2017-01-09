
from matplotlib import pyplot as plt
from matplotlib import animation
import random

#Introduce variables to remove hard coded variables.
Num_boids = 50  # Number of boids.



boids_x=[random.uniform(-450,50.0) for x in range(Num_boids)]
boids_y=[random.uniform(300.0,600.0) for x in range(Num_boids)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(Num_boids)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(Num_boids)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    xs,ys,xvs,yvs=boids
    
    # Fly towards the middle
    for i in range(Num_boids):
        for j in range(Num_boids):
            xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs) 
    for i in range(Numboids):
        for j in range(Numboids):
            yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
            
    # Fly away from nearby boids
    for i in range(Num_boids):
        for j in range(Num_boids):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:  #If distance between two boids is sufficiently small, moves them away.
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
                
    # Try to match speed with nearby boids
    for i in range(Num_boids):
        for j in range(Num_boids):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
                
    # Move according to velocities
    for i in range(Num_boids):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
    update_boids(boids)
    scatter.set_offsets(zip(boids[0],boids[1]))

anim = animation.FuncAnimation(figure, animate,
                                    frames=50, interval=50)

if __name__ == "__main__":
    plt.show()