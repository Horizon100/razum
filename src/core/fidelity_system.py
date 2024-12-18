import numpy as np
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class FidelityComponents:
    """Store individual fidelity components"""
    physics: float = 0.0
    structural: float = 0.0
    behavioral: float = 0.0
    cognitive: float = 0.0
    data: float = 0.0

class FidelitySystem:
    def __init__(self):
        self.components = FidelityComponents()
        self.weights = {
            'physics': 0.2,
            'structural': 0.2,
            'behavioral': 0.2,
            'cognitive': 0.2,
            'data': 0.2
        }
        
    def calculate_physics_fidelity(self, scale_weights: Dict[int, float], 
        physical_accuracy: Dict[int, float],
        interaction_complexity: Dict[int, float],
        energy_drift: Dict[int, float]) -> float:
        """Calculate physics engine fidelity
        F_p(t) = Σ(w_s * (P_a * I_c) / E_d)
        """
        fidelity = 0.0
        for scale, weight in scale_weights.items():
            numerator = physical_accuracy[scale] * interaction_complexity[scale]
            denominator = max(energy_drift[scale], 0.001)  # Prevent division by zero
            fidelity += weight * (numerator / denominator)
            
        self.components.physics = np.clip(fidelity, 0, 1)
        return self.components.physics

    def calculate_structural_fidelity(self, material_correctness: float,
                                    architectural_fidelity: float,
                                    deviation_reference: float,
                                    level: int) -> float:
        """Calculate structural fidelity
        F_s(l) = (M_c * A_f) / D_r
        """
        numerator = material_correctness * architectural_fidelity
        denominator = max(deviation_reference, 0.001)
        
        self.components.structural = np.clip(numerator / denominator, 0, 1)
        return self.components.structural

    def calculate_behavioral_fidelity(self, social_response: float,
                                    cultural_dynamics: float,
                                    human_baseline: float,
                                    emergent_factor: float,
                                    beta: float = 0.5) -> float:
        """Calculate behavioral fidelity
        F_b(t) = β * (S_r * C_d / V_h) * (1 + E_f)
        """
        base_fidelity = (social_response * cultural_dynamics) / max(human_baseline, 0.001)
        
        self.components.behavioral = np.clip(
            beta * base_fidelity * (1 + emergent_factor), 
            0, 
            1
        )
        return self.components.behavioral

    def calculate_cognitive_fidelity(self, reasoning_capability: float,
                                   learning_efficiency: float,
                                   consciousness_emergence: float,
                                   theoretical_ceiling: float) -> float:
        """Calculate cognitive fidelity
        F_c(t) = (R_c * L_e * (1 + C_e)) / T_c
        """
        numerator = reasoning_capability * learning_efficiency * (1 + consciousness_emergence)
        denominator = max(theoretical_ceiling, 0.001)
        
        self.components.cognitive = np.clip(numerator / denominator, 0, 1)
        return self.components.cognitive

    def calculate_data_fidelity(self, data_accuracy: float,
                               update_frequency: float,
                               error_rate: float,
                               quality_factor: float) -> float:
        """Calculate data fidelity
        F_d(t) = (D_a * U_f) / (1 + E_r) * Q_f
        """
        base_fidelity = (data_accuracy * update_frequency) / (1 + error_rate)
        
        self.components.data = np.clip(base_fidelity * quality_factor, 0, 1)
        return self.components.data

    def calculate_total_fidelity(self) -> float:
        """Calculate total system fidelity
        F_total(t) = Σ(α_k * F_k(t))
        """
        total = (
            self.weights['physics'] * self.components.physics +
            self.weights['structural'] * self.components.structural +
            self.weights['behavioral'] * self.components.behavioral +
            self.weights['cognitive'] * self.components.cognitive +
            self.weights['data'] * self.components.data
        )
        return np.clip(total, 0, 1)

    def update_weights(self, new_weights: Dict[str, float]):
        """Update component weights"""
        if sum(new_weights.values()) != 1.0:
            raise ValueError("Weights must sum to 1.0")
        self.weights = new_weights

    def get_component_scores(self) -> Dict[str, float]:
        """Get all component scores"""
        return {
            'physics': self.components.physics,
            'structural': self.components.structural,
            'behavioral': self.components.behavioral,
            'cognitive': self.components.cognitive,
            'data': self.components.data,
            'total': self.calculate_total_fidelity()
        }