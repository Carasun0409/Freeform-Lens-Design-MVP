import time
import datetime

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
        # Start timing
        start_time = time.time()
        error_count = 0
        
        # 1. Strong Parameter Validation
        required_params = ['material', 'refractive_index', 'radius']
        for param in required_params:
            if param not in self.lens_params:
                raise ValueError(f"错误：配置文件缺少必要参数 [{param}]")

        # 2. Archive Configuration Snapshot (BEFORE simulation starts)
        self.io_manager.save_run_config(self.config)

        # 3. Extract parameters (safe now)
        material = self.lens_params['material']
        radius = self.lens_params['radius']
        
        # 4. Professional Logging (Initialization)
        print(f">>> [初始化] 正在加载设计参数：材料={material}, 半径={radius}...")
        
        # Default fallback is only allowed for simulation control params if not critical
        max_iter = self.simulation_params.get('max_iter', 10)
        save_interval = self.simulation_params.get('save_interval', 1)
        
        try:
            for step in range(1, max_iter + 1):
                # 5. Professional Logging (Calculation)
                print(f">>> [计算] 正在执行第 {step}/{max_iter} 步迭代...")
                
                # Simulate design calculation step
                # In a real scenario, we would have actual calculation data here
                current_surface_data = [
                    {"x": 1.0 * step, "y": 2.0 * step, "z": 0.5 * step},
                    {"x": 1.1 * step, "y": 2.1 * step, "z": 0.6 * step}
                ]
                
                # Check if we need to save this step
                if step % save_interval == 0:
                    # Construct self-describing data package
                    data_package = {
                        "step": step,
                        "timestamp": datetime.datetime.now().isoformat(),
                        "parameters": self.config,  # Double insurance: save parameters with data
                        "surface_data": current_surface_data
                    }
                    
                    # Format filename clearly and orderly, using .json
                    filename = f"iter_{step:03d}_data.json"
                    self.io_manager.save_state(data_package, filename)
        except Exception as e:
            error_count += 1
            print(f"❌ [运行时错误] 迭代过程中发生错误: {e}")
            # Depending on severity, we might want to break or continue. 
            # For this MVP, we re-raise to stop execution after logging/counting.
            raise e

        # End timing
        end_time = time.time()
        total_duration = end_time - start_time
        
        # Generate Report
        report_data = {
            "total_duration_seconds": round(total_duration, 4),
            "final_step": max_iter,
            "error_count": error_count,
            "completion_status": "Success" if error_count == 0 else "Failed",
            "final_merit_value": 0.001 * max_iter,  # Dummy value
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        self.io_manager.save_report(report_data)
        
        print(f">>> [完成] 模拟设计流程结束。总耗时: {total_duration:.4f}s")
