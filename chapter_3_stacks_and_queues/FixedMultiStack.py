from enum import Enum


class StackName(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2


class FixedStack:
    def __init__(self, num_stacks, individual_stack_size):
        if individual_stack_size < 2:
            raise MemoryError("Size of each stack must be at least 2")
        self.space = [0]*(individual_stack_size*num_stacks)
        self.stack_tops = [0, int(individual_stack_size*num_stacks/3), int((2*individual_stack_size*num_stacks)/3)]
        self.sizes = [3]*num_stacks

    def is_full(self, stack_name):
        return self.sizes[stack_name.value] == 0

    def _top_of_stack_index(self, stack_name):
        return self.stack_tops[stack_name.value]

    def push(self, stack_name, value):
        if not self.is_full(stack_name):
            insert_index = self.stack_tops[stack_name.value]
            self.stack_tops[stack_name.value] += 1
            self.space[insert_index] = value
            self.sizes[stack_name.value] -= 1

    def pop(self, stack_name):
        if self.is_full(stack_name):
            raise ValueError("stack is empty")
        delete_index = self._top_of_stack_index(stack_name)-1
        popped_item = self.space[delete_index]
        self.stack_tops[stack_name.value] -= 1
        self.space[delete_index] = 0
        self.sizes[stack_name.value] += 1
        return popped_item

    def peek(self, stack_name):
        return self.space


multi_stack = FixedStack(3,3)

multi_stack.push(StackName.ZERO, "Hello")
multi_stack.push(StackName.ZERO, "World")
multi_stack.push(StackName.ONE, "Hola")
multi_stack.push(StackName.ONE, "Mundo")
multi_stack.pop(StackName.ZERO)
print(multi_stack.space)
