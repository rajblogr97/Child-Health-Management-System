# Child-Health-Management-System
Baby Child Health Tracker (2026 Edition)
A lightweight, terminal-based Python application designed to help parents and healthcare providers monitor child growth milestones. This system compares a child's weight and height against standardized growth data for children aged 0 to 6 years.

🚀 Overview
Tracking physical development in the early years is crucial. This Child Health Tracker provides instant access to "Normal" growth parameters based on the latest 2026 reference data. It serves as a quick-reference tool to ensure infants and toddlers are meeting their developmental benchmarks.


✨ Key Features
Gender-Specific Data: Separate logic and databases for Male and Female growth patterns.
Granular Age Tracking: Supports monthly tracking for infants (1–12 months) and yearly tracking for children (1–6 years).
Instant Validation: Immediate feedback on target weight (kg) and height (cm).
User-Friendly Interface: Simple CLI (Command Line Interface) with clear instructions and error handling.


🛠️ How It Works
The system uses a key-value mapping system to retrieve data:
Months: Input as 0.1 (1 month) through 0.12 (12 months).
Years: Input as 1.0 through 6.0.

Enter Gender (m/f): m
Enter Age: 2.0

✅ DATA FOUND FOR MALE
--------------------------------
Age           : 2.0
Normal Weight : 12.2 kg
Normal Height : 87.8 cm
--------------------------------
