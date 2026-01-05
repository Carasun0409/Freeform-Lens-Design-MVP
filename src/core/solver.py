class LensDesignSolver:
    def __init__(self, config, io_manager):
        """
        Initialize the LensDesignSolver.
        
        Args:
            config (dict): Configuration dictionary.
            io_manager (IOManager): Instance of IOManager for saving results.
        """
        self.config = config
        self.io_manager = io_manager
        self.lens_params = config.get('lens_params', {})
        self.simulation_params = config.get('simulation', {})

    def run(self):
        """
        Run the design simulation.
        """
        material = self.lens_params.get('material', 'Unknown')
        print(f"Starting design simulation for {material} lens...")
        print(f"Lens Parameters: {self.lens_params}")
        
        max_iter = self.simulation_params.get('max_iter', 10)
        save_interval = self.simulation_params.get('save_interval', 1)
        
        for step in range(1, max_iter + 1):
            # Simulate design calculation step
            # current_state = ... calculation ...
            current_state = {"step": step, "info": "dummy data"}
            
            # Check if we need to save this step
            if step % save_interval == 0:
                self.io_manager.save_state(current_state, step)
                
        print("Simulation completed.")
