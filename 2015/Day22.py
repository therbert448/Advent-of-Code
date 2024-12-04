class Player:
    def __init__(self, hp, mana, effects):
        self.hp = hp
        self.mana = mana
        self.dead = 0
        self.effects = dict(effects)
        if "shield" in self.effects:
            self.armour = 7
        else:
            self.armour = 0
    
    def apply_effects(self, other):
        newdict = {}
        for effect in self.effects:
            timer = self.effects[effect]
            if effect == "poison":
                other.hp -= 3
            elif effect == "recharge":
                self.mana += 101
            timer -= 1
            if timer != 0:
                newdict[effect] = timer
            elif timer == 0 and effect == "shield":
                self.armour = 0
        if other.hp <= 0:
            other.dead = 1
        self.effects = dict(newdict)

    def attack(self, other, move):
        if self.dead:
            return
        if move == "magic_missile":
            damage = 4
            other.hp -= damage
            if other.hp <= 0:
                other.dead = 1
        elif move == "drain":
            damage = 2
            other.hp -= damage
            self.hp += damage
            if other.hp <= 0:
                other.dead = 1
        elif move in ("shield", "poison"):
            self.effects[move] = 6
            if move == "shield":
                self.armour = 7
        elif move == "recharge":
            self.effects[move] = 5
        self.mana -= moves[move]

class Boss:
    def __init__(self, hp):
        self.hp = hp
        self.damage = 9
        self.dead = 0
    
    def attack(self, other):
        if self.dead:
            return
        if self.damage <= other.armour:
            damage = 1
        else:
            damage = self.damage - other.armour
        other.hp -= damage
        if other.hp <= 0:
            other.dead = 1

def play(player, boss, used, minused):
    hp, mana, effects = [player.hp, player.mana, dict(player.effects)]
    bosshp = boss.hp
    end = False #player hasn't won
    for move in moves: #pick one of the 5 moves
        newplay = Player(hp, mana, effects) #copy the player and boss
        newboss = Boss(bosshp)
        if hard:
            newplay.hp -= 1 #lose 1hp if hard mode
            if newplay.hp <= 0:
                break
        totalmana = used #how much mana have I used up to now
        newplay.apply_effects(newboss) #apply any active effects
        if newboss.dead: #if poison has killed the boss
            if minused == -1 or totalmana < minused: 
                #is this the best case so far?
                end = True #player has won
                minused = totalmana
            break #any selected move will result in this outcome
        needed = moves[move]
        if needed > mana: #do I have enough mana for this move?
            break #I won't have enough mana for any move left (increasing order)
        if move in newplay.effects:
            continue #will the move start an effect that's already active?
        totalmana += needed #add move mana onto cumulative total
        if minused != -1 and totalmana >= minused:
            break #if this amount of mana is worse than the best case so far
            #no point continuing with this line of moves
        newplay.attack(newboss, move) #attack the boss
        if newboss.dead: #if the boss is dead
            if minused == -1 or totalmana < minused: #and this is best so far
                end = True #player has won
                minused = totalmana #save minimum mana value
            break #further moves can't improve on this total mana
        if hard:
            newplay.hp -= 1 #lose 1hp in hard mode
            if newplay.hp <= 0:
                break # player is dead :(
        newplay.apply_effects(newboss) #apply active effects
        if newboss.dead: #boss dead
            if minused == -1 or totalmana < minused: #best case so far
                end = True #player has won
                minused = totalmana #save min mana value
            break #further move combos cannot improve on this case
        newboss.attack(newplay) #let the boss attack
        if not newplay.dead and not newboss.dead: #if both still standing
            #after one move each
            win, totalmana = play(newplay, newboss, totalmana, minused)
            #recursive function to check the best move combos
            if win: #if the function returns at least one case where the
                #player has won
                end = True
                if minused < 0 or totalmana < minused:
                    #check if this case is better than any case before
                    minused = totalmana
    #end will be false if no combination of moves has led to a player victory
    #minused will be ignored in this case
    #end is true if at least one combo killed the boss.
    #minused will be checked to see if this represents the best case
    return end, minused

moves = {"magic_missile": 53, 
         "drain": 73, 
         "shield": 113, 
         "poison": 173,
         "recharge": 229}

hp, mana, effects = [50, 500, {}]
player = Player(hp, mana, effects)
bosshp = 58
boss = Boss(bosshp)

hard = 0
end, minmana = play(player, boss, 0, -1)
if end:
    print(f"Part One: {minmana}")

hard = 1
end, minmana = play(player, boss, 0, -1)
if end:
    print(f"Part Two: {minmana}")