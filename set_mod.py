set_1 = {"apple", "banana", "cherry"}
set_2 = {"google", "microsoft", "apple"}

class CustomSet(set):
    def __init__(self, var_set_1, var_set_2): # Constructor, Constructor Parameter
        self.input_set = var_set_1
        self.output_set = var_set_2

    def custom_intersection_update(self, ): # custom_intersection_update() - Method
        inter = self.input_set.intersection(self.output_set)
        self.input_set.clear()
        self.input_set.add(inter.pop())
        return None # Return Value

object_1 = CustomSet(set_1, set_2) # Object - Class - CustomSet()

object_1.custom_intersection_update()
object_1.input_set