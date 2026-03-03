
import os
import django
import sys

sys.path.append(r'c:\Users\admin\Documents\gone\city360UPDATED\city360UPDATED\city360UPDATED\city360')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'city360.settings')
django.setup()

from app.models import Payment, Booking

# Find a worker ID that has bookings
# We know from previous steps there is a booking with ID 20, let's see its worker ID
b = Booking.objects.filter(id=20).first()
if b:
    worid_str = b.worid
    print(f"Testing with Worker ID (str): '{worid_str}'")
    
    # Simulate the query
    payments = Payment.objects.filter(booking__worid=worid_str)
    print(f"Found {payments.count()} payments for this worker.")
    
    for p in payments:
        print(f"Payment {p.id}: Booking {p.booking.id}, Amount {p.amount}, Date {p.date}")
        print(f"  Booking User: {p.booking.usrid.name}")
else:
    print("Booking 20 not found, trying generic search...")
    # Just list all payments and their worker IDs
    for p in Payment.objects.all():
         if p.booking:
             print(f"Payment {p.id} -> Booking {p.booking.id} -> Worker {p.booking.worid}")
