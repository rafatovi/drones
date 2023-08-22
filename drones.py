"""
Demo the trick flying for the python interface

Author: Amy McGovern
"""
from pyparrot.Minidrone import Mambo

# you will need to change this to the address of YOUR mambo
mamboAddr = "e0:14:c4:78:3d:fd"

# make my mambo object, set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambo = Mambo(mamboAddr, use_wifi=False)

def pop():  
    success = mambo.connect(num_retries=3)
    
    if (success):
        # get the state information
        print("sleeping")
        mambo.smart_sleep(2)
        mambo.ask_for_state_update()
        mambo.smart_sleep(2)

        print("taking off!")
        mambo.safe_takeoff(5)


        if (mambo.sensors.flying_state != "emergency"):
            print("flying state is %s" % mambo.sensors.flying_state)
            print("Flying direct: going up")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
            print("landing")
            print("flying state is %s" % mambo.sensors.flying_state)
            mambo.safe_land(5)
            mambo.smart_sleep(5)
        """
            print("flip left")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="left")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip right")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="right")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip front")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="front")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip back")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="back")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)
"""

        
        print("disconnect")
        mambo.disconnect()
def classical():
    # you will need to change this to the address of YOUR mambo
    mamboAddr = "e0:14:c4:78:3d:fd"

    # make my mambo object
    # remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
    mambo = Mambo(mamboAddr, use_wifi=False)

    print("trying to connect")
    success = mambo.connect(num_retries=3)
    mambo.ask_for_state_update()
    print(f"connected: {success}, battery {mambo.sensors.battery}")

    safe_warning = input("De certeza que quer levantar vou (sim ou nao)")
    if safe_warning != "sim":
        print("Nao vai levantar vou")
        exit()

    
    if (success):
        # get the state information
        print("sleeping")
        mambo.smart_sleep(2)
        mambo.ask_for_state_update()
        mambo.smart_sleep(2)

        print("taking off!")
        mambo.safe_takeoff(5)


        if (mambo.sensors.flying_state != "emergency"):
            print("flying state is %s" % mambo.sensors.flying_state)
            print("Flying direct: going up")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
            print("landing")
            print("flying state is %s" % mambo.sensors.flying_state)
            mambo.safe_land(5)
            mambo.smart_sleep(5)
        """
            print("flip left")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="left")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip right")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="right")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip front")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="front")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip back")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="back")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)
"""

        
        print("disconnect")
        mambo.disconnect()
def country():
    # you will need to change this to the address of YOUR mambo
    mamboAddr = "e0:14:c4:78:3d:fd"

    # make my mambo object
    # remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
    mambo = Mambo(mamboAddr, use_wifi=False)

    print("trying to connect")
    success = mambo.connect(num_retries=3)
    mambo.ask_for_state_update()
    print(f"connected: {success}, battery {mambo.sensors.battery}")

    safe_warning = input("De certeza que quer levantar vou (sim ou nao)")
    if safe_warning != "sim":
        print("Nao vai levantar vou")
        exit()

    
    if (success):
        # get the state information
        print("sleeping")
        mambo.smart_sleep(2)
        mambo.ask_for_state_update()
        mambo.smart_sleep(2)

        print("taking off!")
        mambo.safe_takeoff(5)


        if (mambo.sensors.flying_state != "emergency"):
            print("flying state is %s" % mambo.sensors.flying_state)
            print("Flying direct: going up")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
            print("landing")
            print("flying state is %s" % mambo.sensors.flying_state)
            mambo.safe_land(5)
            mambo.smart_sleep(5)
        """
            print("flip left")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="left")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip right")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="right")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip front")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="front")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip back")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="back")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)
"""

        
        print("disconnect")
        mambo.disconnect()
def disco():
    # you will need to change this to the address of YOUR mambo
    mamboAddr = "e0:14:c4:78:3d:fd"

    # make my mambo object
    # remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
    mambo = Mambo(mamboAddr, use_wifi=False)

    print("trying to connect")
    success = mambo.connect(num_retries=3)
    mambo.ask_for_state_update()
    print(f"connected: {success}, battery {mambo.sensors.battery}")

    safe_warning = input("De certeza que quer levantar vou (sim ou nao)")
    if safe_warning != "sim":
        print("Nao vai levantar vou")
        exit()

    
    if (success):
        # get the state information
        print("sleeping")
        mambo.smart_sleep(2)
        mambo.ask_for_state_update()
        mambo.smart_sleep(2)

        print("taking off!")
        mambo.safe_takeoff(5)


        if (mambo.sensors.flying_state != "emergency"):
            print("flying state is %s" % mambo.sensors.flying_state)
            print("Flying direct: going up")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
            print("landing")
            print("flying state is %s" % mambo.sensors.flying_state)
            mambo.safe_land(5)
            mambo.smart_sleep(5)
        """
            print("flip left")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="left")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip right")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="right")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip front")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="front")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip back")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="back")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)
"""

        
        print("disconnect")
        mambo.disconnect()
def hiphop():
    # you will need to change this to the address of YOUR mambo
    mamboAddr = "e0:14:c4:78:3d:fd"

    # make my mambo object
    # remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
    mambo = Mambo(mamboAddr, use_wifi=False)

    print("trying to connect")
    success = mambo.connect(num_retries=3)
    mambo.ask_for_state_update()
    print(f"connected: {success}, battery {mambo.sensors.battery}")

    safe_warning = input("De certeza que quer levantar vou (sim ou nao)")
    if safe_warning != "sim":
        print("Nao vai levantar vou")
        exit()

    
    if (success):
        # get the state information
        print("sleeping")
        mambo.smart_sleep(2)
        mambo.ask_for_state_update()
        mambo.smart_sleep(2)

        print("taking off!")
        mambo.safe_takeoff(5)


        if (mambo.sensors.flying_state != "emergency"):
            print("flying state is %s" % mambo.sensors.flying_state)
            print("Flying direct: going up")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
            print("landing")
            print("flying state is %s" % mambo.sensors.flying_state)
            mambo.safe_land(5)
            mambo.smart_sleep(5)
        """
            print("flip left")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="left")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip right")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="right")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip front")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="front")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip back")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="back")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)
"""

        
        print("disconnect")
        mambo.disconnect()
def jazz():
    # you will need to change this to the address of YOUR mambo
    mamboAddr = "e0:14:c4:78:3d:fd"

    # make my mambo object
    # remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
    mambo = Mambo(mamboAddr, use_wifi=False)

    print("trying to connect")
    success = mambo.connect(num_retries=3)
    mambo.ask_for_state_update()
    print(f"connected: {success}, battery {mambo.sensors.battery}")

    safe_warning = input("De certeza que quer levantar vou (sim ou nao)")
    if safe_warning != "sim":
        print("Nao vai levantar vou")
        exit()

    
    if (success):
        # get the state information
        print("sleeping")
        mambo.smart_sleep(2)
        mambo.ask_for_state_update()
        mambo.smart_sleep(2)

        print("taking off!")
        mambo.safe_takeoff(5)


        if (mambo.sensors.flying_state != "emergency"):
            print("flying state is %s" % mambo.sensors.flying_state)
            print("Flying direct: going up")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
            print("landing")
            print("flying state is %s" % mambo.sensors.flying_state)
            mambo.safe_land(5)
            mambo.smart_sleep(5)
        """
            print("flip left")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="left")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip right")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="right")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip front")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="front")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip back")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="back")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)
"""

        
        print("disconnect")
        mambo.disconnect()
def metal():
    # you will need to change this to the address of YOUR mambo
    mamboAddr = "e0:14:c4:78:3d:fd"

    # make my mambo object
    # remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
    mambo = Mambo(mamboAddr, use_wifi=False)

    print("trying to connect")
    success = mambo.connect(num_retries=3)
    mambo.ask_for_state_update()
    print(f"connected: {success}, battery {mambo.sensors.battery}")

    safe_warning = input("De certeza que quer levantar vou (sim ou nao)")
    if safe_warning != "sim":
        print("Nao vai levantar vou")
        exit()

    
    if (success):
        # get the state information
        print("sleeping")
        mambo.smart_sleep(2)
        mambo.ask_for_state_update()
        mambo.smart_sleep(2)

        print("taking off!")
        mambo.safe_takeoff(5)


        if (mambo.sensors.flying_state != "emergency"):
            print("flying state is %s" % mambo.sensors.flying_state)
            print("Flying direct: going up")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
            print("landing")
            print("flying state is %s" % mambo.sensors.flying_state)
            mambo.safe_land(5)
            mambo.smart_sleep(5)
        """
            print("flip left")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="left")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip right")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="right")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip front")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="front")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip back")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="back")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)
"""

        
        print("disconnect")
        mambo.disconnect()
def reggae():
    # you will need to change this to the address of YOUR mambo
    mamboAddr = "e0:14:c4:78:3d:fd"

    # make my mambo object
    # remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
    mambo = Mambo(mamboAddr, use_wifi=False)

    print("trying to connect")
    success = mambo.connect(num_retries=3)
    mambo.ask_for_state_update()
    print(f"connected: {success}, battery {mambo.sensors.battery}")

    safe_warning = input("De certeza que quer levantar vou (sim ou nao)")
    if safe_warning != "sim":
        print("Nao vai levantar vou")
        exit()

    
    if (success):
        # get the state information
        print("sleeping")
        mambo.smart_sleep(2)
        mambo.ask_for_state_update()
        mambo.smart_sleep(2)

        print("taking off!")
        mambo.safe_takeoff(5)


        if (mambo.sensors.flying_state != "emergency"):
            print("flying state is %s" % mambo.sensors.flying_state)
            print("Flying direct: going up")
            mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=20, duration=1)
            print("landing")
            print("flying state is %s" % mambo.sensors.flying_state)
            mambo.safe_land(5)
            mambo.smart_sleep(5)
        """
            print("flip left")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="left")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip right")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="right")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip front")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="front")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)

            print("flip back")
            print("flying state is %s" % mambo.sensors.flying_state)
            success = mambo.flip(direction="back")
            print("mambo flip result %s" % success)
            mambo.smart_sleep(5)
"""

        
        print("disconnect")
        mambo.disconnect()

if __name__ == '__main__':
   pop()
   classical()
   country()
   disco()
   hiphop()
   jazz()
   metal()
   reggae()