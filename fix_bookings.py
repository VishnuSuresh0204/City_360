
import os
import django
import sys
from datetime import datetime

sys.path.append(r'c:\Users\admin\Documents\gone\city360UPDATED\city360UPDATED\city360UPDATED\city360')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'city360.settings')
django.setup()

from app.models import Booking, WorkersReg

print("Starting remediation for zero-wage bookings...")

# Filter bookings with 0 wages (checking both string "0" and potentially empty/null if that's an issue, but focusing on 0)
# Note: wages is CharField in models.py, so we check for "0"
bookings = Booking.objects.filter(wages="0")
print(f"Found {bookings.count()} bookings with 0 wages.")

count = 0
for booking in bookings:
    try:
        # Get worker
        # booking.worid is CharField but stores ID.
        worid = int(booking.worid)
        worker = WorkersReg.objects.get(id=worid)
        
        # Get dates
        start_str = booking.startingdate
        end_str = booking.endingdate
        
        sdate = datetime.strptime(start_str, "%Y-%m-%d")
        edate = datetime.strptime(end_str, "%Y-%m-%d")
        
        # New Inclusive Logic
        date_diff = edate - sdate
        days = date_diff.days + 1
        
        if days < 1:
            # Should not happen for valid bookings but safety check
            days = 1
            
        worker_wage = float(worker.wages) if worker.wages else 0
        new_total_wage = int(days * worker_wage)
        
        print(f"Booking {booking.id}: {start_str} to {end_str} ({days} days) @ {worker_wage}/day. Updating 0 -> {new_total_wage}")
        
        booking.wages = str(new_total_wage)
        booking.save()
        count += 1
        
    except Exception as e:
        print(f"Error processing Booking {booking.id}: {e}")

print(f"Successfully updated {count} bookings.")
