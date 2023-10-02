import events as e

def calculate_reward_from_events(self, events) -> int:
   
    game_rewards = {
        e.COIN_COLLECTED: 100,
        e.KILLED_OPPONENT: 500,
        e.MOVED_RIGHT: -1,
        e.MOVED_LEFT: -1,
        e.MOVED_UP: -1,
        e.MOVED_DOWN: -1,
        e.WAITED: -1,
        e.INVALID_ACTION: -10,
        e.BOMB_DROPPED: -1,
        e.KILLED_SELF: 0,
        e.GOT_KILLED: -700,
    }

    total_reward = 0
    for event in events:
        if event in game_rewards:
            total_reward += game_rewards[event]
    self.logger.info(f"Awarded {total_reward} for events {', '.join(events)}")
    return total_reward

def calculate_rewards_from_own_events(self, events):
    
    total_reward = 0
    total_reward += crate_rewards(self, events)
    self.logger.info(f"Awarded {total_reward} for own transition events")
    return total_reward


def crate_rewards(self, events):
    
    if e.BOMB_DROPPED in events:
        self.logger.info(f"reward for the {self.destroyed_crates} that are going to be destroyed -> +{self.destroyed_crates * 33}")
        return self.destroyed_crates * 33
    return 0