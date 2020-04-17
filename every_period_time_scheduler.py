import calendar
import datetime

def Acquisition_Date(term, period):
  dt_now = datetime.datetime.now()
  this_month = int(dt_now.strftime("%m"))
  this_date = int(dt_now.strftime("%d"))
  this_year = int(dt_now.strftime("%Y"))
  this_month_list_reverse = calendar.monthcalendar(this_year, this_month)
  end_of_this_month = 0
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

date_list = Acquisition_Date(30,5)
print(date_list)