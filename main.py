import sys
from PyQt6.QtWidgets import QApplication
from src.ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

# src/ui/main_window.py
from PyQt6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout, 
    QPushButton,
    QTabWidget,
    QLabel,
    QStatusBar
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual City Simulation")
        self.setGeometry(100, 100, 1200, 800)
        self.setup_ui()

    def setup_ui(self):
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Create tab widget for different sections
        tabs = QTabWidget()
        main_layout.addWidget(tabs)

        # Add tabs for different components
        tabs.addTab(self.create_simulation_tab(), "Simulation")
        tabs.addTab(self.create_ai_tab(), "AI Systems")
        tabs.addTab(self.create_economy_tab(), "Economy")
        tabs.addTab(self.create_legal_tab(), "Legal Framework")

        # Add status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("System Ready")

    def create_simulation_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Controls section
        controls_layout = QHBoxLayout()
        start_btn = QPushButton("Start Simulation")
        pause_btn = QPushButton("Pause")
        stop_btn = QPushButton("Stop")
        
        controls_layout.addWidget(start_btn)
        controls_layout.addWidget(pause_btn)
        controls_layout.addWidget(stop_btn)
        
        # Add to main layout
        layout.addLayout(controls_layout)
        
        # Placeholder for simulation view
        simulation_view = QLabel("Simulation View")
        simulation_view.setAlignment(Qt.AlignmentFlag.AlignCenter)
        simulation_view.setStyleSheet("border: 2px solid gray;")
        layout.addWidget(simulation_view)
        
        return tab

    def create_ai_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # AI Systems controls
        ai_controls = QHBoxLayout()
        add_agent_btn = QPushButton("Add AI Agent")
        add_entity_btn = QPushButton("Add AI Entity")
        
        ai_controls.addWidget(add_agent_btn)
        ai_controls.addWidget(add_entity_btn)
        
        layout.addLayout(ai_controls)
        
        # Placeholder for AI metrics
        ai_metrics = QLabel("AI Systems Metrics")
        ai_metrics.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(ai_metrics)
        
        return tab

    def create_economy_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Economy controls
        economy_controls = QHBoxLayout()
        market_btn = QPushButton("Market Overview")
        transactions_btn = QPushButton("Transactions")
        
        economy_controls.addWidget(market_btn)
        economy_controls.addWidget(transactions_btn)
        
        layout.addLayout(economy_controls)
        
        # Placeholder for economic data
        economic_data = QLabel("Economic Metrics")
        economic_data.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(economic_data)
        
        return tab

    def create_legal_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Legal framework controls
        legal_controls = QHBoxLayout()
        compliance_btn = QPushButton("Compliance Check")
        regulations_btn = QPushButton("Regulations")
        
        legal_controls.addWidget(compliance_btn)
        legal_controls.addWidget(regulations_btn)
        
        layout.addLayout(legal_controls)
        
        # Placeholder for legal status
        legal_status = QLabel("Legal Framework Status")
        legal_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(legal_status)
        
        return tab