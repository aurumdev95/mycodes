class Benjamin:
    def __init__(self, id, speed, mana, hp):
        self.id = id
        self.speed = speed
        self.mana = mana
        self.hp = hp 
        self.ready = False
        self.inventory_items = ["grenades","rifle","pistol"]
        self.val = len(self.inventory_items)

    def intro(self):
        print(f"I am benjamin ID:{self.id},my specs are -speed:{self.speed} \
            -mana:{self.mana} \
            -health power:{self.hp} \
            -inventory:{self.inventory_items}" 
            )
# use this to represent inventory(",".join(inventory_ items)
    def deploy(self):
        if self.ready == False and self.hp > 100:
            self.ready = True
            print(f"{self.id} is ready for action....")
        else:
            self.ready = False
            print(f"{self.id} is withdrawing from duty.....")   
    def inventory_update(self , inve_add_item, perm):
    
        self.add = inve_add_item
        self.really = perm
        if self.add != "" and self.really == True:
            self.inventory_items.append(self.add)
            print(f"now, I {self.id} have {self.inventory_items} ")
        else:
             print("invalid input.....")
    
    def attack(self):
        if self.ready == True:
            print("attack operation start......")
            while self.hp > 0 and self.mana > 0:
                
                    
                    
                    
                self.hp -= 50
                self.mana = self.mana / (self.val * (self.speed / 20))
                print(f"attack in progress....... \
                  -hp:{self.hp} \
                  -mana:{self.mana}")
                
                    
            print("......attack operation complete..")
            self.ready = False