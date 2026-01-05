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
        # Use .get() here is fine for initialization, but we will validate strictly in run()
        self.lens_params = config.get('lens_params', {})
        self.simulation_params = config.get('simulation', {})

    def run(self):
        """
        Run the design simulation.
        """
        # 1. Strong Parameter Validation
        required_params = ['material', 'refractive_index', 'radius']
        for param in required_params:
            if param not in self.lens_params:
                raise ValueError(f"错误：配置文件缺少必要参数 [{param}]")

        # 2. Extract parameters (safe now)
        material = self.lens_params['material']
        radius = self.lens_params['radius']
        
        # 3. Professional Logging (Initialization)
        print(f">>> [初始化] 正在加载设计参数：材料={material}, 半径={radius}...")
        
        # Default fallback is only allowed for simulation control params if not critical
        max_iter = self.simulation_params.get('max_iter', 10)
        save_interval = self.simulation_params.get('save_interval', 1)
        
        for step in range(1, max_iter + 1):
            # 4. Professional Logging (Calculation)
            print(f">>> [计算] 正在执行第 {step}/{max_iter} 步迭代...")
            
            # Simulate design calculation step
            current_state = {"step": step, "info": "dummy data"}
            
            # Check if we need to save this step
            if step % save_interval == 0:
                self.io_manager.save_state(current_state, step)
                
        print(">>> [完成] 模拟设计流程结束。")
