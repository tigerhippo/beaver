import uuid
import random
from gym_zgame.envs.enums.NPC_STATES import NPC_STATES_DEAD, NPC_STATES_ZOMBIE, NPC_STATES_FLU
from gym_zgame.envs.enums.NPC_ACTIONS import NPC_ACTIONS
from gym_zgame.envs.enums.PLAYER_ACTIONS import LOCATIONS


class NPC:

    def __init__(self):
        self.id = uuid.uuid4()
        self.state_dead = NPC_STATES_DEAD.ALIVE
        self.state_zombie = NPC_STATES_ZOMBIE.HUMAN
        self.state_flu = NPC_STATES_FLU.HEALTHY
        self.moving = None
        self.active = None
        self.sickly = None
        self.update_states()
        self.bag = []
        self.empty_bag()

    def empty_bag(self):
        self.bag = []

    def set_init_bag_alive(self):
        for _ in range(6):
            self.bag.append(NPC_ACTIONS.STAY)
        self.bag.append(NPC_ACTIONS.N)
        self.bag.append(NPC_ACTIONS.S)
        self.bag.append(NPC_ACTIONS.E)
        self.bag.append(NPC_ACTIONS.W)

    def clean_bag(self, location):
        # Build list of things that shouldn't be in the bag
        actions_to_remove = []
        if location is LOCATIONS.N:
            actions_to_remove = [NPC_ACTIONS.N]
        elif location is LOCATIONS.S:
            actions_to_remove = [NPC_ACTIONS.S]
        elif location is LOCATIONS.E:
            actions_to_remove = [NPC_ACTIONS.E]
        elif location is LOCATIONS.W:
            actions_to_remove = [NPC_ACTIONS.W]
        elif location is LOCATIONS.NE:
            actions_to_remove = [NPC_ACTIONS.N, NPC_ACTIONS.E]
        elif location is LOCATIONS.NW:
            actions_to_remove = [NPC_ACTIONS.N, NPC_ACTIONS.W]
        elif location is LOCATIONS.SE:
            actions_to_remove = [NPC_ACTIONS.S, NPC_ACTIONS.E]
        elif location is LOCATIONS.SW:
            actions_to_remove = [NPC_ACTIONS.S, NPC_ACTIONS.W]
        # Clear the bad things out of the bag
        fresh_bag = [action for action in self.bag if action not in actions_to_remove]
        self.bag = fresh_bag

    def update_states(self):
        self.moving = self.state_dead is NPC_STATES_DEAD.ALIVE
        self.active = self.moving and (self.state_zombie is NPC_STATES_ZOMBIE.HUMAN) and (
                    self.state_flu is not NPC_STATES_FLU.FLU)
        self.sickly = self.moving and not self.active and (self.state_zombie is not NPC_STATES_ZOMBIE.ZOMBIE)

    def change_dead_state(self, npc_states_dead):
        self.state_dead = npc_states_dead

    def change_zombie_state(self, npc_states_zombie):
        self.state_zombie = npc_states_zombie

    def change_flu_state(self, npc_states_flu):
        self.state_flu = npc_states_flu

    def add_to_bag(self, npc_action):
        self.bag.append(npc_action)

    def remove_from_bag(self, npc_action):
        self.bag.remove(npc_action)

    def selection(self):
        return random.choice(self.bag)

    def get_data(self):
        player_data = {'player_id': self.id,
                       'state_dead': self.state_dead,
                       'state_zombie': self.state_zombie,
                       'state_flu': self.state_flu,
                       'moving': self.moving,
                       'active': self.active,
                       'sickly': self.sickly}
        return player_data


if __name__ == '__main__':
    pers = NPC()
    pers.add_to_bag(NPC_ACTIONS.STAY)
    pers.add_to_bag(NPC_ACTIONS.STAY)
    print(pers.bag)
    pers.remove_from_bag(NPC_ACTIONS.STAY)
    print(pers.bag)
    for _ in range(4):
        print(pers.selection())
