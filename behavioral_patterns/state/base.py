# Step 1: Define the State Interface
class State:
    """Interface defining the methods for various states."""
    def handle_state(self):
        """Abstract method to handle state behavior."""
        pass


# Step 2: Create Concrete State Classes
class ConcreteStateA(State):
    """Concrete state representing State A."""
    def handle_state(self):
        """Handle State A behavior."""
        print("Handling State A behaviour.")


class ConcreteStateB(State):
    """Concrete state representing State B."""
    def handle_state(self):
        """Handle State B behaviour."""
        print("Handling State B behaviour.")


class ConcreteStateC(State):
    """Concrete state representing State C."""
    def handle_state(self):
        """Handle State C behaviour."""
        print("Handling State C behaviour.")


# Step 3: Create the Context Class
class Context:
    """Context class managing the states."""
    def __init__(self, state):
        """Initiliaze with a state."""
        self._state = state

    def change_state(self, state):
        """Change the current state."""
        self._state = state

    def request_state_action(self):
        """Perform an action based on the current state."""
        self._state.handle_state()


# Step 4: Example of Usage
if __name__ == "__main__":
    # Create instance of different states
    state_a = ConcreteStateA()
    state_b = ConcreteStateB()
    state_c = ConcreteStateC()

    # Initiliaze the context with State A
    context = Context(state_a)
    context.request_state_action()  # Output: Handling State A behaviour

    # Change the state to State B
    context.change_state(state_b)
    context.request_state_action()  # Output: Handling State B behaviour

    # Change the state State C
    context.change_state(state_c)
    context.request_state_action()  # Output: Handling State C behaviour
