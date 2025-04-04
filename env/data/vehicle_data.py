Truths = {'Ethanol Engine (Flex Fuel)', 'Variable Compression Engine', 'Continuously Variable Transmission (CVT) Petrol Engine', 'Liquefied Petroleum Gas (LPG) Engine', 'Homogeneous Charge Compression Ignition (HCCI) Engine', 'Turbodiesel Engine', 'Turbocharged Direct Injection (TDI) Diesel', 'Turbocharged Diesel Engine', 'Variable Valve Timing Engine', 'Electric Engine with Ultra Capacitor', 'Adiabatic Engine', 'Electric Engine with Inductive Charging', 'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Diesel-Electric Hybrid', 'Supercharged Petrol Engine', 'Plug-in Hybrid Electric Vehicle (PHEV)', 'Diesel Engine', 'Electric Engine with Range Extender', 'Fuel Cell Electric Vehicle with Battery', 'Petrol Engine with Cylinder Deactivation', 'Compressed Air Hybrid Engine', 'Water-Cooled Engine', 'Atkinson Cycle Engine', 'Steam Engine', 'Bi-Fuel Engine (Petrol/LPG)', 'Electric Engine with Solid-State Battery', 'Petrol Engine - 3-cylinder', 'Miller Cycle Engine', 'Petrol Engine - V8', 'Rotary Engine (Wankel)', 'Plug-in Hybrid', 'Cylinder Deactivation Engine', 'Series Hybrid Engine', 'Petrol Supercharged Engine', 'Inline Engine', 'Hybrid Engine - Full Hybrid', 'Diesel Engine with Start-Stop System', 'Hybrid Engine - Mild Hybrid', 'Boxer Engine - Petrol', 'Diesel Engine with Variable Geometry Turbocharger', 'Hybrid Engine', 'Petrol Engine with Atkinson Cycle', 'Air-Cooled Engine', 'Common Rail Direct Injection (CRDI) Diesel', 'Micro Hybrid Engine (Start-Stop system)', 'Petrol Engine with Variable Compression Ratio (VCR)', 'Petrol Turbocharged Engine', 'Petrol Engine with GDI (Gasoline Direct Injection)', 'Diesel Electric Hybrid', 'Petrol Engine with Variable Valve Timing (VVT)', 'V-Type Engine', 'Petrol Engine with Port Injection', 'Rotary (Wankel) Engine', 'Compressed Natural Gas (CNG) Engine', 'Biofuel Engine', 'Series Hybrid', 'Diesel Engine - Inline 4-cylinder', 'Turbocharged Petrol Engine', 'Diesel Engine with Twin Turbo', 'Hydrogen Internal Combustion Engine', 'Petrol Engine with Start-Stop System', 'Ethanol Engine', 'Propane (LPG) Engine', 'Hydrogen Fuel Cell', 'Boxer Engine - Diesel', 'Diesel Engine - V6', 'Turbocharged Compressed Natural Gas Engine', 'High-Performance Engines', 'Direct Injection Petrol Engine', 'Petrol Engine - Inline 4-cylinder', 'Direct Injection Diesel Engine', 'Air Powered Engine', 'Methanol Fuel Cell Engine', 'Boxer Engine', 'Electric Motor - Dual Motor (AWD)', 'Petrol Engine', 'Stirling Engine', 'Diesel Turbocharged Engine', 'Start-Stop System Engine', 'Diesel Engine - 3-cylinder', 'Flexible Fuel Engine', 'Electric Motor', 'Range Extender Electric Vehicle', 'Multi-Fuel Engine', 'Indirect Injection Diesel Engine', 'Two-stroke Petrol Engine', 'Mild Hybrid', 'Gas Turbine Engine', 'Petrol Engine with Twincharger', 'Diesel Engine with HCCI (Homogeneous Charge Compression Ignition)', 'Parallel Hybrid', 'Micro Hybrid System', 'Opposed Piston Engine', 'Bi-Fuel Engine (Petrol/CNG)', 'Lean Burn Engine', 'Petrol Engine with Direct Injection', 'Four-stroke Petrol Engine', 'Bi-Fuel Engine', 'Electric Motor - Single Motor', 'Diesel Engine with AdBlue Injection', 'Biodiesel Engine', 'Dual Clutch Transmission Petrol Engine', 'Petrol Engine - V6', 'Parallel Hybrid Engine', 'Solar Powered Electric Vehicle', 'External Combustion Engine', 'Diesel Engine with Particulate Filter'}
Actions = {'Fuel Octane Requirement Test', 'Engine Brake Test', 'Electric Range Test', 'High Altitude Performance Test', 'Ignition Timing Test', 'Engine Weight Measurement', 'Cooling System Efficiency Test', 'Engine Compression Test', 'Emissions Testing', 'Hydrogen Emission Test', 'Fuel Type Detection', 'Variable Valve Timing Test', 'OBD Diagnostics Readout', 'Exhaust Temperature Measurement', 'Cylinder Deactivation Test', 'Combustion Chamber Visualization', 'Fuel Consumption Testing', 'Catalytic Converter Efficiency Test', 'Regeneration Cycle Testing', 'Cold Start Test', 'Battery Health Monitoring', 'Regenerative Braking Efficiency Test', 'Battery Capacity Test', 'Alternative Fuel Compatibility Test', 'Noise Level Measurement', 'Fuel Cell Output Measurement', 'Acceleration Test', 'Turbo Lag Measurement', 'Hybrid System Efficiency Test', 'Emission Particulate Analysis', 'Drive Range Test', 'Torque Measurement', 'Idle Vibration Measurement', 'Energy Recuperation Test', 'Start-Stop System Test', 'Battery Recharging Rate Test', 'Start-Stop Functionality Test', 'Electric Consumption Test', 'Heat Dissipation Test', 'Fuel Vapor Emission Test', 'Reliability Test under Load', 'Lubricant Consumption Test', 'Knock Sensor Test', 'Exhaust Gas Analysis', 'Engine Size Measurement', 'Fuel Injection Pressure Test', 'Engine Thermal Efficiency Test'}
Outcomes = {
    'Fuel Consumption Testing': {
        'type': 'float',
        'states': {
            (0.0, 3.0): {'Two-stroke Petrol Engine', 'Rotary (Wankel) Engine', 'Diesel Engine', 'Turbocharged Petrol Engine', 'Supercharged Petrol Engine', 'Petrol Engine'},
            (3.0, 6.0): {'Rotary (Wankel) Engine', 'Gas Turbine Engine', 'Two-stroke Petrol Engine'},
            (6.0, 9.0): {'Hydrogen Fuel Cell', 'Battery Electric Vehicle (BEV)', 'Fuel Cell Electric Vehicle (FCEV)', 'Electric Motor'},
            (9.0, 15.0): {'Electric Motor', 'Hydrogen Fuel Cell', 'Plug-in Hybrid', 'Fuel Cell Electric Vehicle (FCEV)', 'Hybrid Engine', 'Battery Electric Vehicle (BEV)'},
            (15.0, 100.0): {'Electric Motor', 'Hydrogen Fuel Cell', 'Plug-in Hybrid', 'Mild Hybrid', 'Battery Electric Vehicle (BEV)', 'Hybrid Engine', 'Fuel Cell Electric Vehicle (FCEV)'}
        }
    },
    'Exhaust Gas Analysis': {
        'type': 'str',
        'states': {
            'Zero Emissions': {'Compressed Natural Gas (CNG) Engine', 'Turbocharged Diesel Engine', 'Biofuel Engine', 'Turbocharged Petrol Engine', 'Supercharged Petrol Engine', 'Bi-Fuel Engine', 'Hydrogen Internal Combustion Engine', 'Ethanol Engine', 'Petrol Engine', 'Diesel Engine', 'Propane (LPG) Engine'},
            'Low Emissions': {'Rotary (Wankel) Engine', 'Gas Turbine Engine', 'Two-stroke Petrol Engine'},
            'High Emissions': {'Electric Motor', 'Hydrogen Fuel Cell', 'Plug-in Hybrid', 'Mild Hybrid', 'Battery Electric Vehicle (BEV)', 'Hybrid Engine', 'Fuel Cell Electric Vehicle (FCEV)'}
        }
    },
    'Acceleration Test': {
        'type': 'float',
        'states': {
            (0.0, 5.0): {'Hydrogen Fuel Cell', 'Hybrid Engine', 'Diesel Engine', 'Battery Electric Vehicle (BEV)', 'Two-stroke Petrol Engine'},
            (5.0, 8.0): {'Hydrogen Fuel Cell', 'Battery Electric Vehicle (BEV)', 'Hybrid Engine'},
            (8.0, 12.0): set(),
            (12.0, 30.0): {'Hydrogen Fuel Cell', 'Plug-in Hybrid', 'Mild Hybrid', 'Electric Motor', 'Hybrid Engine'}
        }
    },
    'Noise Level Measurement': {
        'type': 'float',
        'states': {
            (0.0, 50.0): {'Diesel Engine', 'Petrol Engine', 'Two-stroke Petrol Engine', 'Rotary (Wankel) Engine'},
            (50.0, 70.0): {'Hydrogen Fuel Cell', 'Battery Electric Vehicle (BEV)', 'Fuel Cell Electric Vehicle (FCEV)', 'Electric Motor'},
            (70.0, 120.0): {'Plug-in Hybrid', 'Mild Hybrid', 'Hybrid Engine'}
        }
    },
    'Emissions Testing': {
        'type': 'str',
        'states': {
            'Pass': {'Diesel Engine', 'Turbocharged Diesel Engine', 'Two-stroke Petrol Engine', 'Rotary (Wankel) Engine'},
            'Fail': {'Hydrogen Fuel Cell', 'Battery Electric Vehicle (BEV)', 'Fuel Cell Electric Vehicle (FCEV)', 'Electric Motor'}
        }
    },
    'Electric Consumption Test': {
        'type': 'float',
        'states': {
            (0.0, 15.0): {'Two-stroke Petrol Engine', 'Rotary (Wankel) Engine', 'Diesel Engine', 'Turbocharged Petrol Engine', 'Supercharged Petrol Engine', 'Petrol Engine'},
            (15.0, 30.0): {'Diesel Engine', 'Turbocharged Petrol Engine', 'Supercharged Petrol Engine', 'Petrol Engine'},
            (30.0, 100.0): set()
        }
    },
    'Cold Start Test': {
        'type': 'str',
        'states': {
            'Successful Start': {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'},
            'Hard Start': {'Diesel Engine', 'Two-stroke Petrol Engine'},
            'Failed Start': {'Hydrogen Fuel Cell', 'Ethanol Engine'}
        }
    },
    'Idle Vibration Measurement': {
        'type': 'float',
        'states': {
            (0.0, 1.0): {'Two-stroke Petrol Engine', 'Rotary (Wankel) Engine'},
            (1.0, 3.0): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'},
            (3.0, 10.0): set()
        }
    },
    'Torque Measurement': {
        'type': 'float',
        'states': {
            (0.0, 150.0): {'Diesel Engine', 'Electric Motor'},
            (150.0, 300.0): {'Electric Motor', 'Petrol Engine'},
            (300.0, 1000.0): {'Diesel Engine', 'Petrol Engine'}
        }
    },
    'Engine Thermal Efficiency Test': {
        'type': 'float',
        'states': {
            (0.0, 25.0): {'Diesel Engine', 'Atkinson Cycle Engine'},
            (25.0, 40.0): {'Miller Cycle Engine', 'Petrol Engine'},
            (40.0, 100.0): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)'}
        }
    },
    'Alternative Fuel Compatibility Test': {
        'type': 'str',
        'states': {
            'Compatible': {'Bi-Fuel Engine', 'Flexible Fuel Engine', 'Ethanol Engine', 'Petrol Engine', 'Diesel Engine'},
            'Not Compatible': {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Regeneration Cycle Testing': {
        'type': 'str',
        'states': {
            'Active Regeneration': {'Diesel Engine', 'Turbocharged Diesel Engine', 'Turbodiesel Engine'},
            'Passive Regeneration': {'Petrol Engine'},
            'No Regeneration': {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Turbo Lag Measurement': {
        'type': 'float',
        'states': {
            (0.0, 1.0): {'Battery Electric Vehicle (BEV)', 'Supercharged Petrol Engine', 'Electric Motor'},
            (1.0, 2.0): {'Turbocharged Petrol Engine', 'Turbocharged Diesel Engine'},
            (2.0, 10.0): {'Diesel Engine', 'Petrol Engine', 'Rotary (Wankel) Engine'}
        }
    },
    'High Altitude Performance Test': {
        'type': 'str',
        'states': {
            'No Performance Loss': {'Turbocharged Petrol Engine', 'Turbocharged Diesel Engine', 'Supercharged Petrol Engine', 'Electric Motor'},
            'Performance Loss': {'Diesel Engine', 'Petrol Engine', 'Rotary (Wankel) Engine'}
        }
    },
    'Fuel Type Detection': {
        'type': 'str',
        'states': {
            'Petrol': {'Diesel Engine', 'Battery Electric Vehicle (BEV)', 'Fuel Cell Electric Vehicle (FCEV)', 'Electric Motor'},
            'Diesel': {'Petrol Engine', 'Battery Electric Vehicle (BEV)', 'Fuel Cell Electric Vehicle (FCEV)', 'Electric Motor'},
            'Electric': {'Diesel Engine', 'Petrol Engine'},
            'Hydrogen': {'Diesel Engine', 'Petrol Engine', 'Electric Motor'}
        }
    },
    'Reliability Test under Load': {
        'type': 'float',
        'states': {
            (0.0, 100.0): {'Two-stroke Petrol Engine', 'Rotary (Wankel) Engine'},
            (100.0, 500.0): set(),
            (500.0, 1000.0): {'Two-stroke Petrol Engine', 'Rotary (Wankel) Engine'}
        }
    },
    'Engine Weight Measurement': {
        'type': 'float',
        'states': {
            (0.0, 200.0): {'Diesel Engine', 'Hybrid Engine'},
            (200.0, 500.0): {'Diesel Engine', 'Battery Electric Vehicle (BEV)', 'Fuel Cell Electric Vehicle (FCEV)'},
            (500.0, 2000.0): {'Electric Motor', 'Petrol Engine'}
        }
    },
    'Lubricant Consumption Test': {
        'type': 'float',
        'states': {
            (0.0, 0.5): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'},
            (0.5, 1.0): set(),
            (1.0, 5.0): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Engine Compression Test': {
        'type': 'float',
        'states': {
            (0.0, 8.0): {'Diesel Engine', 'Turbocharged Diesel Engine'},
            (8.0, 12.0): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'},
            (12.0, 20.0): set()
        }
    },
    'Exhaust Temperature Measurement': {
        'type': 'float',
        'states': {
            (0.0, 200.0): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'},
            (200.0, 500.0): {'Diesel Engine', 'Turbocharged Diesel Engine'},
            (500.0, 1000.0): {'Turbocharged Petrol Engine', 'Supercharged Petrol Engine', 'Petrol Engine'}
        }
    },
    'Fuel Injection Pressure Test': {
        'type': 'float',
        'states': {
            (0.0, 1500.0): {'Diesel Engine', 'Turbocharged Diesel Engine'},
            (1500.0, 3000.0): {'Direct Injection Petrol Engine', 'Petrol Engine'},
            (3000.0, 5000.0): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Battery Recharging Rate Test': {
        'type': 'float',
        'states': {
            (0.0, 30.0): {'Diesel Engine', 'Hydrogen Fuel Cell', 'Petrol Engine'},
            (30.0, 60.0): set(),
            (60.0, 120.0): {'Diesel Engine', 'Hydrogen Fuel Cell', 'Petrol Engine'}
        }
    },
    'Drive Range Test': {
        'type': 'float',
        'states': {
            (0.0, 300.0): {'Diesel Engine', 'Petrol Engine'},
            (300.0, 600.0): set(),
            (600.0, 1000.0): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Emission Particulate Analysis': {
        'type': 'str',
        'states': {
            'High Particulates': {'Diesel Engine', 'Turbocharged Diesel Engine', 'Turbodiesel Engine'},
            'Low Particulates': {'Petrol Engine', 'Battery Electric Vehicle (BEV)', 'Fuel Cell Electric Vehicle (FCEV)', 'Electric Motor'}
        }
    },
    'Knock Sensor Test': {
        'type': 'str',
        'states': {
            'Knock Detected': {'Turbocharged Petrol Engine', 'Supercharged Petrol Engine', 'Petrol Engine'},
            'No Knock': {'Diesel Engine', 'Battery Electric Vehicle (BEV)', 'Fuel Cell Electric Vehicle (FCEV)', 'Electric Motor'}
        }
    },
    'Catalytic Converter Efficiency Test': {
        'type': 'float',
        'states': {
            (0.0, 50.0): {'Rotary (Wankel) Engine', 'Two-stroke Petrol Engine'},
            (50.0, 90.0): {'Diesel Engine', 'Petrol Engine'},
            (90.0, 100.0): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Engine Brake Test': {
        'type': 'float',
        'states': {
            (0.0, 100.0): {'Battery Electric Vehicle (BEV)', 'Electric Motor'},
            (100.0, 200.0): {'Diesel Engine', 'Petrol Engine'},
            (200.0, 500.0): {'Turbocharged Petrol Engine', 'Turbocharged Diesel Engine'}
        }
    },
    'Hybrid System Efficiency Test': {
        'type': 'float',
        'states': {
            (0.0, 50.0): {'Diesel Engine', 'Petrol Engine', 'Electric Motor'},
            (50.0, 80.0): {'Mild Hybrid'},
            (80.0, 100.0): {'Plug-in Hybrid', 'Hybrid Engine', 'Series Hybrid', 'Parallel Hybrid'}
        }
    },
    'Start-Stop System Test': {
        'type': 'str',
        'states': {
            'Functional': {'Plug-in Hybrid', 'Start-Stop System Engine', 'Hybrid Engine'},
            'Non-Functional': {'Diesel Engine', 'Petrol Engine', 'Electric Motor'}
        }
    },
    'Cylinder Deactivation Test': {
        'type': 'str',
        'states': {
            'Active': {'Cylinder Deactivation Engine'},
            'Inactive': {'Diesel Engine', 'Petrol Engine', 'Electric Motor'}
        }
    },
    'Variable Valve Timing Test': {
        'type': 'str',
        'states': {
            'VVT Present': {'Variable Valve Timing Engine', 'Turbocharged Petrol Engine'},
            'No VVT': {'Diesel Engine', 'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Cooling System Efficiency Test': {
        'type': 'float',
        'states': {
            (0.0, 50.0): {'Air-Cooled Engine', 'Rotary (Wankel) Engine'},
            (50.0, 90.0): {'Water-Cooled Engine'},
            (90.0, 100.0): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Fuel Vapor Emission Test': {
        'type': 'str',
        'states': {
            'High Vapor Emissions': {'Ethanol Engine', 'Petrol Engine'},
            'Low Vapor Emissions': {'Diesel Engine', 'Electric Motor'}
        }
    },
    'OBD Diagnostics Readout': {
        'type': 'str',
        'states': {
            'Code P0300': {'Turbocharged Petrol Engine', 'Petrol Engine'},
            'Code P0400': {'Diesel Engine', 'Turbocharged Diesel Engine'},
            'No Codes': {'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Engine Size Measurement': {
        'type': 'float',
        'states': {
            (0.0, 1.5): {'Micro Hybrid System', 'Battery Electric Vehicle (BEV)', 'Electric Motor'},
            (1.5, 3.0): {'Diesel Engine', 'Petrol Engine'},
            (3.0, 10.0): {'Turbocharged Diesel Engine', 'Gas Turbine Engine'}
        }
    },
    'Fuel Octane Requirement Test': {
        'type': 'float',
        'states': {
            (0.0, 87.0): {'Diesel Engine', 'Electric Motor'},
            (87.0, 91.0): {'Turbocharged Petrol Engine', 'Petrol Engine'},
            (91.0, 100.0): {'High-Performance Engines', 'Supercharged Petrol Engine'}
        }
    },
    'Combustion Chamber Visualization': {
        'type': 'str',
        'states': {
            'Direct Injection': {'Direct Injection Petrol Engine', 'Direct Injection Diesel Engine'},
            'Indirect Injection': {'Petrol Engine', 'Indirect Injection Diesel Engine'},
            'No Combustion Chamber': {'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Ignition Timing Test': {
        'type': 'str',
        'states': {
            'Advanced Timing': {'Turbocharged Petrol Engine', 'Petrol Engine'},
            'Retarded Timing': {'Diesel Engine'},
            'No Ignition System': {'Battery Electric Vehicle (BEV)', 'Electric Motor'}
        }
    },
    'Fuel Cell Output Measurement': {
        'type': 'float',
        'states': {
            (0.0, 50.0): {'Diesel Engine', 'Petrol Engine'},
            (50.0, 100.0): {'Fuel Cell Electric Vehicle (FCEV)'},
            (100.0, 200.0): {'Hydrogen Fuel Cell'}
        }
    },
    'Regenerative Braking Efficiency Test': {
        'type': 'float',
        'states': {
            (0.0, 12.0): {'Diesel Engine', 'Petrol Engine'},
            (12.0, 25.0): set(),
            (25.0, 100.0): {'Diesel Turbocharged Engine', 'Petrol Engine - V6', 'Electric Motor'}
        }
    },
    'Battery Capacity Test': {
        'type': 'float',
        'states': {
            (0.0, 1.0): {
                'Diesel Electric Hybrid', 'Range Extender Electric Vehicle', 'Electric Motor', 
                'Electric Engine with Solid-State Battery', 'Mild Hybrid', 
                'Electric Engine with Ultra Capacitor', 'Electric Engine with Inductive Charging', 
                'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 
                'Plug-in Hybrid', 'Series Hybrid Engine', 'Parallel Hybrid', 'Micro Hybrid System', 
                'Diesel-Electric Hybrid', 'Series Hybrid', 'Hybrid Engine - Full Hybrid', 
                'Electric Motor - Single Motor', 'Hybrid Engine - Mild Hybrid', 
                'Plug-in Hybrid Electric Vehicle (PHEV)', 'Hybrid Engine', 
                'Electric Engine with Range Extender', 'Fuel Cell Electric Vehicle with Battery', 
                'Compressed Air Hybrid Engine', 'Micro Hybrid Engine (Start-Stop system)', 
                'Electric Motor - Dual Motor (AWD)', 'Solar Powered Electric Vehicle', 
                'Parallel Hybrid Engine'
            },
            (1.0, 10.0): set(),
            (10.0, 100.0): {
                'Stirling Engine', 'Petrol Turbocharged Engine', 'Petrol Engine with GDI (Gasoline Direct Injection)', 
                'Ethanol Engine (Flex Fuel)', 'Variable Compression Engine', 'Diesel Turbocharged Engine', 
                'Start-Stop System Engine', 'Diesel Engine - 3-cylinder', 'Continuously Variable Transmission (CVT) Petrol Engine', 
                'Liquefied Petroleum Gas (LPG) Engine', 'Homogeneous Charge Compression Ignition (HCCI) Engine', 
                'Flexible Fuel Engine', 'Indirect Injection Diesel Engine', 'V-Type Engine', 'Multi-Fuel Engine', 
                'Bi-Fuel Engine (Petrol/LPG)', 'Petrol Engine with Variable Valve Timing (VVT)', 'Turbodiesel Engine', 
                'Two-stroke Petrol Engine', 'Petrol Engine with Port Injection', 'Petrol Engine - 3-cylinder', 
                'Turbocharged Diesel Engine', 'Gas Turbine Engine', 'Petrol Engine with Twincharger', 
                'Rotary (Wankel) Engine', 'Diesel Engine with HCCI (Homogeneous Charge Compression Ignition)', 
                'Variable Valve Timing Engine', 'Miller Cycle Engine', 'Adiabatic Engine', 'Petrol Engine - V8', 
                'Rotary Engine (Wankel)', 'Cylinder Deactivation Engine', 'Petrol Supercharged Engine', 
                'Inline Engine', 'Opposed Piston Engine', 'Compressed Natural Gas (CNG) Engine', 
                'Bi-Fuel Engine (Petrol/CNG)', 'Biofuel Engine', 'Diesel Engine with Variable Geometry Turbocharger', 
                'Diesel Engine - Inline 4-cylinder', 'Turbocharged Petrol Engine', 'Diesel Engine with Twin Turbo', 
                'Lean Burn Engine', 'Supercharged Petrol Engine', 'Petrol Engine with Direct Injection', 
                'Four-stroke Petrol Engine', 'Bi-Fuel Engine', 'Hydrogen Internal Combustion Engine', 
                'Boxer Engine - Petrol', 'Ethanol Engine', 'Propane (LPG) Engine', 'Diesel Engine', 
                'Air-Cooled Engine', 'Diesel Engine with AdBlue Injection', 'Petrol Engine with Start-Stop System', 
                'Diesel Engine with Start-Stop System', 'Petrol Engine with Atkinson Cycle', 'Boxer Engine - Diesel', 
                'Diesel Engine - V6', 'Turbocharged Compressed Natural Gas Engine', 'Direct Injection Petrol Engine', 
                'Petrol Engine - Inline 4-cylinder', 'Petrol Engine with Cylinder Deactivation', 
                'Biodiesel Engine', 'Dual Clutch Transmission Petrol Engine', 'Water-Cooled Engine', 
                'Petrol Engine - V6', 'Atkinson Cycle Engine', 'Air Powered Engine', 'Boxer Engine', 
                'Methanol Fuel Cell Engine', 'External Combustion Engine', 
                'Petrol Engine with Variable Compression Ratio (VCR)', 'Petrol Engine', 'Steam Engine', 
                'Diesel Engine with Particulate Filter'
            }
        }
    },
    'Electric Range Test': {
        'type': 'float',
        'states': {
            (0.0, 50.0): {'Two-stroke Petrol Engine', 'Rotary (Wankel) Engine', 'Diesel Engine', 'Turbocharged Petrol Engine', 'Supercharged Petrol Engine', 'Petrol Engine'},
            (50.0, 100.0): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'},
            (100.0, 1000.0): {'Diesel Engine', 'Turbocharged Petrol Engine', 'Petrol Engine'}
        }
    },
    'Start-Stop Functionality Test': {
        'type': 'str',
        'states': {
            'Functional': {
                'Ethanol Engine (Flex Fuel)', 'Variable Compression Engine', 'Continuously Variable Transmission (CVT) Petrol Engine', 
                'Liquefied Petroleum Gas (LPG) Engine', 'Homogeneous Charge Compression Ignition (HCCI) Engine', 
                'Turbodiesel Engine', 'Turbocharged Direct Injection (TDI) Diesel', 'Turbocharged Diesel Engine', 
                'Variable Valve Timing Engine', 'Adiabatic Engine', 'Supercharged Petrol Engine', 'Diesel Engine', 
                'Petrol Engine with Cylinder Deactivation', 'Compressed Air Hybrid Engine', 'Water-Cooled Engine', 
                'Atkinson Cycle Engine', 'Steam Engine', 'Bi-Fuel Engine (Petrol/LPG)', 'Petrol Engine - 3-cylinder', 
                'Miller Cycle Engine', 'Petrol Engine - V8', 'Rotary Engine (Wankel)', 'Plug-in Hybrid', 
                'Cylinder Deactivation Engine', 'Series Hybrid Engine', 'Petrol Supercharged Engine', 'Inline Engine', 
                'Hybrid Engine - Full Hybrid', 'Diesel Engine with Variable Geometry Turbocharger', 
                'Hybrid Engine - Mild Hybrid', 'Boxer Engine - Petrol', 'Petrol Engine with Atkinson Cycle', 
                'Hybrid Engine', 'Air-Cooled Engine', 'Common Rail Direct Injection (CRDI) Diesel', 
                'Micro Hybrid Engine (Start-Stop system)', 'Petrol Engine with Variable Compression Ratio (VCR)', 
                'Petrol Turbocharged Engine', 'Petrol Engine with GDI (Gasoline Direct Injection)', 
                'Petrol Engine with Variable Valve Timing (VVT)', 'V-Type Engine', 'Petrol Engine with Port Injection', 
                'Rotary (Wankel) Engine', 'Compressed Natural Gas (CNG) Engine', 'Biofuel Engine', 
                'Series Hybrid', 'Diesel Engine - Inline 4-cylinder', 'Turbocharged Petrol Engine', 
                'Diesel Engine with Twin Turbo', 'Hydrogen Internal Combustion Engine', 'Ethanol Engine', 
                'Propane (LPG) Engine', 'Hydrogen Fuel Cell', 'Boxer Engine - Diesel', 'Diesel Engine - V6', 
                'Turbocharged Compressed Natural Gas Engine', 'Direct Injection Petrol Engine', 
                'Petrol Engine - Inline 4-cylinder', 'Air Powered Engine', 'Methanol Fuel Cell Engine', 
                'Boxer Engine', 'Petrol Engine', 'Stirling Engine', 'Diesel Turbocharged Engine', 
                'Diesel Engine - 3-cylinder', 'Flexible Fuel Engine', 'Indirect Injection Diesel Engine', 
                'Multi-Fuel Engine', 'Two-stroke Petrol Engine', 'Mild Hybrid', 'Gas Turbine Engine', 
                'Petrol Engine with Twincharger', 'Diesel Engine with HCCI (Homogeneous Charge Compression Ignition)', 
                'Parallel Hybrid', 'Micro Hybrid System', 'Opposed Piston Engine', 'Bi-Fuel Engine (Petrol/CNG)', 
                'Lean Burn Engine', 'Petrol Engine with Direct Injection', 'Four-stroke Petrol Engine', 
                'Bi-Fuel Engine', 'Diesel Engine with AdBlue Injection', 'Biodiesel Engine', 
                'Dual Clutch Transmission Petrol Engine', 'Petrol Engine - V6', 'Parallel Hybrid Engine', 
                'External Combustion Engine', 'Diesel Engine with Particulate Filter'
            },
            'Non-Functional': {
                'Diesel-Electric Hybrid', 'Electric Engine with Ultra Capacitor', 'Electric Engine with Inductive Charging', 
                'Start-Stop System Engine', 'Battery Electric Vehicle (BEV)', 'Fuel Cell Electric Vehicle (FCEV)', 
                'Diesel Electric Hybrid', 'Electric Motor', 'Electric Engine with Solid-State Battery', 
                'Electric Motor - Dual Motor (AWD)', 'Electric Motor - Single Motor', 
                'Plug-in Hybrid Electric Vehicle (PHEV)', 'Solar Powered Electric Vehicle', 
                'Petrol Engine with Start-Stop System', 'Range Extender Electric Vehicle', 
                'Diesel Engine with Start-Stop System', 'Electric Engine with Range Extender', 
                'Fuel Cell Electric Vehicle with Battery'
            }
        }
    },
    'Heat Dissipation Test': {
        'type': 'float',
        'states': {
            (0.0, 250): {'Fuel Cell Electric Vehicle (FCEV)', 'Battery Electric Vehicle (BEV)', 'Electric Motor'},
            (250.0, 500): set(),
            (500.0, 1000.0): {'Diesel Turbocharged Engine', 'Petrol Engine - V6', 'Hybrid Engine'}
        }
    },
    'Energy Recuperation Test': {
        'type': 'str',
        'states': {
            'High Recuperation': {'Plug-in Hybrid', 'Battery Electric Vehicle (BEV)', 'Hybrid Engine'},
            'Low Recuperation': set()
        }
    },
    'Hydrogen Emission Test': {
        'type': 'str',
        'states': {
            'Zero Emissions': {'Diesel Engine', 'Turbocharged Diesel Engine', 'Petrol Engine'},
            'Some Emissions': {'Hydrogen Internal Combustion Engine'}
        }
    },
    'Battery Health Monitoring': {
        'type': 'float',
        'states': {
            (0.0, 50.0): {'Battery Electric Vehicle (BEV)', 'Electric Motor'},
            (50.0, 80.0): {'Electric Engine with Ultra Capacitor', 'Fuel Cell Electric Vehicle (FCEV)'},
            (80.0, 100.0): set()
        }
    }
}
