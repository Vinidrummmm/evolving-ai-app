# memory_ai.py

class EvolveMemoryAI:
    def __init__(self, memory_capacity=100):
        self.memory = []
        self.memory_capacity = memory_capacity

    def remember(self, experience):
        """Adds a new experience to memory, evicting the oldest if full."""
        if len(self.memory) >= self.memory_capacity:
            self.memory.pop(0)  # Remove the oldest memory
        self.memory.append(experience)

    def evolve_memory(self, evolution_fn):
        """Applies an evolution function to each memory."""
        self.memory = [evolution_fn(mem) for mem in self.memory]

# Example usage
def strengthen_memory(memory):
    return f"Strengthened-{memory}"

if __name__ == "__main__":
    ai = EvolveMemoryAI(memory_capacity=5)
    for i in range(7):
        ai.remember(f"Experience-{i}")
    print("Before Evolution:", ai.memory)
    ai.evolve_memory(strengthen_memory)
    print("After Evolution:", ai.memory)