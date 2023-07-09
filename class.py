#成员变量，成员函数，初始化

# class Footman:
#     def __init__(self, name, health, power, armor, ft_ratio = 0):
#         self.name = name
#         self.health = health
#         self.power = power
#         self.armor = armor 
#         self.fantan = ft_ratio
    
#     def print_health(self):
#         print(f"{self.name}'s health is {self.health}")

#     def attack(self, enermy):
#         damage = max(0, self.power-enermy.armor)
#         enermy.health -= damage
#         self.health -= enermy.fantan * damage
#         enermy.print_health()
#         self.print_health()

    
# a = Footman("a", 100, 10, 5)
# b = Footman("b", 50, 20, 1, 0.5)
# a.print_health()
# b.print_health()
# a.attack(b)

# class Knight:
#     def __init__(self, name, health, power, armor, ft_ratio = 0.4) -> None:
#         self.name = name
#         self.health = health
#         self.power = power
#         self.armor = armor 
#         self.fantan = ft_ratio
    
#     def print_health(self):
#         print(f"{self.name}'s health is {self.health}")

#     def attack(self, enermy):
#         damage = max(0, self.power-enermy.armor)
#         enermy.health -= damage
#         self.health -= enermy.fantan * damage
#         enermy.print_health()
#         self.print_health()

#     def hard_attack(self, enermy):
#         damage = max(0, 2*(self.power-enermy.armor))
#         enermy.health -= damage
#         print(f"{self.name} hard attack {enermy.name}, cause {damage} damage, {enermy.name} left {enermy.health} health")

# a = Knight("a", 100, 10, 5)
# b = Footman(name="b", health=50, power=20, armor=1, ft_ratio=0.2)
# a.print_health()
# b.print_health()
# # b.attack(a)
# a.hard_attack(b)


# class Soldier:
#     def __init__(self, name, health, power, armor) -> None:
#         self.name = name
#         self.health = health
#         self.power = power
#         self.armor = armor
    
#     def __str__(self):
#         '''
#         自我介绍
#         '''
#         return f"{self.name}, has {self.health} health, {self.power} power, {self.armor} armor"

#     def attack(self, enermy):
#         damage = max(0, self.power-enermy.armor)
#         enermy.health -= damage
#         if hasattr(enermy, 'rebound'):
#             self.health -= enermy.rebound * damage

# class Footman(Soldier):
#     def __init__(self, name, health, power, armor, rebound=0.2) -> None:
#         super().__init__(name, health, power, armor) #初始化父类
#         self.state = 'offense'
#         self.rebound = rebound
    
#     def defense_state(self):
#         if self.state=='offense':
#             self.armor *= 2
#             self.power /= 2
#             self.state = 'defense'

#     def __str__(self):
#         return super().__str__() + f", {self.state} state"
    
#     def offense_state(self):
#         if self.state=='defense':
#             self.armor /= 2
#             self.power *= 2
#             self.state = 'offense'

# class Knight(Soldier):
#     def __init__(self, name, health, power, armor, weapon) -> None:
#         super().__init__(name, health, power, armor)
#         self.__weapon = weapon
#         self.weapon_damage = {"arrow": 5, "lance": 10}
    
#     @property
#     def get_weapon(self):
#         return self.__weapon

#     def attack(self, enermy):
#         damage = max(0, self.power + self.weapon_damage[self.__weapon] - enermy.armor)
#         enermy.health -= damage
    
#     def __str__(self):
#         return super().__str__() + f", use {self.__weapon}"

# # 类变量和类函数
# class Wizzard(Soldier):
#     count = 0 # 静态变量(类变量)
#     def __init__(self, name, health, power, armor, mega = 10) -> None:
#         if Wizzard.count >=2:
#             print("error")
#             raise TypeError("too many wizzard")
#         super().__init__(name, health, power, armor) # 初始化父类
#         self.mega = mega
#         Wizzard.count += 1
#         self.id = Wizzard.count
        

#     def attack(self, enermy,use_mega = 0):
#         if use_mega <= self.mega :
#             self.mega -= use_mega
#             damage = max(0, self.power*(1 + 0.1*use_mega) - enermy.armor)
#             enermy.health -= damage
#         else:
#             print("Not enough mega!")

#     def __str__(self):
#         return f"No.{self.id} wizzard, " + super().__str__() + f", remain {self.mega} mega"
    
#     @classmethod #静态方法(类方法)
#     def build_powerful_wizzard(cls, name, health, power, armor, mega):
#         return cls(name, health, power, armor, mega*10)


# bob = Footman(name='bob', health=50, power=10, armor=1, rebound=0.1)
# kevin = Knight("kelvin", 100, 10, 2, weapon='lance')
# lina = Wizzard("lina", health=45, power=12, armor=1)
# lion = Wizzard("lion", health=30, power=20, armor=1, mega=15)
# bane = Wizzard.build_powerful_wizzard("bane", health=30, power=20, armor=1, mega=15)
# print(lina, lion, bane, sep='\n')
# print(kevin.__weapon)
# print(kevin._Knight__weapon)
# print(kevin.get_weapon)
# print(bob, kevin, sep='\n')
# bob.attack(kevin)
# kevin.attack(bob)
# print(bob, kevin, sep='\n')
# lina.attack(bob,6)
# lina.attack(kevin,5)
# lina.attack(kevin,4)
# lina.attack(bob)
# print(bob)
# print(kevin)
# print(lina)
# 共有变量，保护变量(_)，私有变量(__)

from abc import ABC, abstractmethod
from typing import Any

class Soldier(ABC):
    def __init__(self, name, health, power, armor) -> None:
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
    
    def __str__(self):
        '''
        自我介绍
        '''
        return f"{self.name}, has {self.health} health, {self.power} power, {self.armor} armor"

    @abstractmethod
    def attack(self, enermy):
        pass 

class Footman(Soldier):
    def __init__(self, name, health, power, armor, rebound=0.2) -> None:
        super().__init__(name, health, power, armor) #初始化父类
        self.state = 'offense'
        self.rebound = rebound
    
    def defense_state(self):
        if self.state=='offense':
            self.armor *= 2
            self.power /= 2
            self.state = 'defense'

    def __str__(self):
        return super().__str__() + f", {self.state} state"
    
    def offense_state(self):
        if self.state=='defense':
            self.armor /= 2
            self.power *= 2
            self.state = 'offense'

    def attack(self, enermy):
        return super().attack(enermy)

class Knight(Soldier):
    def __init__(self, name, health, power, armor, weapon) -> None:
        super().__init__(name, health, power, armor)
        self.__weapon = weapon
        self.weapon_damage = {"arrow": 5, "lance": 10}
    
    @property
    def get_weapon(self):
        return self.__weapon

    def attack(self, enermy):
        damage = max(0, self.power + self.weapon_damage[self.__weapon] - enermy.armor)
        enermy.health -= damage
    
    def __str__(self):
        return super().__str__() + f", use {self.__weapon}"
    
# bob = Footman(name='bob', health=50, power=10, armor=1, rebound=0.1)
# kevin = Knight("kelvin", 100, 10, 2, weapon='lance')

CONSTANT_NUM = 10
soldier_name = "bob"
#SoldierCommandor
#soldierCommandor

class Test:
    def __init__(self, x) -> None:
        self.x = x

    def __str__(self):
        return f"My id:{self.x}, str"
    
    def __repr__(self) -> str:
        return f"My id:{self.x}, repr"

    def __len__(self):
        return self.x + 1

    def __call__(self, y):
        return self.x + y
    
    def __getitem__(self, index):
        if type(index)==str:
            return str(self.x)+index
        return self.x + index

    def __index__(self):
        return self.x+2
    
    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x
    
    def __eq__(self, other):
        return self.x==other.x-10
    
    def __add__(self, other):
        return Test(self.x+other.x)
    
    def __mul__(self, other):
        if type(other)==int:
            return Test(self.x*other)
        return Test(self.x**2+other.x**2)
    
    def __matmul__(self, other):
        return self.x + other.x + 1

test = Test(10)

#print(str(test))
#print(len(test))
#print(test(20)) # test.__call__(20)
# print(test[3]) # test.__getitem__(3)
# print(test["asd"]) # test.__getitem__("asd")
# c = [i for i in range(20)]
# print(c[test])

test2 = Test(20)
# print(test < test2) # test.__lt__(test2)
# test3 = Test(2)
# a = [test, test2, test3]
# print(sorted(a))


#print(test==test2)
#print(test+test2)
#print(test*test2)
#print(test@test2)
#print(test*3)

# class Soldier:
#     def __init__(self, power, armor) -> None:
#         self.power = power
#         self.armor = armor
    
#     def __lt__(self, other):
#         if self.power + self.armor < other.power + other.armor:
#             return True
#         else:
#             return False
        
#     # def __str__(self) -> str:
#     #     return f"{self.power + self.armor}"
    
#     def __repr__(self) -> str:
#         return f"{self.power + self.armor:.3f}"

# import numpy as np
# def random_number():
#     return np.random.rand(1).item()*10
# army = [Soldier(random_number(), random_number()) for _ in range(5)]
# print(army)
# print(sorted(army))

# 算法有问题
# class Soldier:
#     def __init__(self, power, armor) -> None:
#         self.power = power
#         self.armor = armor
    
#     def __lt__(self, other):
#         if self.power < other.armor :
#             return True
#         else:
#             return False
        
    
#     def __repr__(self) -> str:
#         return f"({self.power:.3f}, {self.armor:.3f})"

# import numpy as np
# def random_number():
#     return np.random.rand(1).item()*10
# army = [Soldier(random_number(), random_number()) for _ in range(5)]
# print(army)
# print(sorted(army))
class A:
    pass 

class Soldier:
    def __init__(self, power, armor) -> None:
        self.power = power
        self.armor = armor
    
    def __lt__(self, other):
        if self.power + self.armor < other.power + other.armor:
            return True
        else:
            return False
        
    # def __str__(self) -> str:
    #     return f"{self.power + self.armor}"
    
    def __repr__(self) -> str:
        return f"{self.power + self.armor:.3f}"

    def __getattr__(self, name):
        return "do not have " + name

    def __getattribute__(self, name: str) -> Any:
        #return  super.__dict__[name]
        print("get into getattribution")
        return super().__getattribute__(name)
        #return "have " + __name
    def __setattr__(self, name, value):
        print(f"set attr {name}, value {value}!")
        self.__dict__[name] = value

soldier1 = Soldier(10, 20)
# print(dir(soldier1))
# print(soldier1.__dict__)
# print(Soldier.__name__)
# print(isinstance(soldier1, Soldier))
# print(hasattr(soldier1, "power"))
# print(getattr(soldier1, "power1", 5))
setattr(soldier1, "magic", 50)
# print(soldier1.magic)
print(soldier1.power)
