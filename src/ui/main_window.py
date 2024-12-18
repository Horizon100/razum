from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTabWidget, QLabel, QStatusBar, QGroupBox, QSplitter, QFrame
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor

from src.core.simulation_engine import SimulationEngine

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load and set stylesheet using relative path from current file location
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        style_path = os.path.join(current_dir, 'style.qss')
        
        with open(style_path, 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
            self.simulation_engine = SimulationEngine()
            self.setWindowTitle("Virtual City Simulation")
            self.setGeometry(100, 100, 1200, 800)
            self.setup_ui()

    def setup_animations(self):
        # For buttons
        for button in self.findChildren(QPushButton):
            button.enterEvent = lambda e, b=button: self.start_hover_animation(b, True)
            button.leaveEvent = lambda e, b=button: self.start_hover_animation(b, False)

    def start_hover_animation(self, widget, hover_in):
        # Create animation
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(200)
        anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        if hover_in:
            anim.setEndValue(widget.pos().y() - 2)
        else:
            anim.setEndValue(widget.pos().y() + 2)
        
        anim.start()


    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        self.setup_animations()

        # Create main tab widget
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # Add tabs
        self.tabs.addTab(self.create_simulation_tab(), "Simulation")
        self.tabs.addTab(self.create_ai_tab(), "AI Systems")
        self.tabs.addTab(self.create_economy_tab(), "Economy")
        self.tabs.addTab(self.create_legal_tab(), "Legal Framework")

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("System Ready")

    def create_simulation_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Create horizontal splitter for main layout
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left panel - Controls and Parameters
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # Control section
        controls_group = QGroupBox("Simulation Controls")
        controls_group.setProperty('class', 'sliding-widget')
        controls_layout = QVBoxLayout()
        
        # Button container
        buttons_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start Simulation")
        self.start_btn.setProperty('class', 'success-button')

        self.pause_btn = QPushButton("Pause")
        self.pause_btn.setProperty('class', 'warning-button')

        self.stop_btn = QPushButton("Stop")
        self.stop_btn.setProperty('class', 'danger-button')
        
        buttons_layout.addWidget(self.start_btn)
        buttons_layout.addWidget(self.pause_btn)
        buttons_layout.addWidget(self.stop_btn)
        
        controls_layout.addLayout(buttons_layout)
        controls_group.setLayout(controls_layout)
        left_layout.addWidget(controls_group)
        
        # Parameters section
        params_group = QGroupBox("Parameters")
        params_group.setProperty('class', 'sliding-widget')
        params_layout = QVBoxLayout()
        # Add parameter controls here
        params_group.setLayout(params_layout)
        left_layout.addWidget(params_group)
        
        # Center panel - Visualization
        center_panel = QWidget()
        center_layout = QVBoxLayout(center_panel)
        
        vis_group = QGroupBox("Visualization")
        vis_group.setProperty('class', 'sliding-widget')
        vis_layout = QVBoxLayout()
        # Add visualization widget here
        vis_group.setLayout(vis_layout)
        center_layout.addWidget(vis_group)
        
        # Right panel - Metrics and Analysis
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Metrics section
        metrics_group = QGroupBox("Simulation Metrics")
        metrics_group.setProperty('class', 'sliding-widget')
        metrics_layout = QVBoxLayout()
        
        self.fidelity_label = QLabel("Fidelity Index: 2.0")
        self.economic_label = QLabel("Economic Health: 3.0")
        self.ai_label = QLabel("AI Evolution: 3.0")
        self.legal_label = QLabel("Legal Compliance: 4.0")

        self.fidelity_label.setProperty('class', 'metric-label')
        self.economic_label.setProperty('class', 'metric-label')
        self.ai_label.setProperty('class', 'metric-label')
        self.legal_label.setProperty('class', 'metric-label')

            
        
        metrics_layout.addWidget(self.fidelity_label)
        metrics_layout.addWidget(self.economic_label)
        metrics_layout.addWidget(self.ai_label)
        metrics_layout.addWidget(self.legal_label)
        
        metrics_group.setLayout(metrics_layout)
        right_layout.addWidget(metrics_group)
        
        # Analysis section
        analysis_group = QGroupBox("Analysis")
        analysis_group.setProperty('class', 'sliding-widget')
        analysis_layout = QVBoxLayout()
        # Add analysis widgets here
        analysis_group.setLayout(analysis_layout)
        right_layout.addWidget(analysis_group)
        
        # Add panels to splitter
        splitter.addWidget(left_panel)
        splitter.addWidget(center_panel)
        splitter.addWidget(right_panel)
        
        # Set initial sizes
        splitter.setSizes([300, 600, 300])
        
        layout.addWidget(splitter)
        return tab

    def create_ai_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left panel - Controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        ai_controls = QGroupBox("AI Controls")
        controls_layout = QVBoxLayout()
        add_agent_btn = QPushButton("Add AI Agent")
        add_agent_btn.setProperty('class', 'primary-button')
        add_entity_btn = QPushButton("Add AI Entity")
        add_entity_btn.setProperty('class', 'primary-button')
        
        controls_layout.addWidget(add_agent_btn)
        controls_layout.addWidget(add_entity_btn)
        ai_controls.setLayout(controls_layout)
        left_layout.addWidget(ai_controls)
        
        # Center panel - Visualization
        center_panel = QWidget()
        center_layout = QVBoxLayout(center_panel)
        
        vis_group = QGroupBox("AI Network Visualization")
        vis_layout = QVBoxLayout()
        # Add visualization widget here
        vis_group.setLayout(vis_layout)
        center_layout.addWidget(vis_group)
        
        # Right panel - Metrics
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        metrics_group = QGroupBox("AI Metrics")
        metrics_layout = QVBoxLayout()
        # Add metrics widgets here
        metrics_group.setLayout(metrics_layout)
        right_layout.addWidget(metrics_group)
        
        splitter.addWidget(left_panel)
        splitter.addWidget(center_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([300, 600, 300])
        
        layout.addWidget(splitter)
        return tab

    def create_economy_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        economy_controls = QHBoxLayout()
        market_btn = QPushButton("Market Overview")
        market_btn.setProperty('class', 'primary-button')
        transactions_btn = QPushButton("Transactions")
        transactions_btn.setProperty('class', 'primary-button')

        economy_controls.addWidget(market_btn)
        economy_controls.addWidget(transactions_btn)
        
        layout.addLayout(economy_controls)
        
        economic_data = QLabel("Economic Metrics")
        economic_data.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(economic_data)
        
        return tab

    def create_legal_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        legal_controls = QHBoxLayout()
        compliance_btn = QPushButton("Compliance Check")
        compliance_btn.setProperty('class', 'primary-button')
        regulations_btn = QPushButton("Regulations")
        regulations_btn.setProperty('class', 'primary-button')
        regulations_btn = QPushButton("Regulations")
        
        legal_controls.addWidget(compliance_btn)
        legal_controls.addWidget(regulations_btn)
        
        layout.addLayout(legal_controls)
        
        legal_status = QLabel("Legal Framework Status")
        legal_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(legal_status)
        
        return tab

    def start_simulation(self):
        self.simulation_engine.start()
        self.update_metrics()
        self.status_bar.showMessage("Simulation Running")

    def pause_simulation(self):
        self.simulation_engine.pause()
        self.status_bar.showMessage("Simulation Paused")

    def stop_simulation(self):
        self.simulation_engine.pause()
        self.status_bar.showMessage("Simulation Stopped")

    def update_metrics(self):
        metrics = self.simulation_engine.get_metrics()
        self.fidelity_label.setText(f"Fidelity Index: {metrics['fidelity_index']:.3f}")
        self.economic_label.setText(f"Economic Health: {metrics['economic_health']:.3f}")
        self.ai_label.setText(f"AI Evolution: {metrics['ai_evolution']:.3f}")
        self.legal_label.setText(f"Legal Compliance: {metrics['legal_compliance']:.3f}")