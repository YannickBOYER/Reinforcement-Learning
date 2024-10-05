import random
import matplotlib.pyplot as plt
import seaborn as sns

class Bandit:
    def __init__(self):
        self.avg = random.gauss(0, 1)
    
    def play(self):
        return random.gauss(self.avg, 1)

class Ban10:
    def __init__(self):
        self.bandits = [Bandit() for i in range(10)]
        self.id_best_bandit = max(range(len(self.bandits)), key=lambda x: self.bandits[x].avg)

    def play(self, numero):
        if 0 <= numero < len(self.bandits):
            return self.bandits[numero].play()

class GreedyPlayer:
    def __init__(self, n, eps):
        self.n = n
        self.eps = eps
        self.eval_count = [0] * n
        self.action_values = [0.0] * n

    def get_action(self):
        random_value = random.random()
        explore = random_value < self.eps
        
        if explore:
            return self._random_action()
        else:
            return self._greedy_action()
    
    def _greedy_action(self):
        max_value_estimation = max(self.action_values)
        bests_actions = [i for i, value in enumerate(self.action_values) if value == max_value_estimation]
        return random.choice(bests_actions)
    
    def _random_action(self):
        return random.randint(0, self.n - 1)

    def reward(self, action, reward):
        self.eval_count[action] += 1
        self.action_values[action] += (reward - self.action_values[action]) / self.eval_count[action]

if __name__ == "__main__":
    # Exo 1
    # bandit1 = Bandit()
    # bandit2 = Bandit()
    # bandit3 = Bandit()
    
    # print(f"Valeur moyenne bandit 1 (avg) : {bandit1.avg}")
    # print(f"Valeur moyenne bandit 2 (avg) : {bandit2.avg}")
    # print(f"Valeur moyenne bandi 3 (avg) : {bandit3.avg}")

    # results1 = [bandit1.play() for i in range(1000)]
    # results2 = [bandit2.play() for i in range(1000)]
    # results3 = [bandit3.play() for i in range(1000)]

    # sns.histplot(results1, kde=True, stat="density") # Kernel Density Estimation activée
    # sns.histplot(results2, kde=True, stat="density")
    # sns.histplot(results3, kde=True, stat="density")
    # plt.title('Histogramme')
    # plt.xlabel('Valeurs')
    # plt.ylabel('Densité')
    # plt.show()

    # Exo 2
    # ban10 = Ban10()
    # print(f"Id du meilleur bandit : {ban10.id_best_bandit}")
    # print(f"Valeur jouée avec le meilleur bandit : {ban10.play(ban10.id_best_bandit)}")

    # Exo 3 + 4
    
    players = [GreedyPlayer(n=10, eps=0.1) for _ in range(2000)]
    bandits = [Ban10() for _ in range(2000)]
    rewards = []

    for _ in range(1000):
        rewards_step = []
        for i in range(len(players)):
            player = players[i]
            bandit = bandits[i]
            action = player.get_action()
            reward = bandit.play(action)
            player.reward(action, reward)
            optimal_action = action == bandit.id_best_bandit
            print(f"Tour {_}: Récompense: {reward}, Optimal: {optimal_action}")
            rewards_step.append(reward)
        avg_reward = sum(rewards_step) / len(rewards_step)
        rewards.append(avg_reward)

    plt.plot(rewards)
    plt.title('Évolution de la récompense')
    plt.xlabel('Itération')
    plt.ylabel('Récompense')
    plt.show()

    print(f"Action values: {player.action_values}")

