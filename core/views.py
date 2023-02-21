from django.shortcuts import render
# Create your views here.
import os
import random
import africastalking
from datetime import datetime, timedelta
from core.models import Reporting, Service, Responder, userLocation
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from dotenv import load_dotenv

# the load_dotenv function gets the environment variables defined in .env file
load_dotenv()

# Initialize SDK
#username = os.getenv("username")
username = "I-sema" 
api_key = os.getenv("SANDBOX_API_KEY")    
africastalking.initialize(username, api_key)

sms = africastalking.SMS

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        response = ""

        def send_messages():
            print('phone_number')
            alert='Request received on iSema. Our emergency response team will contact you for additional information.'
            message=alert
            print(phone_number)
            recipients=[str(phone_number), '+254791573545']
            responsed =sms.send(message, recipients)
            print(responsed)

        def emergency_location():
            # Prompt the user to input their location
            response = "CON iSema\n"
            response += "Please enter your current location:\n (e.g. Kimbo, Ruiru)\n"
            # Store the reporting details (including location) in a database or file
            print(text)
            location = text
            new_userlocation = userLocation.objects.create(
                phone_number=phone_number,
                location=location
            )
            
        if text == "":
            response = "CON iSema\n Welcome! \n Which service would you like to access? \n"  
            response += "1. List of service providers  \n"
            response += "2. Check Report status \n"
            response += "3. Report Emergency \n"
            response += "4. Cancel a report \n"
            response += "5. First Aid Training"

         #User wants to see list of service responders
        elif text == "1":
            response = "CON Select to list: \n"
            response += "1. Hospitals \n"
            response += "2. Ambulance Service \n"
            response += "3. Police \n"
            response += "4. Tow service \n"
            response += "5. Fire department \n"
            response += "6. Gender officers \n"
            response += "7. Couselling centers "

        #Follow up Hos
        elif text == '1*1':
            providers=Responder.objects.filter(category="Hospital")
            for i in providers:
                response += f"END {i} \n \n"

        #Follow up Amb
        elif text == '1*2':
            providers=Responder.objects.filter(category="Ambulance")
            for i in providers:
                response += f"END {i} \n \n"

        #Follow up Police
        elif text == '1*3':
            providers=Responder.objects.filter(category="Police")
            for i in providers:
                response += f"END {i} \n \n"

        #Follow up ts
        elif text == '1*4':
            providers=Responder.objects.filter(category="Tow Service")
            for i in providers:
                response += f"END {i} \n \n"

        #Follow up FD
        elif text == '1*5':
            providers=Responder.objects.filter(category="Fire Station")
            for i in providers:
                response += f"END {i} \n \n"

        #Follow up GO
        elif text == '1*6':
            providers=Responder.objects.filter(category="Gender service")
            for i in providers:
                response += f"END {i} \n \n"

        #Follow up CC
        elif text == '1*7':
            providers=Responder.objects.filter(category="Couselling Center")
            for i in providers:
                response += f"END {i} \n \n"

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
                response += f"END Ticket {tkt.id} on {tkt.departure:%Y-%m-%d %H:%M}{tkt.status}"

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
            else:
                response ='END No reports found'

        #User wants to report a identifier
        elif text == "3":
            response = "CON Okay, Whats your emergency? \n"
            response += "1. Road Accident \n"
            response += "2. Fire Incident \n"
            response += "3. Robbery/Crime \n"
            response += "4. Medical Emergency \n"
            response += "5. GBV \n"
            response += "6. Child Services \n"
            response += "7. Death "

        #Follow up RA
        elif text == '3*1':
            response = "CON iSema\n"
            response += "Please enter your current location:\n (e.g. Kimbo, Ruiru)\n"
            

        elif text[:5] == "3*1*":
            identifier=random.randint(1,30)
            services=Service.objects.filter(SERVICE_CATEGORY="RA", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=4)
            new_reporting=Reporting.objects.create(
                SERVICECATEGORY="RA",
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure
                )
            
            # Store the reporting details (including location) in a database or file
            print(text)
            location = text[5:]
            new_userlocation = userLocation.objects.create(
                phone_number=phone_number,
                location=location
            )
            send_messages()
            

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
                SERVICECATEGORY="FI",
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure
                )
            send_messages()
            response = f"END  Successful! Report info: \n TICKET ID 678{new_reporting.id} \n Service {service} \n Your case number is 8976{identifier} \n Closses at {departure:%H:%M:%S}"

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
                SERVICECATEGORY="RC",
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure
                )
            send_messages()
            response = f"END  Successful! Report info: \n TICKET ID 678{new_reporting.id} \n Service {service} \n Your case number is 8976{identifier} \n Closses at {departure:%H:%M:%S}"

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
                SERVICECATEGORY="ME",
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure
                )
            send_messages()
            response = f"END  Successful! Report info: \n TICKET ID 678{new_reporting.id} \n Service {service} \n Your case number is 8976{identifier} \n Closses at {departure:%H:%M:%S}"

        #Follow up GBV
        elif text == '3*5':
            identifier=random.randint(160,190)
            services=Service.objects.filter(SERVICE_CATEGORY="GBV", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=1)
            new_reporting=Reporting.objects.create(
                SERVICECATEGORY="GBV",
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure
                )
            send_messages()
            response = f"END  Successful! Report info: \n TICKET ID 678{new_reporting.id} \n Service {service} \n Your case number is 8976{identifier} \n Closses at {departure:%H:%M:%S}"

        #Follow up CR
        elif text == '3*6':
            identifier=random.randint(200,230)
            services=Service.objects.filter(SERVICE_CATEGORY="CR", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=1)
            new_reporting=Reporting.objects.create(
                SERVICECATEGORY="CR",
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure
                )
            send_messages()
            response = f"END  Successful! Report info: \n TICKET ID 678{new_reporting.id} \n Service {service} \n Your case number is 8976{identifier} \n Closses at {departure:%H:%M:%S}"

        #Follow up SUD
        elif text == '3*7':
            identifier=random.randint(240,270)
            services=Service.objects.filter(SERVICE_CATEGORY="SUD", is_available=True)
            services=[service for service in services]
            service=random.choices(services)
            for i in service:
                service=i
            departure=datetime.now() + timedelta(hours=1)
            new_reporting=Reporting.objects.create(
                SERVICECATEGORY="SUD",
                service=service,
                customer=phone_number,
                identifier=identifier,
                departure=departure
                )
            send_messages()
            response = f"END  Successful! Report info: \n TICKET ID 678{new_reporting.id} \n Service {service} \n Your case number is 8976{identifier} \n Closses at {departure:%H:%M:%S}"

         
        elif text == "4":
            response = "END Feature work in progress, check again soon"
        elif text == "5":
            response = "END Feature work in progress, check again soon"

        return HttpResponse(response)
