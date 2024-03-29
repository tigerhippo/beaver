import random
from gym_zgame.envs.enums.PLAYER_ACTIONS import LOCATIONS, DEPLOYMENTS
from gym_zgame.envs.enums.NPC_STATES import NPC_STATES_DEAD, NPC_STATES_ZOMBIE, NPC_STATES_FLU
from gym_zgame.envs.model.NPC import NPC


class Neighborhood:

    def __init__(self, id, location, adj_locations, num_init_npcs):
        self.id = id
        self.location = location
        self.NPCs = []
        self.adj_locations = adj_locations
        self._npc_init(num_init_npcs)
        self.deployments = []
        # Transition probabilities
        self.trans_probs = self.compute_baseline_trans_probs()
        # Keep summary stats up to date for ease
        self.num_npcs = len(self.NPCs)
        self.num_alive = 0
        self.num_dead = 0
        self.num_ashen = 0
        self.num_human = 0
        self.num_zombie_bitten = 0
        self.num_zombie = 0
        self.num_healthy = 0
        self.num_incubating = 0
        self.num_flu = 0
        self.num_immune = 0
        self.num_moving = 0
        self.num_active = 0
        self.num_sickly = 0
        self.update_summary_stats()
        self.orig_alive, self.orig_dead = self._get_original_state_metrics()

    def _npc_init(self, num_npcs):
        init_npcs = []
        for _ in range(num_npcs):
            npc = NPC()
            zombie_chance = random.uniform(0, 1)
            flu_chance = random.uniform(0, 1)
            if zombie_chance >= 0.9:
                npc.state_zombie = NPC_STATES_ZOMBIE.ZOMBIE
            if flu_chance >= 0.9:
                npc.state_flu = NPC_STATES_FLU.FLU
            init_npcs.append(npc)
        self.add_NPCs(init_npcs)

    def _get_original_state_metrics(self):
        og_alive = 0
        og_dead = 0
        og_alive += self.num_alive
        og_dead += self.num_dead
        return og_alive, og_dead

    def compute_baseline_trans_probs(self):
        self.update_summary_stats()
        trans_probs = {
            'burial': (self.num_active / self.num_dead) * 0.1 if self.num_dead > 0 else 0,  # dead -> ashen
            'recover': 0.25,  # flu -> flu immune
            'pneumonia': 0.01,  # flu -> dead
            'incubate': 0.25,  # incubating -> flu
            'fumes': self.num_dead * 0.01,  # healthy -> incubating
            'cough': self.num_flu / self.num_moving if self.num_moving > 0 else 0,  # healthy -> incubating
            'mutate': 0.01,  # immune -> healthy
            'turn': 0.2,  # zombie bitten -> zombie
            'devour': (self.num_zombie / self.num_moving) * 0.5 if self.num_moving > 0 else 0,  # human -> dead
            'bite': (self.num_zombie / self.num_moving) * 0.5 if self.num_moving > 0 else 0,  # human -> zombie bitten
            'fight_back': self.num_active * 0.01,  # zombie -> dead
            'collapse': 0.1,  # zombie -> dead
            'rise': 0.1  # dead -> zombie
        }
        return trans_probs

    def add_NPC(self, NPC):
        self.NPCs.append(NPC)
        self.update_summary_stats()

    def add_NPCs(self, NPCs):
        self.NPCs.extend(NPCs)
        self.update_summary_stats()

    def remove_NPC(self, NPC):
        if NPC in self.NPCs:
            self.NPCs.remove(NPC)
            self.update_summary_stats()
        else:
            print('WARNING: Attempted to remove NPC that did not exist in neighborhood')

    def remove_NPCs(self, NPCs):
        for NPC in NPCs:
            self.remove_NPC(NPC)

    def clean_all_bags(self):
        for npc in self.NPCs:
            npc.clean_bag(self.location)

    def add_deployment(self, deployment):
        self.deployments.append(deployment)

    def add_deployments(self, deployments):
        self.deployments.extend(deployments)

    def destroy_deployments_by_type(self, dep_types):
        self.deployments = [dep for dep in self.deployments if dep not in dep_types]

    def update_summary_stats(self):
        self.num_npcs = len(self.NPCs)
        num_alive = 0
        num_dead = 0
        num_ashen = 0
        num_human = 0
        num_zombie_bitten = 0
        num_zombie = 0
        num_healthy = 0
        num_incubating = 0
        num_flu = 0
        num_immune = 0
        num_moving = 0
        num_active = 0
        num_sickly = 0
        for npc in self.NPCs:
            if npc.state_dead is NPC_STATES_DEAD.ALIVE:
                num_alive += 1
            if npc.state_dead is NPC_STATES_DEAD.DEAD:
                num_dead += 1
            if npc.state_dead is NPC_STATES_DEAD.ASHEN:
                num_ashen += 1
            if npc.state_zombie is NPC_STATES_ZOMBIE.HUMAN:
                num_human += 1
            if npc.state_zombie is NPC_STATES_ZOMBIE.ZOMBIE_BITTEN:
                num_zombie_bitten += 1
            if npc.state_zombie is NPC_STATES_ZOMBIE.ZOMBIE:
                num_zombie += 1
            if npc.state_flu is NPC_STATES_FLU.HEALTHY:
                num_healthy += 1
            if npc.state_flu is NPC_STATES_FLU.INCUBATING:
                num_incubating += 1
            if npc.state_flu is NPC_STATES_FLU.FLU:
                num_flu += 1
            if npc.state_flu is NPC_STATES_FLU.IMMUNE:
                num_immune += 1
            if npc.moving:
                num_moving += 1
            if npc.active:
                num_active += 1
            if npc.sickly:
                num_sickly += 1

        self.num_alive = num_alive
        self.num_dead = num_dead
        self.num_ashen = num_ashen
        self.num_human = num_human
        self.num_zombie_bitten = num_zombie_bitten
        self.num_zombie = num_zombie
        self.num_healthy = num_healthy
        self.num_incubating = num_incubating
        self.num_flu = num_flu
        self.num_immune = num_immune
        self.num_moving = num_moving
        self.num_active = num_active
        self.num_sickly = num_sickly

        total_count_dead = self.num_alive + self.num_dead + self.num_ashen
        total_count_zombie = self.num_human + self.num_zombie_bitten + self.num_zombie
        total_count_flu = self.num_healthy + self.num_incubating + self.num_flu + self.num_immune
        assert (self.num_npcs == total_count_dead)
        assert (self.num_npcs == total_count_zombie)
        assert (self.num_npcs == total_count_flu)

    def get_data(self):
        self.update_summary_stats()
        neighborhood_data = {'id': self.id,
                             'location': self.location,
                             'num_npcs': self.num_npcs,
                             'num_alive': self.num_alive,
                             'num_dead': self.num_dead,
                             'num_ashen': self.num_ashen,
                             'num_human': self.num_human,
                             'num_zombie_bitten': self.num_zombie_bitten,
                             'num_zombie': self.num_zombie,
                             'num_healthy': self.num_healthy,
                             'num_incubating': self.num_incubating,
                             'num_flu': self.num_flu,
                             'num_immune': self.num_immune,
                             'num_moving': self.num_moving,
                             'num_active': self.num_active,
                             'num_sickly': self.num_sickly,
                             'original_alive': self.orig_alive,
                             'original_dead': self.orig_dead,
                             'deployments': self.deployments}
        return neighborhood_data


if __name__ == '__main__':
    nb = Neighborhood('CENTER', LOCATIONS.CENTER, (LOCATIONS.N, LOCATIONS.S, LOCATIONS.W, LOCATIONS.E), 10)
    print(nb.num_npcs)
