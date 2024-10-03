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
        return self.bandits[numero].play()
        
if __name__ == "__main__":
    # Exo 1
    bandit1 = Bandit()
    bandit2 = Bandit()
    bandit3 = Bandit()
    
    print(f"Valeur moyenne bandit 1 (avg) : {bandit1.avg}")
    print(f"Valeur moyenne bandit 2 (avg) : {bandit2.avg}")
    print(f"Valeur moyenne bandi 3 (avg) : {bandit3.avg}")

    results1 = [bandit1.play() for i in range(1000)]
    results2 = [bandit2.play() for i in range(1000)]
    results3 = [bandit3.play() for i in range(1000)]

    sns.histplot(results1, kde=True, stat="density") # Kernel Density Estimation activée
    sns.histplot(results2, kde=True, stat="density")
    sns.histplot(results3, kde=True, stat="density")
    plt.title('Histogramme')
    plt.xlabel('Valeurs')
    plt.ylabel('Densité')
    # plt.show()

    # Exo 2
    ban10 = Ban10()
    print(f"Id du meilleur bandit : {ban10.id_best_bandit}")
    print(f"Valeur jouée avec le meilleur bandit : {ban10.play(ban10.id_best_bandit)}")

