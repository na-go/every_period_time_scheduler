from __future__ import print_function
import datetime
import pickle
import os.path
import calendar
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Change on lines 93 and 99
# Write the calenderID on 110 line
 
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Acquisition_Date_List
def Acquisition_Date(start_year,start_month,start_date,term = 30 , period = 12):
  dt_now = datetime.datetime.now()
  this_month = start_month
  this_date = start_date
  this_year = start_year
  this_month_list_reverse = calendar.monthcalendar(this_year, this_month)
  end_of_this_month = 0
  # Take an "end of this month"
  for tmlr in this_month_list_reverse:
    for date in tmlr:
      if date !=0:
        end_of_this_month = date

  update_date = this_date
  update_month = this_month
  update_year = this_year
  reservation_list = []
  while(period):

    if update_date + term > end_of_this_month:
      if update_month == 12:
        update_year += 1
        reservation_year = update_year
      else :
        reservation_year = update_year
      if update_month == 12 :
        reservation_month = 1
        update_month = 1
      else :
        reservation_month = update_month + 1
        update_month += 1
      over_date = update_date + term - end_of_this_month
      reservation_date = over_date
      
      print(reservation_year,"年",reservation_month,"月",reservation_date,"日")
      update_date = over_date

    else :
      reservation_year = update_year
      reservation_month = update_month
      reservation_date = update_date + term
      print(reservation_year,"年",reservation_month,"月",reservation_date,"日")
      update_date += term
    period -= 1

    update_month_list_reverse = calendar.monthcalendar(update_year, update_month)
    for umlr in update_month_list_reverse:
      for udate in umlr:
        if udate != 0:
          end_of_this_month = udate
    reservation_list.append([reservation_year,reservation_month,reservation_date])
  return reservation_list

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Acquisition_Date(start_year,start_month,start_date,term,period)
    event_date_list = Acquisition_Date(2020,4,17,30,12)

    for here_date in event_date_list:

        event = {
        # Title
        'summary': '御伽原江良メンバーシップ更新日',
        'start': {
            'dateTime': '{}-{}-{}T00:00:00'.format(here_date[0],here_date[1],here_date[2]),
            'timeZone': 'Japan',
        },
        'end': {
            'dateTime': '{}-{}-{}T00:23:59'.format(here_date[0],here_date[1],here_date[2]),
            'timeZone': 'Japan',
        },
        }
    # Deleate "calenderID" later when upload this to github
        event = service.events().insert(calendarId='ここにID',
                                        body=event).execute()
        print (event['id'])

if __name__ == '__main__':
    main()