from django.shortcuts import render
# Create your views here.
import random
from datetime import datetime, timedelta
from core.models import Reporting, Service
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Kiambu County EMS \n Welcome! \n Which service would you like to access? \n"  
            response += "1. List of services offered  \n"
            response += "2. Check Report status \n"
            response += "3. Report Emergency \n"
            response += "4. Cancel a report \n"
            response += "5. Report suspicious activity"

         #User needs a list of all services   
        elif text == "1":
            results=Service.objects.all()
            for i in results:
                response += f"END {i}:{i.start}-{i.finish} @KSHS{i.price} \n \n"

        elif text == "2":
            response = "CON Choose an option \n"
            response += "1. All reports \n"
            response += "2. Today active reports"

         #Follow up
        elif text == '2*1':
            tickets=Reporting.objects.filter(
                customer=phone_number
            )
            for tkt in tickets:
                response += f"END Ticket {tkt.id} on {tkt.departure:%Y-%m-%d %H:%M}"

         #Follow up
        elif text == '2*2':
            now = datetime.now()
            tickets=Reporting.objects.filter(
                customer=phone_number,
                departure__date=now
            )
            if tickets:
                for tkt in tickets:
                    response += f"END Ticket {tkt.id} on {tkt.departure:%Y-%m-%d %H:%M}"
            response ='END No reports found'

        #User wants to report a identifier
        elif text == "3":
            response = "CON Okay, Whats your emergency? \n"
            response += "1. Road Accident \n"
            response += "2. Fire Incident \n"
            response += "3. Robbery/Crime \n"
            response += "4. Medical Emergency \n"
            response += "5. Sexual Abuse \n"
            response += "6. Domestic Violence \n"
            response += "7. Suspicious activity "

        #Follow up RA
        elif text == '3*1':
            identifier=random.randint(1,30)
            services=Service.objects.filter(SERVICE_CATEGORY="RA", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=1)
            new_reporting=Reporting.objects.create(
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure

            )
            response = f"END  Alright! Here is your reporting info: \n TICKET NO {new_reporting.id} \n Service Number is {service} \n Your identifier number is {identifier} \n Your service leaves at {departure:%H:%M:%S}" 

        #Follow up FI
        elif text == '3*2':
            identifier=random.randint(40,70)
            services=Service.objects.filter(SERVICE_CATEGORY="FI", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=1)
            new_reporting=Reporting.objects.create(
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure

            )
            response = f"END  Alright! Here is your reporting info: \n TICKET NO {new_reporting.id} \n Service Number is {service} \n Your identifier number is {identifier} \n Your service leaves at {departure:%H:%M:%S}"

        #Follow up RC
        elif text == '3*3':
            identifier=random.randint(80,110)
            services=Service.objects.filter(SERVICE_CATEGORY="RC", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=1)
            new_reporting=Reporting.objects.create(
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure

            )
            response = f"END  Alright! Here is your reporting info: \n TICKET NO {new_reporting.id} \n Service Number is {service} \n Your identifier number is {identifier} \n Your service leaves at {departure:%H:%M:%S}"

        #Follow up ME
        elif text == '3*4':
            identifier=random.randint(120,150)
            services=Service.objects.filter(SERVICE_CATEGORY="ME", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=1)
            new_reporting=Reporting.objects.create(
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure

            )
            response = f"END  Alright! Here is your reporting info: \n TICKET NO {new_reporting.id} \n Service Number is {service} \n Your identifier number is {identifier} \n Your service leaves at {departure:%H:%M:%S}"

        #Follow up SA
        elif text == '3*5':
            identifier=random.randint(160,190)
            services=Service.objects.filter(SERVICE_CATEGORY="SA", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=1)
            new_reporting=Reporting.objects.create(
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure

            )
            response = f"END  Alright! Here is your reporting info: \n TICKET NO {new_reporting.id} \n Service Number is {service} \n Your identifier number is {identifier} \n Your service leaves at {departure:%H:%M:%S}"

        #Follow up DA
        elif text == '3*6':
            identifier=random.randint(200,230)
            services=Service.objects.filter(SERVICE_CATEGORY="DA", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=1)
            new_reporting=Reporting.objects.create(
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure

            )
            response = f"END  Alright! Here is your reporting info: \n TICKET NO {new_reporting.id} \n Service Number is {service} \n Your identifier number is {identifier} \n Your service leaves at {departure:%H:%M:%S}"

        #Follow up SUA
        elif text == '3*7':
            identifier=random.randint(240,270)
            services=Service.objects.filter(SERVICE_CATEGORY="SUA", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=1)
            new_reporting=Reporting.objects.create(
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure

            )
            response = f"END  Alright! Here is your reporting info: \n TICKET NO {new_reporting.id} \n Service Number is {service} \n Your identifier number is {identifier} \n Your service leaves at {departure:%H:%M:%S}"

         
        elif text == "4":
            response = "END Feature work in progress, check again soon"
        elif text == "5":
            response = "END Feature work in progress, check again soon"

        return HttpResponse(response)