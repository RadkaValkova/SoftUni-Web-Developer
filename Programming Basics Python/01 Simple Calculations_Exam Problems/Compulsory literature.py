pages = int(input())
page_for_an_hour = int(input())
days = int(input())

hours_for_the_book = pages/page_for_an_hour
hours_every_day = hours_for_the_book/days

print(hours_every_day)