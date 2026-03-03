
import os
import django
import sys

sys.path.append(r'c:\Users\admin\Documents\gone\city360UPDATED\city360UPDATED\city360UPDATED\city360')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'city360.settings')
django.setup()

from app.models import Payment, Booking

print("Checking Payment objects...")
payments = Payment.objects.all()
for p in payments:
    print(f"Payment ID: {p.id}, Amount: '{p.amount}', Date: {p.date}")
    if p.booking:
        print(f"  Booking ID: {p.booking.id}, Wages: {p.booking.wages}")
    else:
        print("  No Booking associated")

print("-" * 20)
print("Checking Booking objects...")
bookings = Booking.objects.all()
for b in bookings:
    print(f"Booking ID: {b.id}, Wages: '{b.wages}', Status: {b.status}")
