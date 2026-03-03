# City 360 - On-Demand Service Platform

City 360 is a modern, professional web application designed to connect users with skilled service workers (like electricians, plumbers, and more). The platform provides a seamless interface for booking services, managing workers, and ensuring high-quality interactions through a robust feedback system.

## 🚀 Key Features

### 👤 User Management
- **Service Discovery**: Browse workers by category with detailed profiles and ratings.
- **Easy Booking**: Quick and intuitive booking process for various household and professional services.
- **Feedback System**: Post-service feedback to ensure service quality and reliability.
- **Chat**: Real-time communication with workers for job coordination.

### 👷 Worker Management
- **Job History**: Track all completed and ongoing work with payment status.
- **Profile Customization**: Manage professional details, wages, and categories.
- **Service Feedback**: Workers can also provide feedback on jobs and user interactions.

### 🛡️ Administrative Terminal
- **Visual Dashboards**: Modern, card-based layouts for managing Users, Workers, and Categories.
- **Blocking System**: Robust account management with the ability to block/unblock users and workers.
- **Category Control**: Dynamic management of service categories including name and image updates.
- **Feedback Moderation**: Monitor and manage feedback from both users and workers.

## 💻 Technical Overhaul
Recent updates have significantly improved the platform's reliability and aesthetic:
- **Premium Design**: Overhauled all admin and key user interfaces with a professional, card-based aesthetic.
- **State Management**: Implemented a comprehensive account status system (Pending, Approved, Blocked).
- **Bug Fixes**: Resolved critical issues in registration flows and feedback routing.

## 🛠️ Technology Stack
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3 (Premium styling), JavaScript
- **Database**: SQLite (Development) / Exported SQL provided

## 📝 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/VishnuSuresh0204/City_360.git
   ```
2. Install dependencies (Python 3.x required).
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

---
*Developed as part of the City 360 Modernization Project.*
