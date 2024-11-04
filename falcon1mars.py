import math
with open('C:\\Users\\08nat\\OneDrive - jmss.vic.edu.au\\Documents\\Python Excel\\Falcon1Mars.csv', 'w') as outFile:
    outFile.write("Fuel Remaining,Mass,Acceleration,Altitude,Velocity,Flight time\n")

    # Peak speed
    peak_speed = 0

    # Peak Altitude
    peak_altitude = 0

    # Altitude
    altitude = 0 

    # Time since engine engagement
    time_elapsed = 0

    # Time step
    time_step = 1

    # Starting velocity 
    velocity = 0

    # Planet Choice

    # Gravity force (m/s**2)
    gravitational_force = 3.73

    # Air density (Kg/m**3)
    air_density = 0.020


    # Mass without fuel (kg)
    mass_without_fuel = 6000

    # Mass of fuel (kg)
    fuel_mass = 21000

    # drym + fuelm (kg)
    intial_mass = mass_without_fuel + fuel_mass

    # Height (m)
    height = 21.3

    # Diamater (m)
    diamater = 1.68

    # Cross-Sectional Area (m)
    cross_sectional_area = math.pi * (diamater / 2) ** 2

    # Thrust force (N)
    force_thrust = 400000

    # Specific Impulse (s)
    specific_impulse = 250

    # Burn rate
    burn_rate = force_thrust/(gravitational_force * specific_impulse)

    # Burn time
    burn_time = int(fuel_mass / burn_rate)

    # Drag
    Drag = 0.45

    # Drag Force
    force_drag = 1/2*Drag*cross_sectional_area*air_density*velocity**2

    # Acting gravity
    acting_gravity = intial_mass*gravitational_force

    # Net force
    net_force = force_thrust - acting_gravity - force_drag

    # Thrust to weight ratio
    ttw = force_thrust/acting_gravity

    # Acceleration (m/s)

    acceleration = net_force/intial_mass

    # Remaining Fuel
    fuel_remaining = fuel_mass


    # Is liftoff achieved
    if force_thrust > acting_gravity:
        print("Liftoff Achieved")
        for n in range(0, burn_time,time_step):
            if fuel_remaining <= 0:
                print("Fuel depleted")
                break
            
            fuel_burnt = burn_rate*time_step
            fuel_remaining -= fuel_burnt
            intial_mass -= fuel_burnt
            acceleration = net_force/intial_mass
            velocity += acceleration*time_step
            altitude += velocity+time_step
            time_elapsed += time_step
            acting_gravity = intial_mass*gravitational_force
            force_drag = 1/2*Drag*cross_sectional_area*air_density*velocity**2
            print(f'Fuel Remaining: {int(fuel_remaining)} kg ')
            print(f'Mass: {int(intial_mass)} kg ')
            print(f'Acceleration: {int(acceleration)} m/s ')
            print(f'Altitude: {int(altitude)} m ')
            print(f'Velocity: {int(velocity)} m/s')
            print(f'Flight Time: {time_elapsed} s')
            print('------------------------------')
            outFile.write(f"{fuel_remaining},{intial_mass},{acceleration},{altitude},{velocity},{time_elapsed}\n")

            if peak_altitude < altitude:
                peak_altitude = altitude
            if peak_speed < velocity:
                peak_speed = velocity
        
        while altitude > 0:
            acting_gravity = intial_mass*gravitational_force
            force_drag = 1/2*Drag*cross_sectional_area*air_density*velocity**2
            force_drag = -force_drag if velocity > 0 else force_drag
            net_force = -acting_gravity + force_drag
            acceleration = net_force / intial_mass
            velocity += acceleration * time_step
            altitude += velocity * time_step
            time_elapsed += time_step

            if altitude < 0:
                altitude = 0
                velocity = 0
                print("Rocket hit the ground")
            print(f'Fuel Remaining: {int(fuel_remaining)} kg ')
            print(f'Mass: {int(intial_mass)} kg ')
            print(f'Acceleration: {int(acceleration)} m/s ')
            print(f'Altitude: {int(altitude)} m ')
            print(f'Velocity: {int(velocity)} m/s')
            print(f'Flight Time: {time_elapsed} s')
            print('------------------------------')
            outFile.write(f"{fuel_remaining},{intial_mass},{acceleration},{altitude},{velocity},{time_elapsed}\n")

            

    else:
        print("Liftoff was not achieved")
    print(f"Peak Altitude: {int(peak_altitude)} m\nPeak Speed: {int(peak_speed)} m/s\nFlight Time: {int(time_elapsed)} s")
